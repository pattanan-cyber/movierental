import csv


class Movie:
    """
	A movie available for rent.
	"""

    def __init__(self, title, year, genre):
        # Initialize a new movie.
        self.__title = title
        self.__year = year
        self.__genre = genre

    def get_title(self):
        return self.__title

    def __str__(self):
        return self.__title

    def is_genre(self, genre):
        return genre in self.__genre

    @property
    def genre(self):
        return self.__genre

    @property
    def year(self):
        return self.__year

class MovieCatalog:
    """movie catalog"""
    def __init__(self):
        self.movies = {}
        self.movie_generator = MovieCatalog.read_data(self.movies)

    @staticmethod
    def read_data(movies):
        file = open('movies.csv')
        csvreader = csv.reader(file)
        for row in csvreader:
            if row[0].startswith('#'):
                continue
            movies[row[1]] = Movie(row[1],int(row[2]),row[3].split('|'))
            yield movies[row[1]]
        file.close()


    def get_movie(self, title:str):
        if not title in self.movies:
            for movie in self.movie_generator:
                if title == movie.get_title():
                    return movie
        else:
            return self.movies[title]
