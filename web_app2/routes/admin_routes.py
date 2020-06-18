  
from flask import Blueprint, jsonify

from .models import db

admin_routes = Blueprint("admin_routes", __name__)

# TODO: think about password protecting these admin routes

@admin_routes.route("/admin/db/reset")
def reset_db():
    print(type(db))
    db.drop_all()
    db.create_all()
    return jsonify({"message": "DB RESET OK"})  
