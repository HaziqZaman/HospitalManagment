from app.services.auth import authenticate_user
from app.services.db import Database
import hashlib

def setup_test_user():
    db = Database()
    username = "testuser"
    password = "testpass"
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)")
    db.execute("DELETE FROM users WHERE username = ?", (username,))
    db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    db.close()

def test_auth():
    setup_test_user()
    assert authenticate_user("testuser", "testpass") == True
    assert authenticate_user("testuser", "wrongpass") == False
    print("Auth tests passed.")

if __name__ == "__main__":
    test_auth()

