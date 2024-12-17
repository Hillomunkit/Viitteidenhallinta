from sqlalchemy import text
from config import db, app

table_names = ["books", "articles", "inproceedings"]

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
    for table_name in table_names:
        print(f"Clearing contents from table {table_name}")
        sql = text(f"DELETE FROM {table_name}")
        db.session.execute(sql)
        db.session.commit()

def setup_db():
    for table_name in table_names:
        if table_exists(table_name):
            print(f"Table {table_name} exists, dropping")
            sql = text(f"DROP TABLE {table_name}")
            db.session.execute(sql)
            db.session.commit()

        if table_name == "books":
            print(f"Creating table {table_name}")
            sql = text(
                f"CREATE TABLE {table_name} ("
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
        elif table_name == "articles":
            print(f"Creating table {table_name}")
            sql = text(
                f"CREATE TABLE {table_name} ("
                "  id SERIAL PRIMARY KEY, "
                "  title TEXT,"
                "  author TEXT,"
                "  editor TEXT,"
                "  journal TEXT,"
                "  year TEXT,"
                "  volume TEXT,"
                "  number TEXT,"
                "  pages TEXT,"
                "  month TEXT,"
                "  note TEXT,"
                "  annote TEXT"
                ")"
            )
        elif table_name == "inproceedings":
            print(f"Creating table {table_name}")
            sql = text(
                f"CREATE TABLE {table_name} ("
                "  id SERIAL PRIMARY KEY, "
                "  title TEXT,"
                "  author TEXT,"
                "  year INTEGER,"
                "  booktitle TEXT,"
                "  editor TEXT,"
                "  volume TEXT,"
                "  number TEXT,"
                "  series TEXT,"
                "  pages TEXT,"
                "  month TEXT,"
                "  address TEXT,"
                "  organization TEXT,"
                "  publisher TEXT,"
                "  note TEXT,"
                "  annote TEXT"
                ")"
            )

        db.session.execute(sql)
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        setup_db()
