from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Rating
from typing import List

class RatingDAO(GeneralDAO):
    """
    Realization of Rating data access layer for TripAdvisor's ratings.
    """
    _domain_type = Rating

    def insert_10_new_media(self):
        try:
            result = self._session.execute(text("SELECT getAverageReviewRating();"))
            average_rating = result.scalar()  # Use scalar() to get a single value from the query
            return average_rating
        except Exception as e:
            self._session.rollback()
            return f"Error: {str(e)}"