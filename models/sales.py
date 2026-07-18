class SalesItem:
    def __init__(self, product, quantity, rate, amount):
        self.product = product
        self.quantity = quantity
        self.rate = rate
        self.amount = amount

    def to_dict(self):
        return {
            "product": self.product,
            "quantity": self.quantity,
            "rate": self.rate,
            "amount": self.amount
        }