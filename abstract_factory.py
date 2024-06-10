from abc import ABC, abstractmethod


class ProductBase(ABC):
    @abstractmethod
    def detail(self):
        pass

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def shipping(self):
        pass


class DetailBase(ABC):
    @abstractmethod
    def show(self):
        pass


# *********************Rugs*********
class RugsDetail(DetailBase):

    def __init__(self, rugs):
        self.rugs = rugs

    @property
    def show(self):
        return f"details: {self.rugs.name}---{self.rugs.size} meter"


class RugsPrice(DetailBase):
    def __init__(self, rugs):
        self.rugs = rugs

    @property
    def show(self):
        return f"price: {self.rugs._price}"


class RugsShipping(DetailBase):
    def __init__(self, rugs):
        self.rugs = rugs

    @property
    def show(self):
        return f"shipping: {self.rugs._shipping}"


class Rugs(ProductBase):
    def __init__(self, name, size, price, shipping):
        self.name = name
        self.size = size
        self._price = price
        self._shipping = shipping

    @property
    def detail(self):
        return RugsDetail(self)

    @property
    def price(self):
        return RugsPrice(self)

    @property
    def shipping(self):
        return RugsShipping(self)


# **************************GiftCard

class GiftCartDetail(DetailBase):
    def __init__(self, cart):
        self.cart = cart

    @property
    def show(self):
        return f"company: {self.cart.company}"


class GiftCartPrice(DetailBase):
    def __init__(self, cart):
        self.cart = cart

    @property
    def show(self):
        return f"min_price: {self.cart.min_price}-----max_price: {self.cart.max_price}"


class GiftCartShipping(DetailBase):
    def __init__(self, cart):
        self.cart = cart

    @property
    def show(self):
        return f"shipping: {self.cart._shipping}"


class GiftCart(ProductBase):
    def __init__(self, company, min_price, max_price, shipping):
        self.company = company
        self.min_price = min_price
        self.max_price = max_price
        self._shipping = shipping

    @property
    def detail(self):
        return GiftCartDetail(self)

    @property
    def price(self):
        return GiftCartPrice(self)

    @property
    def shipping(self):
        return GiftCartShipping(self)


# ******************mobile*********

class MobileDetail(DetailBase):
    def __init__(self, mobile):
        self.mobile = mobile

    @property
    def show(self):
        return f"detail: {self.mobile.name}-----brand: {self.mobile.brand}"


class MobilePrice(DetailBase):
    def __init__(self, mobile):
        self.mobile = mobile

    @property
    def show(self):
        return f"price: {self.mobile._price}"


class MobileShipping(DetailBase):
    def __init__(self, mobile):
        self.mobile = mobile

    @property
    def show(self):
        return f"shipping: {self.mobile._shipping}"


class Mobile(ProductBase):
    def __init__(self, name, brand, price, shipping):
        self.name = name
        self.brand = brand
        self._price = price
        self._shipping = shipping

    @property
    def detail(self):
        return MobileDetail(self)

    @property
    def price(self):
        return MobilePrice(self)

    @property
    def shipping(self):
        return MobileShipping(self)


if __name__ == "__main__":
    r1 = Rugs(name="Mashhad", size=12, price=5000000, shipping="car")
    r2 = Rugs(name="Tabriz", size=6, price=3500000, shipping="car")

    g1 = GiftCart(company="Google", min_price=100000, max_price=500000, shipping="SMS")
    g2 = GiftCart(company="Facebook", min_price=50000, max_price=350000, shipping="SMS")

    m1 = Mobile(name="A24", brand="Samsung", price=7000000, shipping="Motor")
    m2 = Mobile(name="Pro_Max", brand="Iphone", price=20000000, shipping="Motor")

    products = [r1, r2, g1, g2, m1, m2]

    for product in products:
        print(product.detail.show)
        print(product.price.show)
        print(product.shipping.show,"\n\n")

