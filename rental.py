from movie import Movie
from movie import *
import logging

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
	
	def __init__(self, movie:Movie, days_rented):
		"""Initialize a new movie rental object for
		   a movie with known rental period (daysRented).
		"""
		self.movie = movie
		self.days_rented = days_rented

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
		return self.movie.get_price_code().price(self.days_rented)

	def get_points(self):
		return self.movie.get_price_code().renter_point(self.days_rented)
		# if self.get_movie().get_price_code() == Movie.NEW_RELEASE:
		# 	return self.get_days_rented()
		# else:
		# 	return 1
