from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import owners_controller
from t08_flask_mysql.app.my_project.auth.domain import Owner

owners_bp = Blueprint('owners', __name__, url_prefix='/owners')

@owners_bp.get('')
def get_all_owners() -> Response:
    owners = owners_controller.find_all()
    return make_response(jsonify(owners), HTTPStatus.OK)

@owners_bp.post('')
def create_owner() -> Response:
    content = request.get_json()
    owner = Owner.create_from_dto(content)
    owners_controller.create(owner)
    return make_response(jsonify(owner.put_into_dto()), HTTPStatus.CREATED)

@owners_bp.get('/<int:owner_id>')
def get_owner(owner_id: int) -> Response:
    owner = owners_controller.find_by_id(owner_id)
    if owner:
        return make_response(jsonify(owner), HTTPStatus.OK)
    return make_response(jsonify({"error": "Owner not found"}), HTTPStatus.NOT_FOUND)

@owners_bp.put('/<int:owner_id>')
def update_owner(owner_id: int) -> Response:
    content = request.get_json()
    owner = Owner.create_from_dto(content)
    owners_controller.update(owner_id, owner)
    return make_response("Owner updated", HTTPStatus.OK)

@owners_bp.patch('/<int:owner_id>')
def patch_owner(owner_id: int) -> Response:
    content = request.get_json()
    owners_controller.patch(owner_id, content)
    return make_response("Owner updated", HTTPStatus.OK)

@owners_bp.delete('/<int:owner_id>')
def delete_owner(owner_id: int) -> Response:
    owners_controller.delete(owner_id)
    return make_response("Owner deleted", HTTPStatus.OK)
@owners_bp.post('/create10')
def create_10_tables() -> Response:
    result = owners_controller.create_10_timestampt_tables()
    return make_response(jsonify({'message': result}), HTTPStatus.OK)