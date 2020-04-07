import pandas as pd 

# --------------------------------------------------------------------------
# Data pipeline

class SalesPipeline:
    # ----------------------------------------------------------------------
    # Constructors

    def __init__(self, **data):
        for k, v in data.items():
            setattr(self, k, v)
            
         self.merged_order_data = self._merge_order_data()

    # ----------------------------------------------------------------------
    # formatting methods 
            
    def _format_orders(self, orders):
        orders["created_at"] = pd.to_datetime(orders["created_at"]).dt.date
        return orders
    
    def _merge_order_data(self):
        orders = self._format_orders(self._orders)
        order_lines = self._order_lines
        
        return order_lines.merge(
            orders, 
            how="left", 
            left_on="order_id", 
            right_on="id",

    # ----------------------------------------------------------------------
    # statistics/calculation methods

    def _customer_count(self):
        orders = self._format_orders(self._orders)
        customer_count = orders.groupby("created_at")["customer_id"].nunique()
        customer_count.name = "customers"
        
        return customer_count
    
    def _total_discount(self):
        merged = self.merged_order_data  
        merged["total_discount"] = (
            merged["full_price_amount"] - merged["discounted_amount"])
        
        total_discount = merged.groupby("created_at")["total_discount"].sum()
        total_discount.name = "total_discount_amount"
        
        return total_discount
        
    def _item_count(self):
        sales_quantity = (self.merged_order_data
                 .groupby("created_at")["quantity"].sum())
        sales_quantity.name = "items"
        
        return sales_quantity
    
    def _mean_order_total(self):
        average_daily_order = (self.merged_order_data
                .groupby("created_at")['total_amount'].mean())
        average_daily_order.name = "order_total_avg"
        
        return average_daily_order
    
    def _mean_discount_rate(self):
        average_discount_rate = (self.merged_order_data
                .groupby("created_at")["discount_rate"].mean())
        average_discount_rate.name = "discount_rate_avg"
        
        return average_discount_rate