import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello All FOR CICD"

if __name__ == "__main__":
    # Cloud Run requires listening on 0.0.0.0 and the PORT env var
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
