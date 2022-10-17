import sqlite3


def add(account, title, author, date, category, link):
    """Add all the information of the newspaper"""
    con = sqlite3.connect('newspapers_management.db')
    cur = con.cursor()
    cur.execute(f"""
CREATE TABLE IF NOT EXISTS newspaperFor_{account}(id INTEGER PRIMARY KEY,
                                    title TEXT,
                                    author TEXT,
                                    date TEXT,
                                    category TEXT,
                                    link TEXT)""")
    cur.execute(f"""
INSERT INTO newspaperFor_{account}(title, author, date, category, link)
VALUES (?, ?, ?, ?, ?);""", (str(title), str(author), str(date), str(category), str(link)))
    con.commit()
    con.close()


def display(account):
    """Display all the data of the user"""
    con = sqlite3.connect('newspapers_management.db')
    cur = con.cursor()
    cur.execute(f"""
SELECT * FROM newspaperFor_{account}""")
    data = cur.fetchall()
    con.commit()
    con.close()
    return data


def update(account, id, title, author, date, category, link):
    """To update information in database

    Args:
        account: account of the users
        id: id of a newspaper
        title: title of a newspaper
        author: author of a newspaper
        date: date the author write for a newspaper
        category: category of a newspaper
        link: link of a newspaper
    """
    con = sqlite3.connect('newspapers_management.db')
    cur = con.cursor()
    cur.execute(f"""
UPDATE newspaperFor_{account}
SET title = ?,
    author = ?,
    date = ?,
    category = ?,
    link = ?
WHERE id = {id};""", (title, author, date, category, link))
    con.commit()
    con.close()


def delete(account, id):
    """Delete one date based on the id of newspapers you chose"""
    con = sqlite3.connect('newspapers_management.db')
    cur = con.cursor()
    cur.execute(f"DELETE FROM newspaperFor_{account} WHERE id = {id}")
    con.commit()
    con.close()


def delete_all(account):
    """Delete all the data in the database"""
    con = sqlite3.connect('newspapers_management.db')
    cur = con.cursor()
    cur.execute(f"DROP TABLE IF EXISTS newspaperFor_{account}")
    cur.execute(f"""
CREATE TABLE IF NOT EXISTS newspaperFor_{account}(id INTEGER PRIMARY KEY,
                                    title TEXT,
                                    author TEXT,
                                    date TEXT,
                                    category TEXT,
                                    link TEXT)""")
    con.commit()
    con.close()


def search(account, type_of_search, search):
    """To search the content you want to find in the database

    Args:
        account (_type_): account of the user
        type_of_search (_type_): choose the attribute you want to search
        search (_type_): search the content of that attribute

    Returns:
        data: return the data you want to search
    """
    con = sqlite3.connect('newspapers_management.db')
    cur = con.cursor()
    search_command = f"SELECT * FROM newspaperFor_{account} WHERE {type_of_search} LIKE '%{search}%'"
    cur.execute(search_command)
    data = cur.fetchall()
    con.commit()
    con.close()
    return data
