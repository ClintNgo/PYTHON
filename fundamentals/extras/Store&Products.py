class Store:
    store_name = "Walmart"
    stores = []
    def __init__(self, state, city):
        self.state = state   
        self.city = city


    def update_price(self, product, percent_change,is_increase):
        if (is_increase == 1):
            product.price += product.price * percent_change
            print(f"The price of {product.name} has increased {percent_change}x to {product.price}.")
        else:
            product.price -= product.price * percent_change
            print(f"The price of {product.name} has decreased {percent_change}x to {product.price}.")
        return self

    def print_info(self,product):
        print(f"Product name : {product.name} category : {product.category} count : {product.count}.")

class Product:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.count = 25
        self.price = 999.99
        self.store = Store("Missouri","Kansas City")

    # def add_product(self, new_product):
    #     new_product

    # def sell_product(self,id):
    #     id

    # def inflation(self, percentage_change):
    #     percentage_change

    # def set_clearance(self,category,percent_discount):
    #     category


walmart = Store("Missouri","Kansas City")
iphone = Product("iphone","electronic")

walmart.update_price(iphone,.50,0)