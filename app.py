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
