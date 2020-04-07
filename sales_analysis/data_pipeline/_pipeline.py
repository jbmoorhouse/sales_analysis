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