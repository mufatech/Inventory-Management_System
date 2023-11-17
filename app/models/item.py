class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    daily_sales = db.column(db.float, default=0)
    stock_balance = db.column(db.float, default=0)
    price = db.column(db.float, nullable=False)
    stock_value = db.column(db.float, default=0)

    def __init__(self, item_name, quantity, daily_sales, stock_balance, price, stock_value=None):
        self.item_name = item_name
        self.quantity = quantity
        self.daily_sales = daily_sales
        self.stock_balance = stock_balance
        self.price = price
        self.stock_value = stock_value   
