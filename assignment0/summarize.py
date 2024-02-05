def summarize_data(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('''SELECT nature, COUNT(*) as count 
                   FROM incidents 
                   GROUP BY nature 
                   ORDER BY count DESC, nature''')
    rows = cur.fetchall()
    for row in rows:
        print(f"{row[0]}|{row[1]}")
    conn.close()

# Example usage:
# summarize_data("path/to/normanpd.db")
