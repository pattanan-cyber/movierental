# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie, MovieCatalog
from rental import Rental
from customer import Customer

def make_movies():
    movies = [
        "Mulan",
        "Spotlight",
        "The Great Wall",
        "The Martian",
        "Weathering With You"
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    catalog = MovieCatalog()
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        movie = catalog.get_movie(movie)
        customer.add_rental(Rental(movie, days))
        days += 1
    print(customer.statement())
