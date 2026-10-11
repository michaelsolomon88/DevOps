from flask import Flask, jsonify, render_template
import os
import socket
from datetime import datetime, timezone

app = Flask(__name__)

APP_VERSION = os.environ.get("APP_VERSION", "v1.0.0")
APP_ENV = os.environ.get("APP_ENV", "local")


@app.route("/")
def index():
    return render_template(
        "index.html",
        version=APP_VERSION,
        environment=APP_ENV,
        hostname=socket.gethostname(),
        timestamp=datetime.now(timezone.utc).isoformat(),
        health_status="healthy",
    )


@app.route("/api/status")
def api_status():
    return jsonify({
        "message": "Hello from the DevOps CI/CD demo project!",
        "version": APP_VERSION,
        "environment": APP_ENV,
        "hostname": socket.gethostname(),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=os.environ.get("FLASK_DEBUG") == "1",
    )
