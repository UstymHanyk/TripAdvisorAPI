from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import users_controller
from t08_flask_mysql.app.my_project.auth.domain import User

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.get('')
def get_all_users() -> Response:
    users = users_controller.find_all()
    return make_response(jsonify(users), HTTPStatus.OK)

@users_bp.post('')
def create_user() -> Response:
    content = request.get_json()
    user = User.create_from_dto(content)
    users_controller.create(user)
    return make_response(jsonify(user.put_into_dto()), HTTPStatus.CREATED)

@users_bp.get('/<int:user_id>')
def get_user(user_id: int) -> Response:
    user = users_controller.find_by_id(user_id)
    if user:
        return make_response(jsonify(user), HTTPStatus.OK)
    return make_response(jsonify({"error": "User not found"}), HTTPStatus.NOT_FOUND)

@users_bp.put('/<int:user_id>')
def update_user(user_id: int) -> Response:
    content = request.get_json()
    user = User.create_from_dto(content)
    users_controller.update(user_id, user)
    return make_response("User updated", HTTPStatus.OK)

@users_bp.patch('/<int:user_id>')
def patch_user(user_id: int) -> Response:
    content = request.get_json()
    users_controller.patch(user_id, content)
    return make_response("User updated", HTTPStatus.OK)

@users_bp.delete('/<int:user_id>')
def delete_user(user_id: int) -> Response:
    users_controller.delete(user_id)
    return make_response("User deleted", HTTPStatus.OK)
