from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from algorithms import fcfs, sjf, priority_scheduling, round_robin

app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app, resources={r"/*": {"origins": "*"}})  # Enable CORS for all routes

@app.route('/')
def serve_ui():
    return send_from_directory('.', 'index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data received"}), 400
        
        processes = data.get('processes', [])
        algorithm = data.get('algorithm')
        quantum = data.get('quantum', 0)

        if not processes:
            return jsonify({"error": "No processes provided"}), 400
        if not algorithm:
            return jsonify({"error": "No algorithm selected"}), 400
        if algorithm == 'RR' and quantum <= 0:
            return jsonify({"error": "Invalid quantum for Round Robin"}), 400

        proc_copy = [p.copy() for p in processes]

        if algorithm == 'FCFS':
            result = fcfs(proc_copy)
        elif algorithm == 'SJF':
            result = sjf(proc_copy)
        elif algorithm == 'Priority':
            result = priority_scheduling(proc_copy)
        elif algorithm == 'RR':
            result = round_robin(proc_copy, quantum)
        else:
            return jsonify({"error": "Invalid algorithm"}), 400

        return jsonify({
            "success": True,
            "algorithm": algorithm,
            "results": result
        })

    except Exception as e:
        print(f"Server error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)