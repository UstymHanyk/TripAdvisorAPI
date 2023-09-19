from typing import Dict, Any
from t08_flask_mysql.app.my_project import db


class PlaceAmenity(db.Model):
    __tablename__ = "place_amenities"

    place_id = db.Column(db.Integer, db.ForeignKey('places.id', ondelete='CASCADE'), primary_key=True)
    amenity_id = db.Column(db.Integer, db.ForeignKey('amenities.id', ondelete='CASCADE'), primary_key=True)


    def __repr__(self) -> str:
        return f"PlaceAmenity(place_id={self.place_id}, amenity_id={self.amenity_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'place_id': self.place_id,
            'amenity_id': self.amenity_id
        }

    @staticmethod
    def create_from_dto(place_amenity_dict: Dict[str, Any]):
        return PlaceAmenity(
            place_id=place_amenity_dict['place_id'],
            amenity_id=place_amenity_dict['amenity_id']
        )