<<<<<<< HEAD
from flask import Flask, request, redirect
import requests
import base64
import os

EBAY_CLIENT_ID = os.getenv("EBAY_CLIENT_ID")
EBAY_CLIENT_SECRET = os.getenv("EBAY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("EBAY_REDIRECT_URI")

@app.route("/")
def home():
    return "eBay OAuth callback app is running."

@app.route("/callback")
def ebay_callback():
    code = request.args.get("code")
    if not code:
        return "No code received from eBay!"

    # Exchange code for tokens
    token_url = "https://api.ebay.com/identity/v1/oauth2/token"
    credentials = f"{EBAY_CLIENT_ID}:{EBAY_CLIENT_SECRET}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {encoded_credentials}"
    }

    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI
    }

    response = requests.post(token_url, headers=headers, data=data)
    if response.status_code == 200:
        tokens = response.json()
        return f"Access Token: {tokens['access_token']}<br><br>Refresh Token: {tokens['refresh_token']}"
    else:
        return f"Error getting token: {response.text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
from flask import Flask, request

app = Flask(__name__)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    state = request.args.get("state")

    return f"""
    <h2>Authorization Successful</h2>
    <p>Your authorization code is:</p>
    <pre>{code}</pre>
    <p>Copy this code and paste it into your script later to exchange for an access token.</p>
    """
>>>>>>> 56abe2bd922b92d7f28efcd1640b5408f12b87c3
