from t08_flask_mysql.app.my_project.auth.dao import user_details_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class UserDetailsService(GeneralService):
    """
    Realization of UserDetails service.
    """
    _dao = user_details_dao