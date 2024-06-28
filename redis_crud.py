from flask import Flask, request, jsonify
from rediscluster import RedisCluster

# Initialize Flask application
app = Flask(__name__)

# Configuration for Redis Cluster nodes
startup_nodes = [
    {"host": "127.0.0.1", "port": "7000"},
    {"host": "127.0.0.1", "port": "7001"},
    {"host": "127.0.0.1", "port": "7002"}
]

# Connect to Redis Cluster
rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

# CRUD operations
@app.route('/redis/set', methods=['POST'])
def redis_set():
    data = request.json
    key = data.get('key')
    value = data.get('value')
    rc.set(key, value)
    return jsonify({"message": f"Set: {key} => {value}"}), 200

@app.route('/redis/get', methods=['GET'])
def redis_get():
    key = request.args.get('key')
    value = rc.get(key)
    return jsonify({"message": f"Get: {key} => {value}"}), 200

@app.route('/redis/delete', methods=['DELETE'])
def redis_delete():
    key = request.args.get('key')
    rc.delete(key)
    return jsonify({"message": f"Deleted: {key}"}), 200

# Test endpoint
if __name__ == '__main__':
    app.run(debug=True)
