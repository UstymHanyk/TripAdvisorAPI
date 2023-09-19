from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import amenities_controller
from t08_flask_mysql.app.my_project.auth.domain import Amenity

amenity_bp = Blueprint('amenities', __name__, url_prefix='/amenities')

@amenity_bp.get('')
def get_all_amenities() -> Response:
    amenities = amenities_controller.find_all()
    return make_response(jsonify(amenities), HTTPStatus.OK)

@amenity_bp.post('')
def create_amenity() -> Response:
    content = request.get_json()
    amenity = Amenity.create_from_dto(content)
    amenities_controller.create(amenity)
    return make_response(jsonify(amenity.put_into_dto()), HTTPStatus.CREATED)

@amenity_bp.get('/<int:amenity_id>')
def get_amenity(amenity_id: int) -> Response:
    amenity = amenities_controller.find_by_id(amenity_id)
    if amenity:
        return make_response(jsonify(amenity), HTTPStatus.OK)
    return make_response(jsonify({"error": "Amenity not found"}), HTTPStatus.NOT_FOUND)

@amenity_bp.put('/<int:amenity_id>')
def update_amenity(amenity_id: int) -> Response:
    content = request.get_json()
    amenity = Amenity.create_from_dto(content)
    amenities_controller.update(amenity_id, amenity)
    return make_response("Amenity updated", HTTPStatus.OK)

@amenity_bp.patch('/<int:amenity_id>')
def patch_amenity(amenity_id: int) -> Response:
    content = request.get_json()
    amenities_controller.patch(amenity_id, content)
    return make_response("Amenity updated", HTTPStatus.OK)

@amenity_bp.delete('/<int:amenity_id>')
def delete_amenity(amenity_id: int) -> Response:
    amenities_controller.delete(amenity_id)
    return make_response("Amenity deleted", HTTPStatus.OK)
