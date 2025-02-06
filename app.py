from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health-monitor', methods=['GET'])
def health_monitor():
    return jsonify({"info": "Everything looks good"})

if __name__ == '__main__':
    app.run(debug=True)
