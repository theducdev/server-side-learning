from flask import Flask, request, jsonify
from scraper import scrape_dantri

app = Flask(__name__)

# Route GET
@app.route('/', methods=['GET'])
def home():
    return "Hello from Python server!"

# Route POST nhận JSON
@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    print("Received data:", data)
    return jsonify({"status": "success", "received": data})

# Route test query param
@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return f"Hello, {name}!"

# Route scrape Dân trí
@app.route('/api/scrape-dantri', methods=['GET'])
def api_scrape_dantri():
    data = scrape_dantri()
    if data:
        return jsonify({"status": "success", "data": data})
    else:
        return jsonify({"status": "error", "message": "Không thể cào dữ liệu"}), 500

# Khởi động server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
