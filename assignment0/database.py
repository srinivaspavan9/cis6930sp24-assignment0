import sqlite3

def create_db(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS incidents (
                   date_time TEXT, 
                   incident_number TEXT, 
                   location TEXT, 
                   nature TEXT, 
                   incident_ori TEXT)''')
    conn.commit()
    conn.close()

def insert_incidents(db_path, incidents):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.executemany('''INSERT INTO incidents 
                       (date_time, incident_number, location, nature, incident_ori) 
                       VALUES (?, ?, ?, ?, ?)''', incidents)
    conn.commit()
    conn.close()

# Example usage:
# create_db("path/to/normanpd.db")
# insert_incidents("path/to/normanpd.db", incidents)

