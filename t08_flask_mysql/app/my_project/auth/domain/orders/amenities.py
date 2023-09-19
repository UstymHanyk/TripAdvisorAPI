from typing import Dict, Any
from t08_flask_mysql.app.my_project import db


class Amenity(db.Model):
    __tablename__ = "amenities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.TEXT, nullable=True)

    places = db.relationship('PlaceAmenity', cascade='all, delete-orphan')

    def __repr__(self) -> str:
        return f"Amenity(id={self.id}, name='{self.name}', description='{self.description}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

    @staticmethod
    def create_from_dto(place_dict: Dict[str, Any]) :
        if 'id' in place_dict:
            return Media(
                **place_dict
            )
        else:
            return Media(
                **{k: v for k, v in place_dict.items() if k != 'id'}
            )