from flask import Flask
import datetime as datetime
import pandas as pd 

class SalesPipeline:
    # ----------------------------------------------------------------------
    # Constructors

    def __init__(self, **data):
        for k, v in data.items():
            setattr(self, k, v)
            

