from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import places_controller
from t08_flask_mysql.app.my_project.auth.domain import Place

places_bp = Blueprint('places', __name__, url_prefix='/places')

@places_bp.get('')
def get_all_places() -> Response:
    places = places_controller.find_all()
    return make_response(jsonify(places), HTTPStatus.OK)

@places_bp.post('')
def create_place() -> Response:
    content = request.get_json()
    place = Place.create_from_dto(content)
    places_controller.create(place)
    return make_response(jsonify(place.put_into_dto()), HTTPStatus.CREATED)

@places_bp.get('/<int:place_id>')
def get_place(place_id: int) -> Response:
    place = places_controller.find_by_id(place_id)
    if place:
        return make_response(jsonify(place), HTTPStatus.OK)
    return make_response(jsonify({"error": "Place not found"}), HTTPStatus.NOT_FOUND)

@places_bp.put('/<int:place_id>')
def update_place(place_id: int) -> Response:
    content = request.get_json()
    place = Place.create_from_dto(content)
    places_controller.update(place_id, place)
    return make_response("Place updated", HTTPStatus.OK)

@places_bp.patch('/<int:place_id>')
def patch_place(place_id: int) -> Response:
    content = request.get_json()
    places_controller.patch(place_id, content)
    return make_response("Place updated", HTTPStatus.OK)

@places_bp.delete('/<int:place_id>')
def delete_place(place_id: int) -> Response:
    places_controller.delete(place_id)
    return make_response("Place deleted", HTTPStatus.OK)
