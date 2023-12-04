from typing import Dict, Any
from t08_flask_mysql.app.my_project import db

class UserDetails(db.Model):
    __tablename__ = "user_details"

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, primary_key=True)
    first_name = db.Column(db.String(45), nullable=True, default=None)
    last_name = db.Column(db.String(45), nullable=True, default=None)
    date_of_birth = db.Column(db.Date, nullable=True, default=None)
    gender = db.Column(db.String(45), nullable=True, default=None)

    def __repr__(self) -> str:
        return f"UserDetails(user_id={self.user_id}, first_name='{self.first_name}', last_name='{self.last_name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_of_birth': self.date_of_birth,
            'gender': self.gender
        }

    @staticmethod
    def create_from_dto(details_dict: Dict[str, Any]):
        return UserDetails(**details_dict)
