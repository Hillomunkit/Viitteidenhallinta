from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.reference_repository import get_references, create_reference
from config import app, test_env
from util import validate_reference

@app.route("/")
def index():
    references = get_references()
    return render_template("index.html", references=references)

@app.route("/new_reference")
def new():
    return render_template("new_reference.html")

@app.route("/create_reference", methods=["POST"])
def reference_creation():
    title = request.form.get("title")
    author = request.form.get("author")
    year = request.form.get("year")

    try:
        #Syötteiden tarkistus tulee tähän, tällä hetkellä ei tarkista syötteitä
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
