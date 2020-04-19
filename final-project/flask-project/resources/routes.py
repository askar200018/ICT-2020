from .user import UsersApi, UserApi
from .task import TasksApi, TaskApi
from .users_task import UserTasksApi

def initialize_routes(api):
    api.add_resource(UsersApi, '/api/users')
    api.add_resource(UserApi, '/api/users/<id>')
    api.add_resource(TasksApi, '/api/tasks')
    api.add_resource(TaskApi, '/api/tasks/<id>')
    api.add_resource(UserTasksApi, '/api/users/<id>/tasks')