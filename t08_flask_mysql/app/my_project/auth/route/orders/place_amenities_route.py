from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import place_amenity_controller

place_amenity_bp = Blueprint('place_amenity', __name__, url_prefix='/place-amenities')


@place_amenity_bp.get('')
def get_all() -> Response:
    place_owners = place_amenity_controller.find_all()
    return make_response(jsonify(place_owners), HTTPStatus.OK)

@place_amenity_bp.post('/<int:place_id>/amenities/<int:amenity_id>')
def add_amenity_to_place(place_id: int, amenity_id: int) -> Response:
    success = place_amenity_controller.add_amenity_to_place(place_id, amenity_id)
    if success:
        return make_response("Amenity added to place", HTTPStatus.OK)
    return make_response("Failed to add amenity to place", HTTPStatus.INTERNAL_SERVER_ERROR)

@place_amenity_bp.delete('/<int:place_id>/amenities/<int:amenity_id>')
def remove_amenity_from_place(place_id: int, amenity_id: int) -> Response:
    success = place_amenity_controller.remove_amenity_from_place(place_id, amenity_id)
    if success:
        return make_response("Amenity removed from place", HTTPStatus.OK)
    return make_response("Failed to remove amenity from place", HTTPStatus.INTERNAL_SERVER_ERROR)

@place_amenity_bp.get('/<int:place_id>/amenities')
def get_amenities_for_place(place_id: int) -> Response:
    amenities = place_amenity_controller.get_amenities_for_place(place_id)
    return make_response(jsonify(amenities), HTTPStatus.OK)
