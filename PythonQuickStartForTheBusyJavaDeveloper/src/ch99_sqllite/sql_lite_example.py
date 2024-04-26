import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS author (
    author_id INTEGER NOT NULL PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR
);''')

conn.execute('''CREATE TABLE IF NOT EXISTS  book (
    book_id INTEGER NOT NULL PRIMARY KEY,
    author_id INTEGER REFERENCES author,
    title VARCHAR
);''')

conn.execute('''CREATE TABLE IF NOT EXISTS publisher (
    publisher_id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR
);''')

conn.execute("INSERT INTO author (first_name, last_name) VALUES ('Paul', 'Panther');")
conn.execute("INSERT INTO author (first_name, last_name) VALUES ('Michael', 'Inden');")
conn.execute("INSERT INTO author (first_name, last_name) VALUES ('Tom', 'Jerry');")

print("Tables created successfully")

cur = conn.cursor()
cur.execute("SELECT * FROM author")
records = cur.fetchall()
print("Total rows are:  ", len(records))
print("Printing each row")
for row in records:
    print("Id: ", row[0])
    print("Name: ", row[1])
    print("Lastname: ", row[2])
    print("")

# Achtung: WEIL ES SQL IST, KANN MAN KEINE TAUSENDER _ NUTZEN, WIE 50_000
cur.execute("CREATE TABLE IF NOT EXISTS cars(id INT, name TEXT, price INT)")
cur.execute("INSERT INTO cars VALUES(1,'Audi', 55000)")
cur.execute("INSERT INTO cars VALUES(2,'Mercedes', 60000)")
cur.execute("INSERT INTO cars VALUES(3,'Skoda', 9000)")
cur.execute("INSERT INTO cars VALUES(4,'Volvo', 30000)")

# NICER

# HIER SCHON!
cars2 = (
    (1, 'Audi', 55_000),
    (2, 'Mercedes', 60_000),
    (3, 'Skoda', 9_000),
    (4, 'Volvo', 30_000),
    (5, 'Bentley', 350_000),
    (6, 'Hummer', 77_000),
    (7, 'Volkswagen', 22_000)
)
cur.executemany("INSERT INTO cars VALUES(?, ?, ?)", cars2)

cur.execute("SELECT * FROM cars")
records = cur.fetchall()
print("Total rows are:  ", len(records))
print("Printing each row")
for row in records:
    print("Id: ", row[0])
    print("Name: ", row[1])
    print("Price: ", row[2])
    print("")

# Save (commit) the changes
conn.commit()

conn.close()
