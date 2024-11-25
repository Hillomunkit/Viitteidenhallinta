from flask import redirect, render_template, request, jsonify, flash, session
from db_helper import reset_db
from repositories.reference_repository import get_references, create_reference, delete_reference
from config import app, test_env
from util import validate_reference

@app.route("/")
def index():
    references = get_references()
    return render_template("index.html", references=references)

@app.route("/choose_reference", methods=["POST"])
def choose():
    reference_type = request.form.get("reference_type")
    session["reference_type"] = reference_type
    return redirect("/new_reference")

@app.route("/new_reference")
def new():
    if session.get("reference_type") is None:
        session["reference_type"] = "book"

    return render_template("new_reference.html", reference_type=session["reference_type"])

@app.route("/create_reference", methods=["POST"])
def reference_creation():
    title = request.form.get("title")
    author = request.form.get("author")
    year = request.form.get("year")

    try:
        validate_reference(title, author, year)
        create_reference(title, author, year)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect("/new_reference")

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })



@app.route("/delete_reference", methods=["POST"])
def delete_ref():
    reference_id = request.form.get("reference_id")
    delete_reference(reference_id)

    return redirect("/")


