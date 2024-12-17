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
        booktitle,
        editor,
        volume,
        number,
        series,
        pages,
        month,
        address,
        organization,
        publisher,
        note,
        annote
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

def create_inproceedings_reference(
        title, author, year=None, booktitle=None,
        editor=None, volume=None, number=None,
        series=None, pages=None, month=None,
        address=None, organization=None, publisher=None,
        note=None, annote=None
        ):
    sql = """
    INSERT INTO 
        inproceedings (
        title, author, year, booktitle, editor, volume, number, series,
        pages, month, address, organization, publisher, note, annote
        )
    VALUES 
        (
        :title, :author, :year, :booktitle, :editor, :volume, :number, :series,
        :pages, :month, :address, :organization, :publisher, :note, :annote
        )
    """
    db.session.execute(
        text(sql),
        {
            "title": title,
            "author": author,
            "year": year,
            "booktitle": booktitle,
            "editor": editor,
            "volume": volume,
            "number": number,
            "series": series,
            "pages": pages,
            "month": month,
            "address": address,
            "organization": organization,
            "publisher": publisher,
            "note": note,
            "annote": annote
        }
    )
    db.session.commit()

def delete_reference(table_name, reference_id):
    sql = f"""
    DELETE FROM
        {table_name}
    WHERE
        id = :reference_id
    """
    db.session.execute(text(sql), {"reference_id": reference_id})
    db.session.commit()

def update_book_reference(reference):
    sql = """
    UPDATE
        books
    SET title = :title,
        author = :author,
        publisher = :publisher,
        year = :year,
        volume = :volume,
        number = :number,
        series = :series,
        address = :address,
        edition = :edition,
        month = :month,
        note = :note,
        annote = :annote
    WHERE
        id = :reference_id
    """
    db.session.execute(
    text(sql),
        {
        "title": reference["title"],
        "author": reference["author"],
        "publisher": reference["publisher"],
        "year": reference["year"],
        "volume": reference["volume"],
        "number": reference["number"],
        "series": reference["series"],
        "address": reference["address"],
        "edition": reference["edition"],
        "month": reference["month"],
        "note": reference["note"],
        "annote": reference["annote"],
        "reference_id": reference["reference_id"]
    }
    )
    db.session.commit()

def update_article_reference(reference):
    print(reference)
    sql = """
    UPDATE
        articles
    SET title = :title,
        author = :author,
        year = :year,
        journal = :journal,
        volume = :volume,
        number = :number,
        pages = :pages,
        month = :month,
        note = :note,
        annote = :annote
    WHERE
        id = :reference_id
    """
    db.session.execute(
    text(sql),
        {
        "title": reference["title"],
        "author": reference["author"],
        "year": reference["year"],
        "journal": reference["journal"],
        "volume": reference["volume"],
        "number": reference["number"],
        "pages": reference["pages"],
        "month": reference["month"],
        "note": reference["note"],
        "annote": reference["annote"],
        "reference_id": reference["reference_id"]
    }
    )
    db.session.commit()

def update_inproceedings_reference(reference):
    print(reference)
    sql = """
    UPDATE
        inproceedings
    SET title = :title,
        author = :author,
        year = :year,
        booktitle = :booktitle,
        editor = :editor,
        volume = :volume,
        number = :number,
        series = :series,
        pages = :pages,
        month = :month,
        address = :address,
        organization = :organization,
        publisher = :publisher,
        note = :note,
        annote = :annote
    WHERE
        id = :reference_id
    """
    db.session.execute(
    text(sql),
        {
        "title": reference["title"],
        "author": reference["author"],
        "year": reference["year"],
        "booktitle": reference["booktitle"],
        "editor": reference["editor"],
        "volume": reference["volume"],
        "number": reference["number"],
        "series": reference["series"],
        "pages": reference["pages"],
        "month": reference["month"],
        "address": reference["address"],
        "organization": reference["organization"],
        "publisher": reference["publisher"],
        "note": reference["note"],
        "annote": reference["annote"],
        "reference_id": reference["reference_id"]
    }
    )
    db.session.commit()
