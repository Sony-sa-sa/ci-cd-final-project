"""
Routes for the Flask application
"""
from flask import jsonify
from service import app


@app.route("/")
def index():
    """Root URL response"""
    return jsonify(
        status="OK",
        message="Welcome to the CI/CD Final Project API"
    ), 200


@app.route("/health")
def health():
    """Health check endpoint"""
    return jsonify(status="OK"), 200
