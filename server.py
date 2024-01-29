import json
from flask import Flask, jsonify, request
from bchain import Blockchain

app = Flask(__name__)

blockchain = Blockchain()



@app.route("/mine_block", methods=["POST"])
def mine_block():
    if request.is_json:
        data = request.json
        response = blockchain.add(data=data)
        return jsonify(response), 200
    else:
        return "Content type is not supported."

@app.route("/get_chain", methods=["GET"])
def display_chain():
    response = {"all_transactions": blockchain.hashes, "length": len(blockchain.hashes)}
    return jsonify(response), 200

@app.route("/get_transaction_type", methods=["GET"])
def display_chain_usertype():
    return blockchain.usertype_transactions, 200

@app.route("/print_all", methods=["GET"])
def print_all():
    return jsonify(blockchain.getTransactions('all')), 200

# Run the flask server locally
app.run(host="127.0.0.1", port=5000, debug=True)