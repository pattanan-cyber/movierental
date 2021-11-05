from movie import Movie
from enum import Enum
import datetime


class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior"""
    NEW_RELEASE = {"price": lambda days: 3.0 * days,
                   "frp": lambda days: days
                   }
    REGULAR = {"price": lambda days: 2 if days <= 2 else 2 + 1.5 * (days - 2),
               "frp": lambda days: 1
               }
    CHILDREN = {"price": lambda days: 1.5 if days <= 3 else 1.5 + 1.5 * (days - 3),
                "frp": lambda days: 1
                }

    def price(self, days: int) -> float:
        "Return the rental price for a given number of days"""
        pricing = self.value["price"]  # the enum member's price formula
        return pricing(days)

    def renter_point(self, days: int):
        point = self.value["frp"]
        return point(days)

    @classmethod
    def for_movie(cls, movie: Movie):
        year = datetime.date.today().year
        if movie.year == year:
            return cls.NEW_RELEASE
        elif movie.is_genre('Children'):
            return cls.CHILDREN
        return cls.REGULAR

class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    But for simplicity of the example only a days_rented
    field is used.
    """

    def __init__(self, movie: Movie, days_rented):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = PriceCode.for_movie(movie)


    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    # def get_charge(self):
    # 	amount = 0
    # 	if self.get_movie().get_price_code() == Movie.REGULAR:
    # 		amount = 2.0
    # 		if self.get_days_rented() > 2:
    # 			amount += 1.5 * (self.get_days_rented() - 2)
    # 	elif self.get_movie().get_price_code() == Movie.CHILDRENS:
    # 		# Three days for $1.50, additional days 1.50 each.
    # 		amount = 1.5
    # 		if self.get_days_rented() > 3:
    # 			amount += 1.5 * (self.get_days_rented() - 3)
    # 	elif self.get_movie().get_price_code() == Movie.NEW_RELEASE:
    # 		# Straight per day charge
    # 		amount = 3 * self.get_days_rented()
    # 	else:
    # 		log = logging.getLogger()
    # 		log.error(
    # 			f"Movie {self.get_movie()} has unrecognized priceCode {self.get_movie().get_price_code()}")
    # 	return amount

    def get_charge(self):
        """compute rental change."""
        return self.price_code.price(self.days_rented)

    def get_points(self):
        return self.price_code.renter_point(self.days_rented)
    # if self.get_movie().get_price_code() == Movie.NEW_RELEASE:
    # 	return self.get_days_rented()
    # else:
    # 	return 1
