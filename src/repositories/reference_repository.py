from config import db
from sqlalchemy import text

from entities.reference import Reference

def get_references():
    sql = """
    SELECT 
        title,
        author,
        year
    FROM 
        books
    """
    result = db.session.execute(text(sql))
    references = result.fetchall()
    return [Reference(reference[0], reference[1], reference[2]) for reference in references]

def create_reference(title, author, year):
    sql = """
    INSERT INTO 
        books (title, author, year)
    VALUES 
        (:title, :author, :year)
    """
    db.session.execute(text(sql), { "title": title, "author": author, "year": year })
    db.session.commit()

def delete_reference(title, author, year):
    sql = """
    DELETE FROM
        books
    WHERE
        title = :title
    AND 
        author = :author
    AND
        year = :year
    """

    db.session.execute(text(sql), {"title": title, "author": author, "year": year})
    db.session.commit()
