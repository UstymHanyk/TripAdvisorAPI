from http import HTTPStatus
from flask import Blueprint, Response, make_response, jsonify, request
from t08_flask_mysql.app.my_project.auth.controller import place_owners_controller

place_owners_bp = Blueprint('place_owners', __name__, url_prefix='/place-owners')

@place_owners_bp.get('')
def get_all() -> Response:
    place_owners = place_owners_controller.find_all()
    return make_response(jsonify(place_owners), HTTPStatus.OK)

@place_owners_bp.get('/<int:place_id>/owners')
def get_owners_for_place(place_id: int) -> Response:
    owners = place_owners_controller.get_owners_for_place(place_id)
    return make_response(jsonify(owners), HTTPStatus.OK)

@place_owners_bp.get('/<int:owner_id>/places')
def get_places_for_owner(owner_id: int) -> Response:
    places = place_owners_controller.get_places_for_owner(owner_id)
    return make_response(jsonify(places), HTTPStatus.OK)

@place_owners_bp.post('/<int:place_id>/owners/<int:owner_id>')
def add_owner_to_place(place_id: int, owner_id: int) -> Response:
    place_owners_controller.add_owner_to_place(place_id, owner_id)
    return make_response("Owner added to Place", HTTPStatus.OK)

@place_owners_bp.delete('/<int:place_id>/owners/<int:owner_id>')
def remove_owner_from_place(place_id: int, owner_id: int) -> Response:
    place_owners_controller.remove_owner_from_place(place_id, owner_id)
    return make_response("Owner removed from Place", HTTPStatus.OK)
