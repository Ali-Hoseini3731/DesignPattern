COUNTRIES = ["Iran", "UAE"]
TAX = {"Iran": 9, "UAE": 20}


class User:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"


class Address:
    def __init__(self, country):
        self.country = country


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Purchase:
    def __init__(self, user, address):
        self.user = user
        self.address = address
        self.product_list = list()

    def add_product(self, product_list):
        if not isinstance(product_list, list):
            product_list = [product_list]
        self.product_list.extend(product_list)

    def total_price(self):
        s = 0
        for product in self.product_list:
            s += product.price
        return s


def calculate_tax(func):
    def wrapped_func(pur):
        tax = TAX[pur.address.country]
        return pur.total_price() + pur.total_price() * tax / 100

    return wrapped_func


def show_total_price(pur):
    return pur.total_price()


@calculate_tax
def show_total_tax_price(pur):
    return pur.total_price()


if __name__ == "__main__":
    user1 = User(
        first_name="Ali", last_name="Hoseini", phone="09105572418", email="a.h.computer73@gmail.com"
    )

    addr_iran = Address(country=COUNTRIES[0])
    addr_uae = Address(country=COUNTRIES[1])

    p1 = Product(name="Mashhad Rugs", price=5000000)
    p2 = Product(name="lenovo tablet", price=7000000)
    p3 = Product(name="washing machine", price=15000000)

    purchase_iran = Purchase(user=user1, address=addr_iran)
    purchase_iran.add_product([p1, p2, p3])

    purchase_uae = Purchase(user=user1, address=addr_uae)
    purchase_uae.add_product([p1, p2, p3])

    print(f"{purchase_iran.user.fullname}---{purchase_iran.address.country}---: {show_total_price(purchase_iran)}")
    print(
        f"{purchase_iran.user.fullname}---{purchase_iran.address.country}---: {show_total_tax_price(purchase_iran)}\n")

    print(f"{purchase_uae.user.fullname}---{purchase_uae.address.country}---: {show_total_price(purchase_uae)}")
    print(f"{purchase_uae.user.fullname}---{purchase_uae.address.country}---: {show_total_tax_price(purchase_uae)}")
