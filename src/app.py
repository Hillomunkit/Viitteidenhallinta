from flask import redirect, render_template, request, jsonify, flash, session
from db_helper import reset_db
from repositories.reference_repository import get_references, create_book_reference, create_article_reference, create_inproceedings_reference, delete_book_reference, delete_article_reference, delete_inproceedings_reference
from config import app, test_env
from util import validate_reference

@app.route("/")
def index():
    references = get_references()
    return render_template("index.html", references=references)

# Saves the chosen reference type into a session object
@app.route("/choose_reference", methods=["POST"])
def choose():
    reference_type = request.form.get("reference_type")
    session["reference_type"] = reference_type
    return redirect("/new_reference")

@app.route("/new_reference")
def new():
    # If reference type hasn't been chosen, sets it as "book" by default
    if session.get("reference_type") is None:
        session["reference_type"] = "book"

    return render_template("new_reference.html", reference_type=session["reference_type"])

@app.route("/create_reference", methods=["POST"])
def reference_creation():
    reference_type = request.form.get("reference_type")

    if reference_type == "book":
        title = request.form.get("title")
        author = request.form.get("author")
        year = request.form.get("year")

        try:
            validate_reference(title, author, year)
            create_book_reference(title, author, year)
            return redirect("/")
        except Exception as error:
            flash(str(error))
            return  redirect("/new_reference")
        
    elif reference_type == "article":
        title = request.form.get("title")
        author = request.form.get("author")
        journal = request.form.get("journal")
        year = request.form.get("year")
        volume = request.form.get("volume")
        pages = request.form.get("pages")

        try:
            # TODO: validate article reference
            # validate_reference(title, author, year)
            create_article_reference(title, author, year, journal, volume, pages)
            return redirect("/")
        except Exception as error:
            flash(str(error))
            return  redirect("/new_reference")

    elif reference_type == "inproceedings":
        title = request.form.get("title")
        author = request.form.get("author")
        year = request.form.get("year")
        booktitle = request.form.get("booktitle")

        try:
            # TODO: validate inproceedings referece
            #validate_reference(title, author, year)
            create_inproceedings_reference(title, author, year, booktitle)
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
    reference_type = request.form.get("reference_type")

    if reference_type == "book":
        delete_book_reference(reference_id)
    elif reference_type == "article":
        delete_article_reference(reference_id)
    elif reference_type == "inproceedings":
        delete_inproceedings_reference(reference_id)

    return redirect("/")


