from time import sleep


class Lazy:
    def __init__(self, cls):
        self.cls = cls
        self.object = None

    def __getattr__(self, item):
        if self.object is None:
            self.object = self.cls()
        return getattr(self.object, item)


class MySqlHandler:
    def __init__(self):
        sleep(1)

    def greeting(self):
        return "Hello form mysql"


class MongoDBHandler:
    def __init__(self):
        sleep(3)

    def greeting(self):
        return "Hello form mongo"


class PostgresHandler:
    def __init__(self):
        sleep(1)

    def greeting(self):
        return "Hello form postgres"


if __name__ == "__main__":
    mysql = Lazy(MySqlHandler)
    mongo = Lazy(MongoDBHandler)
    postgres = Lazy(PostgresHandler)

    print(mysql.greeting())
    print(mongo.greeting())
    print(postgres.greeting())
