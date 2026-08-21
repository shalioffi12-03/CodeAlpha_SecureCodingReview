from flask import Flask, request
import sqlite3

app = Flask(__name__)

SECRET_KEY = "mysecret123"

def get_user(username):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)

    result = cursor.fetchone()
    connection.close()

    return result

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = get_user(username)

        if user and password == user[2]:
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
    app.run(debug=True)