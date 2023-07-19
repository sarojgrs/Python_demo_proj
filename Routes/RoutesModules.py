from starlette.routing import Route
from Controller.User import UserController
from Controller.Abc import Abc

user_routes = [
    # Route('/', endpoint=UserController.get, methods=['GET']),
    Route('/list_users', UserController.list_users, methods=['GET']),
    Route('/getname/{username:int}',
          endpoint=UserController.getname, methods=['GET'])
    # Route('/', UserController.create_user, methods=['POST']),
    # Route('/{user_id:int}', UserController.get_user, methods=['GET']),
    # Route('/{user_id:int}', UserController.update_user, methods=['PUT']),
    # Route('/{user_id:int}', UserController.delete_user, methods=['DELETE']),
]

abc_routes = [
    Route('/abc', endpoint=Abc, methods=['GET']),
    Route('/abcd', endpoint=Abc.getName, methods=['GET']),
]
