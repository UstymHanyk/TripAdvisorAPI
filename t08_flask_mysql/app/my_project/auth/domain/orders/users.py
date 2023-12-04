from typing import Dict, Any
from t08_flask_mysql.app.my_project import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), unique=True, nullable=False)

    user_reviews = db.relationship('Review', backref='user')
    user_details = db.relationship('UserDetails', uselist='false', backref='user')

    def __repr__(self) -> str:
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"

    def put_into_dto(self) -> Dict[str, Any]:
        user_details = [{
            'date_of_birth': detail.date_of_birth,
            'gender': detail.gender
        } for detail in self.user_details]
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'details': user_details
        }

    @staticmethod
    def create_from_dto(place_dict: Dict[str, Any]):
        if 'id' in place_dict:
            return User(
                **place_dict
            )
        else:
            return User(
                **{k: v for k, v in place_dict.items() if k != 'id'}
            )
