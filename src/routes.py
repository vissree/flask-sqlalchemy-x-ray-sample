from flask import request, make_response, abort
from flask import current_app as app
from .models import db, Uid
from os import urandom
from base64 import b64encode
from aws_xray_sdk.core import xray_recorder


@app.route("/<id>", methods=["GET", "POST"])
def read_write_db(id):
    if request.method == "POST":
        return write_to_db(id)
    else:
        return read_from_db(id)


def write_to_db(id):
    _uid = Uid.query.filter_by(id=id).first()
    if _uid:
        return make_response(f"Duplicate {id}")

    new_uid = Uid(
        id=id,
        data=generate_random_string(),
    )

    db.session.add(new_uid)
    db.session.commit()

    return make_response(f"{id} successfully added")


def read_from_db(id):
    _uid = Uid.query.filter_by(id=id).first()
    if not _uid:
        abort(404, description=f"{id} not found")

    return {"id": _uid.id, "data": _uid.data}


@xray_recorder.capture("generate_random_string")
def generate_random_string():
    return b64encode(urandom(16)).decode()
