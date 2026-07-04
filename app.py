"""
AtapDigital AI Toolkit - Flask Backend
Web interface untuk AI Prompt Library
"""

import os
import sys
from pathlib import Path
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from SCRIPTS.prompt_runner import run_prompt

app = Flask(__name__, static_folder='.')
CORS(app)

# Serve static HTML
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

# API endpoint for generating content
@app.route('/api/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        prompt_file = data.get('prompt_file')
        context = data.get('context', {})

        if not prompt_file:
            return jsonify({'error': 'prompt_file is required'}), 400

        result = run_prompt(
            prompt_file=prompt_file,
            context=context,
            max_tokens=4096
        )

        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("=" * 50)
    print("AI-Powered Social Media Toolkit")
    print("=" * 50)
    print("Starting server...")
    print("Open browser: http://localhost:5000")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)
