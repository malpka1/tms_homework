class Product:
    def __init__(self, idp, name, price, amount):
        self.idp = idp
        self.name = name
        self.price = price
        self.amount = amount


        @classmethod
        def new_product(cls, idp, name, price, amount):
            return cls(name, idp, price, amount)

aples = Product.new_product(6,'aples',10, 100)
print(aples)


milk = Product(1, 'milk', 10, 10)
cheese = Product(2, 'cheese', 20, 5)
bread = Product(3, 'bread', 10, 20)
tea = Product(4, 'tea', 10, 10)
cola = Product(5, 'cola', 12, 10)


class Store(Product):
    def __init__(self, product):
        self.product = product

class Big_store:
    def __new__(cls):
        if not hasattr(cls, 'big_store'):
            cls.big_store = super(Big_store, cls).__new__(cls)
        return cls.big_store


product = ['milk', 'bread', 'cheese', 'tea', 'cola']
store = Store(product)
print(store.product)


class Basket(Product):
    def __init__(self, id, products_in_basket):
        self.id = id
        self.product_in_basket = products_in_basket


class Buyer(Product):
    def __init__(self, idp, money, list_of_products, basket):
        self.idp = idp
        self.money = money
        self.list_of_products = list_of_products
        self.basket = basket


    def __str__(self):
        return f"Buyer: id - {self.idp}, money - {self.money}, list_of_products - {self.list_of_products}"


    def add_product_to_basket(self, product):
        if self.idp in self.list_of_products:
            if self.price <= self.money:
                if self.amount > 0:
                    self.idp.append(product)
        else:
            print("product missing")


buyer1 = Buyer(1, 200, ['cheese'], 1)
print(buyer1)
buyer1.add_product_to_basket(aples)


















