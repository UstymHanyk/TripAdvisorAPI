from sqlalchemy import text

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Review
from typing import List

class ReviewDAO(GeneralDAO):
    """
    Realization of Review data access layer for TripAdvisor's reviews.
    """
    _domain_type = Review

    def get_average_review_rating(self):
        try:
            result = self._session.execute(text("SELECT getAverageReviewRating();"))
            average_rating = result.scalar()  # Use scalar() to get a single value from the query
            return average_rating
        except Exception as e:
            self._session.rollback()
            return f"Error: {str(e)}"