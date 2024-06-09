class Singleton:
    instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(*args, **kwargs)
        return cls.instance

    def __int__(self):
        pass
