'''
OOP in Python
Simple Example of Inheritance
'''


class Movie:
    def __init__(self, name, director, rating):
        self.name = name
        self.director = director
        self.rating = rating

    def print_info(self):
        print(f'<<{self.name}>> by {self.director}')
        print(f'Rating of <<{self.name}>> is {self.average_rating()}')

    def average_rating(self):
        return sum(self.rating) / len(self.rating)


class WebSeries(Movie):
    def __init__(self, name, director, rating, episodes):
        super().__init__(name, director, rating)
        self.episodes = episodes

    def getepisodes(self):
        return self.episodes


u_movie = Movie('BORAT', 'Someone Unknown', [4, 4, 4])
u_movie.print_info()

web_series = WebSeries('Suits', 'Gosling', [5, 4, 3], 12)
print(f'Series {web_series.name} has {web_series.average_rating()} avg rating and {web_series.getepisodes()} episodes.')
