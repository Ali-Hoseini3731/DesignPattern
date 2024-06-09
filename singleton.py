class Singleton:
    instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(*args, **kwargs)
        return cls.instance


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    print(f"{id(s1)}------{id(s2)}--------{id(s1) == id(s2)}")