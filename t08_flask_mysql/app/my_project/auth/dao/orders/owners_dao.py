from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Owner
from typing import List
from sqlalchemy import text
class OwnerDAO(GeneralDAO):
    """
    Realization of Owner data access layer for TripAdvisor's owners.
    """
    _domain_type = Owner

    def create_10_timestampt_tables(self):

        try:
            self._session.execute(text("CALL CreateTables()"))
            self._session.commit()
            return "Created successfully"
        except Exception as e:
            self._session.rollback()
            return f"Error: {str(e)}"
