from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Review
from typing import List

class ReviewDAO(GeneralDAO):
    """
    Realization of Review data access layer for TripAdvisor's reviews.
    """
    _domain_type = Review

    def find_by_place_id(self, place_id: int) -> List[object]:
        """
        Gets reviews objects from the database table by place_id.
        :param place_id: place_id value
        :return: search objects
        """
        return self._session.query(Review).filter(Review.place_id == place_id).all()

    def find_by_user_id(self, user_id: int) -> List[object]:
        """
        Gets reviews objects from the database table by user_id.
        :param user_id: user_id value
        :return: search objects
        """
        return self._session.query(Review).filter(Review.user_id == user_id).all()

    def find_by_rating(self, rating: float) -> List[object]:
        """
        Gets reviews objects from the database table by rating.
        :param rating: rating value
        :return: search objects
        """
        return self._session.query(Review).filter(Review.rating == rating).all()

