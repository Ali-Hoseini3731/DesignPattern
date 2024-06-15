class Cinema:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name}---{self.address}"


class Movie:
    def __init__(self, name, ranking_imdb, time, language, subtitle=True):
        self.name = name
        self.ranking_imdb = ranking_imdb
        self.time = time
        self.language = language
        self.subtitle = subtitle

    def __str__(self):
        return f"{self.name}---{self.ranking_imdb}---{self.time}"


class Time:
    def __init__(self, start_time):
        self.start_time = start_time

    def __str__(self):
        return self.start_time


class Hall:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return f"{self.name}---{self.capacity}"


class Seat:
    def __init__(self, number):
        self.number = number
        self.status = None

    def __str__(self):
        return self.number


class Sans:
    def __init__(self, cinema, movie, time, hall):
        self.cinema = cinema
        self.movie = movie
        self.time = time
        self.hall = hall
        self.seats = list()
        self.production_seat()

    def production_seat(self):
        for i in range(self.hall.capacity):
            self.seats.append(Seat(i))


if __name__ == "__main__":
    cinema = Cinema(name="Azadi", address="Tehran-Azadi")
    movie = Movie(name="rambo", ranking_imdb=8.5, time=2.30, language="english")
    time = Time(start_time="17:00")
    hall = Hall(name=1, capacity=100)

    sans = Sans(cinema, movie, time, hall)

    print(type(sans))
    print(type(sans.seats[0]))
    print(f"number seats: {len(sans.seats)}")
    print(
        f"cinema_name: {sans.cinema.name}\nmovie_name: {sans.movie.name}\nmovie_imdb: {sans.movie.ranking_imdb}\n"
        f"movie_time: {sans.movie.time}\nstart_time: {sans.time.start_time}"
    )
