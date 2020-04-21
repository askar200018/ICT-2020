from flask import Blueprint, Response, request
from database.models import Task
import json

status = Blueprint('status', __name__)

@status.route('/api/tasks/<id>/status', methods=['GET'])
def get_status_tasks(id):
    tasks = Task.objects(user_id=id).count()
    done = Task.objects(user_id=id,status=True).count()
    undone = Task.objects(user_id=id,status=False).count()
    data = {
        "tasks": tasks,
        "done":done,
        "undone": undone
    }
    res = json.dumps(data)
    return Response(res, mimetype="application/json", status=200)
