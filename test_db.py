from app.services.db import Database

def test_db_connection():
    db = Database()
    db.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT)")
    db.execute("INSERT INTO test (name) VALUES (?)", ("test_name",))
    db.execute("SELECT * FROM test")
    result = db.fetchall()
    db.close()
    assert result and result[0]["name"] == "test_name"
    print("Database test passed.")

if __name__ == "__main__":
    test_db_connection()
