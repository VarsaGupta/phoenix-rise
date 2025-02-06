from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health-monitor')
def health_monitor():
    return jsonify({"info": "Everything looks good"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
