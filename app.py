from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

candidates = {}

@app.route('/api/candidates', methods=['GET'])
def get_all_candidates():
    return jsonify(list(candidates.values()))

@app.route('/api/candidates', methods=['POST'])
def add_candidate():
    data = request.get_json()
    candidate_id = str(uuid.uuid4())
    candidate = {
        "id": candidate_id,
        "name": data["name"],
        "email": data["email"],
        "role": data["role"],
        "status": data.get("status", "Applied")
    }
    candidates[candidate_id] = candidate
    return jsonify(candidate), 201

@app.route('/api/candidates/<candidate_id>', methods=['PUT'])
def update_candidate(candidate_id):
    if candidate_id not in candidates:
        return jsonify({"error": "Candidate not found"}), 404
    data = request.get_json()
    candidates[candidate_id].update(data)
    return jsonify(candidates[candidate_id])

@app.route('/api/candidates/<candidate_id>', methods=['DELETE'])
def delete_candidate(candidate_id):
    if candidate_id in candidates:
        del candidates[candidate_id]
        return jsonify({"message": "Deleted"})
    return jsonify({"error": "Candidate not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)




















