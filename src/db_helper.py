from sqlalchemy import text
from config import db, app

table_name_books = "books"
table_name_articles = "articles"
table_name_inproceedings = "inproceedings"

def table_exists(name):
    sql_table_existence = text(
        "SELECT EXISTS ("
        "  SELECT 1"
        "  FROM information_schema.tables"
        f" WHERE table_name = '{name}'"
        ")"
    )

    print(f"Checking if table {name} exists")
    print(sql_table_existence)

    result = db.session.execute(sql_table_existence)
    return result.fetchall()[0][0]

def reset_db():
    print(f"Clearing contents from table {table_name_books}")
    sql = text(f"DELETE FROM {table_name_books}")
    db.session.execute(sql)
    db.session.commit()

    print(f"Clearing contents from table {table_name_articles}")
    sql = text(f"DELETE FROM {table_name_articles}")
    db.session.execute(sql)
    db.session.commit()

    print(f"Clearing contents from table {table_name_inproceedings}")
    sql = text(f"DELETE FROM {table_name_inproceedings}")
    db.session.execute(sql)
    db.session.commit()

def setup_db():
    if table_exists(table_name_books):
        print(f"Table {table_name_books} exists, dropping")
        sql = text(f"DROP TABLE {table_name_books}")
        db.session.execute(sql)
        db.session.commit()

    print(f"Creating table {table_name_books}")
    sql = text(
        f"CREATE TABLE {table_name_books} ("
        "  id SERIAL PRIMARY KEY, "
        "  title TEXT,"
        "  author TEXT,"
        "  publisher TEXT,"
        "  year INTEGER,"
        "  volume TEXT,"
        "  number TEXT,"
        "  series TEXT,"
        "  address TEXT,"
        "  edition TEXT,"
        "  month TEXT,"
        "  note TEXT,"
        "  annote TEXT"
        ")"
    )

    db.session.execute(sql)
    db.session.commit()

    if table_exists(table_name_articles):
        print(f"Table {table_name_articles} exists, dropping")
        sql = text(f"DROP TABLE {table_name_articles}")
        db.session.execute(sql)
        db.session.commit()

    print(f"Creating table {table_name_articles}")
    sql = text(
        f"CREATE TABLE {table_name_articles} ("
        "  id SERIAL PRIMARY KEY, "
        "  title TEXT,"
        "  author TEXT,"
        "  year INTEGER,"
        "  journal TEXT,"
        "  volume INTEGER,"
        "  pages TEXT"
        ")"
    )

    db.session.execute(sql)
    db.session.commit()

    if table_exists(table_name_inproceedings):
        print(f"Table {table_name_inproceedings} exists, dropping")
        sql = text(f"DROP TABLE {table_name_inproceedings}")
        db.session.execute(sql)
        db.session.commit()

    print(f"Creating table {table_name_inproceedings}")
    sql = text(
        f"CREATE TABLE {table_name_inproceedings} ("
        "  id SERIAL PRIMARY KEY, "
        "  title TEXT,"
        "  author TEXT,"
        "  year INTEGER,"
        "  booktitle TEXT"
        ")"
    )

    db.session.execute(sql)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        setup_db()
