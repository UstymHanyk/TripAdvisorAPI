from .orders.media_service import MediaService
from .orders.owners_service import OwnersService
from .orders.places_service import PlacesService
from .orders.place_owners_service import PlaceOwnersService
from .orders.place_amenities_service import PlaceAmenityService
from .orders.amenities_service import AmenityService
from .orders.ratings_service import RatingsService
from .orders.reviews_service import ReviewsService
from .orders.users_service import UsersService
from .orders.user_details_service import UserDetailsService


media_service = MediaService()
owners_service = OwnersService()
places_service = PlacesService()
place_owners_service = PlaceOwnersService()
place_amenities_service = PlaceAmenityService()
amenities_service = AmenityService()
ratings_service = RatingsService()
reviews_service = ReviewsService()
users_service = UsersService()
user_details_service = UserDetailsService()
