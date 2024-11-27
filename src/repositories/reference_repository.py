from sqlalchemy import text
from config import db

from entities.reference import BookReference, ArticleReference, InproceedingsReference


def get_book_references():
    sql = """
    SELECT 
        id,
        title,
        author,
        year
    FROM 
        books
    """
    result = db.session.execute(text(sql))
    references = result.fetchall()
    return [BookReference(reference[0], reference[1],
                          reference[2], reference[3]) for reference in references]

def get_article_references():
    sql = """
    SELECT 
        id,
        title,
        author,
        year,
        journal,
        volume,
        pages
    FROM 
        articles
    """
    result = db.session.execute(text(sql))
    references = result.fetchall()
    return [ArticleReference(reference[0], reference[1], reference[2], reference[3],
                             reference[4], reference[5], reference[6]) for reference in references]

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
    references = result.fetchall()
    return [InproceedingsReference(reference[0], reference[1], reference[2],
                                   reference[3], reference[4]) for reference in references]

def get_references():
    books = get_book_references()
    articles = get_article_references()
    inproceedings = get_inproceedings_references()
    all_references = books + articles + inproceedings
    return all_references

def create_book_reference(title, author, year):
    sql = """
    INSERT INTO 
        books (title, author, year)
    VALUES 
        (:title, :author, :year)
    """
    db.session.execute(text(sql), { "title": title, "author": author, "year": year })
    db.session.commit()

def create_article_reference(title, author, year, journal, volume, pages):
    sql = """
    INSERT INTO 
        articles (title, author, year, journal, volume, pages)
    VALUES 
        (:title, :author, :year, :journal, :volume, :pages)
    """
    db.session.execute(text(sql), { "title": title, "author": author, "year": year,
                                   "journal": journal, "volume": volume, "pages": pages })
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
