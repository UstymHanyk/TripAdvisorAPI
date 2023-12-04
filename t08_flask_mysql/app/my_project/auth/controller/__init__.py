from .orders.media_controller import MediaController
from .orders.owners_controller import OwnersController
from .orders.places_controller import PlacesController
from .orders.place_owners_controller import PlaceOwnersController
from .orders.place_amenities_controller import PlaceAmenitiesController
from .orders.amenities_controller import AmenitiesController
from .orders.ratings_controller import RatingsController
from .orders.reviews_controller import ReviewsController
from .orders.users_controller import UsersController
from .orders.payment_options_controller import PaymentOptionsController

media_controller = MediaController()
owners_controller = OwnersController()
places_controller = PlacesController()
place_owners_controller = PlaceOwnersController()
place_amenity_controller = PlaceAmenitiesController()
amenities_controller = AmenitiesController()
ratings_controller = RatingsController()
reviews_controller = ReviewsController()
users_controller = UsersController()
payment_options_controller = PaymentOptionsController()
