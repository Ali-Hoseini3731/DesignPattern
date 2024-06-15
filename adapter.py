from abstract_factory import Rugs


class AdapterPrice:
    def __init__(self, rate):
        self.rate = rate

    def exchange(self, product_price):
        return self.rate * product_price


if __name__ == "__main__":
    rate = int(input("enter rate today: "))
    adapter = AdapterPrice(rate)
    r1 = Rugs(name="Persion rugs", size=12, price=50, shipping="car")
    r2 = Rugs(name="Nain rugs", size=6, price=30, shipping="car")
    r3 = Rugs(name="Mashhad rugs", size=16, price=60, shipping="trailer")

    rugs = [r1, r2, r3]
    for rug in rugs:
        print(f"{rug.detail.show}\n{rug.shipping.show}\nprice: {adapter.exchange(rug._price)}$\n\n")
