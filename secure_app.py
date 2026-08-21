from flask import Flask, request
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Read secret from environment variable instead of hardcoding it
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "development-only-key")


def get_user(username):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    # Parameterized query prevents SQL injection
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))

    result = cursor.fetchone()
    connection.close()

    return result


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = get_user(username)

        if user and check_password_hash(user[2], password):
            return "Login successful"

        return "Invalid username or password"

    return """
    <form method="POST">
        Username: <input name="username"><br>
        Password: <input name="password" type="password"><br>
        <input type="submit" value="Login">
    </form>
    """


if __name__ == "__main__":
    # Debug mode disabled
    app.run(debug=False)