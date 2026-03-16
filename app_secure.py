from flask import Flask
import json
import boto3
from botocore.exceptions import ClientError

app = Flask(__name__)

# Secret configuration
SECRET_NAME = "prod/db-credentials"
REGION_NAME = "eu-west-1"

def get_secret():
    client = boto3.client("secretsmanager", region_name=REGION_NAME)

    try:
        response = client.get_secret_value(SecretId=SECRET_NAME)
        secret = response["SecretString"]
        return json.loads(secret)

    except ClientError as e:
        return {"error": str(e)}

@app.route("/")
def home():

    secret = get_secret()

    if "error" in secret:
        return f"""
        <html>
        <head><title>Secrets Manager Error</title></head>
        <body>
            <h2>Failed to retrieve secret</h2>
            <p>{secret['error']}</p>
        </body>
        </html>
        """

    username = secret.get("username", "Not found")
    password = secret.get("password", "Not found")

    return f"""
    <html>
    <head>
        <title>Secure Secret Retrieval Demo</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                padding: 40px;
            }}

            .card {{
                max-width: 650px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }}

            h2 {{
                color: green;
            }}

            p {{
                font-size: 18px;
            }}
        </style>
    </head>

    <body>

        <div class="card">

            <h2>Connecting using secret fetched from AWS Secrets Manager...</h2>

            <p><b>Username:</b> {username}</p>

            <p><b>Password:</b> ********</p>

            <p><b>Connected successfully</b></p>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
