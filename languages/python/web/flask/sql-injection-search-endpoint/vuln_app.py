from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT, password TEXT)")
    cursor.execute("DELETE FROM users")
    cursor.executemany(
        "INSERT INTO users (email, password) VALUES (?, ?)",
        [
            ("admin@example.com", "admin123"),
            ("user@example.com", "user123"),
            ("test@example.com", "test123"),
        ],
    )
    conn.commit()
    conn.close()

@app.route("/search")
def search_user():
    email = request.args.get("email", "")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # VULNERABLE: user input is directly concatenated into SQL query (SQL Injection)
    query = f"SELECT id, email FROM users WHERE email = '{email}'"
    print(f"[DEBUG] Executing query: {query}")

    try:
        cursor.execute(query)
        rows = cursor.fetchall()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

    return jsonify({"results": rows})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)