from .orders.users_dao import UserDAO
from .orders.user_details_dao import UserDetailsDAO
from .orders.places_dao import PlaceDAO
from .orders.owners_dao import OwnerDAO
from .orders.place_owners_dao import PlaceOwnerDAO
from .orders.media_dao import MediaDAO
from .orders.place_amenities_dao import PlaceAmenityDAO
from .orders.amenities_dao import AmenityDAO
from .orders.ratings_dao import RatingDAO
from .orders.reviews_dao import ReviewDAO
from .orders.payment_options_dao import PaymentOptionsDAO

users_dao = UserDAO()
user_details_dao = UserDetailsDAO()
places_dao = PlaceDAO()
owners_dao = OwnerDAO()
place_owners_dao = PlaceOwnerDAO()
media_dao = MediaDAO()
place_amenities_dao = PlaceAmenityDAO()
amenities_dao = AmenityDAO()
ratings_dao = RatingDAO()
reviews_dao = ReviewDAO()
payment_options_dao = PaymentOptionsDAO()