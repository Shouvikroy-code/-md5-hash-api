from flask import Flask, request, jsonify
import hashlib
import requests

app = Flask(__name__)

@app.route('/hash', methods=['GET'])
def compute_hash():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'Missing URL'}), 400
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        content = response.text
        hash_val = hashlib.md5(content.encode('utf-8')).hexdigest()
        return jsonify({'md5': hash_val})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    
import os

port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port)

