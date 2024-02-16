
class Good:
    def __init__(self, price, amount=1, size, id) -> None:
        self.price = price
        self.amount = amount
        self.size = size
        self.id = id
    def buy(self, count):
        if count <1:
            return "Sorry"
        if count>self.amount:
            return "Sorry"
        self.amount_=count
    
    def sale(self, percentage):
        return (1-percentage)*self.price
    
    def __delete(self, sklad, count):
        sklad.remove(self.id, count)

class Acount:
    def __init__(self, name, address, phone, ac_id, cart) -> None:
        self.name = name
        self.address = address
        self.phone = phone
        self.ac_id = ac_id
        self.cart = cart
    def buy(self)
        order = self.cart
        self.cart=0
        order.ac_id = self.ac_id
        order.addres = self.address
        