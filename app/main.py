from flask import Flask, jsonify, request

def create_app():
    """
    Funkce vytvoří Flask aplikaci.
    """
    app = Flask(__name__)

    # Endpoint "/" → vrátí základní zprávu
    @app.route("/")
    def index():
        return jsonify(message="Hello, world!"), 200

    # Endpoint "/echo" → vrátí JSON, který uživatel pošle
    @app.route("/echo", methods=["POST"])
    def echo():
        data = request.json or {}  # vezme JSON z POST requestu
        return jsonify(data=data), 200

    return app

# Tento blok umožní spustit aplikaci přímo z terminálu
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)

