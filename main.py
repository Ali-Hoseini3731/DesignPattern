from singleton import Singleton

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    print(f"{id(s1)}------{id(s2)}--------{id(s1) == id(s2)}")
