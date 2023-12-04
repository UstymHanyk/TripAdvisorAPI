from typing import Dict, Any
from t08_flask_mysql.app.my_project import db


class PlaceOwner(db.Model):
    __tablename__ = "place_owners"

    place_id = db.Column(db.Integer, db.ForeignKey('places.id'), primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'), primary_key=True)
    place_name = db.Column(db.String(200))
    owner_email = db.Column(db.String(200))

    def __repr__(self) -> str:
        return f"PlaceOwner(place_id={self.place_id}, owner_id={self.owner_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'place_id': self.place_id,
            'owner_id': self.owner_id
        }

    @staticmethod
    def create_from_dto(place_owner_dict: Dict[str, Any]):
        return PlaceOwner(
            place_id=place_owner_dict['place_id'],
            owner_id=place_owner_dict['owner_id']
        )
