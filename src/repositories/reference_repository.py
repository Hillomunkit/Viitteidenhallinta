from sqlalchemy import text
from config import db

from entities.reference import BookReference, ArticleReference, InproceedingsReference


def get_book_references():
    sql = """
    SELECT 
        id,
        title,
        author,
        publisher,
        year,
        volume, 
        number, 
        series, 
        address, 
        edition, 
        month, 
        note, 
        annote
    FROM 
        books
    """
    result = db.session.execute(text(sql))
    references = result.mappings().all()
    return [BookReference(**reference) for reference in references]

def get_article_references():
    sql = """
    SELECT 
        id,
        title,
        author,
        year,
        journal,
        volume,
        number,
        pages,
        month, 
        note,
        annote
    FROM 
        articles
    """
    result = db.session.execute(text(sql))
    references = result.mappings().all()
    return [ArticleReference(**reference) for reference in references]

def get_inproceedings_references():
    sql = """
    SELECT 
        id,
        title,
        author,
        year,
        booktitle
    FROM 
        inproceedings
    """
    result = db.session.execute(text(sql))
    references = result.mappings().all()
    return [InproceedingsReference(**reference) for reference in references]

def get_references():
    books = get_book_references()
    articles = get_article_references()
    inproceedings = get_inproceedings_references()
    all_references = books + articles + inproceedings
    return all_references

def create_book_reference(
        title, author, publisher, year, volume=None, number=None,
        series=None, address=None, edition=None, month=None, note=None, annote=None
        ):
    sql = """
    INSERT INTO 
        books (title, author, publisher, year, volume, number, series, address, edition, month, note, annote)
    VALUES 
        (:title, :author, :publisher, :year, :volume, :number, :series, :address, :edition, :month, :note, :annote)
    """
    db.session.execute(
        text(sql),
        {
            "title": title,
            "author": author,
            "publisher": publisher,
            "year": year,
            "volume": volume,
            "number": number,
            "series": series,
            "address": address,
            "edition": edition,
            "month": month,
            "note": note,
            "annote": annote
        }
    )
    db.session.commit()

def create_article_reference(
        title, author, year, journal, volume=None, number=None,
        pages=None, month=None, note=None, annote=None
        ):
    sql = """
    INSERT INTO 
        articles (title, author, year, journal, volume, number, pages, month, note, annote)
    VALUES 
        (:title, :author, :year, :journal, :volume, :number, :pages, :month, :note, :annote)
    """
    db.session.execute(
        text(sql),
        {
            "title": title,
            "author": author,
            "year": year,
            "journal": journal,
            "volume": volume,
            "number": number,
            "pages": pages,
            "month": month,
            "note": note,
            "annote": annote
            }
        )
    db.session.commit()

def create_inproceedings_reference(title, author, year, booktitle):
    sql = """
    INSERT INTO 
        inproceedings (title, author, year, booktitle)
    VALUES 
        (:title, :author, :year, :booktitle)
    """
    db.session.execute(text(sql), { "title": title, "author": author,
                                   "year": year, "booktitle": booktitle })
    db.session.commit()

def delete_book_reference(reference_id):
    sql = """
    DELETE FROM
        books
    WHERE
        id = :reference_id
    """

    db.session.execute(text(sql), {"reference_id": reference_id})
    db.session.commit()

def delete_article_reference(reference_id):
    sql = """
    DELETE FROM
        articles
    WHERE
        id = :reference_id
    """

    db.session.execute(text(sql), {"reference_id": reference_id})
    db.session.commit()

def delete_inproceedings_reference(reference_id):
    sql = """
    DELETE FROM
        inproceedings
    WHERE
        id = :reference_id
    """

    db.session.execute(text(sql), {"reference_id": reference_id})
    db.session.commit()
