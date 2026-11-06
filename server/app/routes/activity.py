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

