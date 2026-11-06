from flask import Blueprint,make_response,request
from app.models import Activity
from app.db import db

activity_bp=Blueprint("activity",__name__)

@activity_bp.route('/',methods=["GET"])
def activities():
    activities=[activity.to_dict(rules=("-signups",)) for activity in Activity.query.all()]

    return make_response(
        activities,
        200
    )

@activity_bp.route('/<int:id>',methods=["GET"])
def activity_by_id(id):

    activity=Activity.query.filter_by(id=id).first()

    if activity is None:

        return {"error": "Activity not found"},404
    
    if request.method == "GET":

        response=activity.to_dict(rules=("-signups",))

        return make_response(
            response,
            200
        )