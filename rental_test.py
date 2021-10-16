import unittest
from customer import Customer
from rental import Rental
from movie import Movie, PriceCode


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.new_movie = Movie("Mulan", PriceCode.NEW_RELEASE)
		self.regular_movie = Movie("CitizenFour", PriceCode.REGULAR)
		self.children_movie = Movie("Frozen", PriceCode.CHILDREN)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("CitizenFour", PriceCode.REGULAR)
		self.assertEqual("CitizenFour", m.get_title())
		self.assertEqual(PriceCode.REGULAR, m.get_price_code())

	def test_rental_price(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_charge(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_charge(), 15.0)

		rental = Rental(self.regular_movie, 4)
		self.assertEqual(rental.get_charge(), 5)
		rental = Rental(self.regular_movie, 10)
		self.assertEqual(rental.get_charge(), 14)
	#
	# @unittest.skip("TODO add test of frequent renter points when you add it to Rental")
	def test_rental_points(self):
		# self.fail("TODO add  test of frequent renter points")
		# rental = Rental(self.regular_movie, 5)
		# self.assertEqual(rental.get_points, 1.0)
		# rental = Rental(self.children_movie, 2)
		# self.assertEqual(rental.get_points(), 1.0)
		# rental = Rental(self.new_movie, 20)
		# self.assertEqual(rental.get_points(), 20.0)
		rental = Rental(self.new_movie, 3)
		self.assertEqual(rental.get_points(), 3.0)
