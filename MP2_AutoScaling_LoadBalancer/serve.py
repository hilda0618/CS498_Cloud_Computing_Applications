from flask import Flask, request, jsonify
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_ip():
    # Get the private IP address of the instance
    try:
        private_ip = socket.gethostbyname(socket.gethostname())
    except Exception as e:
        private_ip = "Error: " + str(e)
    return private_ip

@app.route('/', methods=['POST'])
def trigger_stress():
    try:
        # Launch stress_cpu.py in a separate process (non-blocking)
        subprocess.Popen(['python3', 'stress_cpu.py'])
        return jsonify({"status": "success", "message": "Stress test initiated"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Run on all interfaces (0.0.0.0) on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
