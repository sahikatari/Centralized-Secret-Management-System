from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    DB_USERNAME = "Sahi"
    DB_PASSWORD = "MyHardcodedPass@123"

    return f"""
    <html>
        <head>
            <title>Hardcoded Secret Demo</title>
        </head>
        <body>
            <h2>Connecting to database using hardcoded credentials...</h2>
            <p><b>Username:</b> {DB_USERNAME}</p>
            <p><b>Password:</b> {DB_PASSWORD}</p>
            <p><b>Connected successfully </b></p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
