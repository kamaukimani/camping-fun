from flask import Blueprint,make_response,request
from app.models import Signup
from app.db import db

signup_bp=Blueprint("signup",__name__)

@signup_bp.route('/',methods=["GET"])
def signups():
    if request.method == "GET":
        signups=[signup.to_dict() for signup in Signup.query.all()]

        return make_response(
            signups,
            200
        )