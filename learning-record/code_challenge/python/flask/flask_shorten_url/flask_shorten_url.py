from flask import Flask, request, jsonify, redirect
import string
import random

app = Flask(__name__)

# Store the shortened URLs in memory
url_mapping = {}

# Base URL for shortened URLs
BASE_URL = "http://localhost:5000/"

def generate_short_code(length=6):
    """Generate a random short code."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/shorten', methods=['POST'])
def shorten_url():
    """Endpoint to shorten a URL."""
    original_url = request.json.get('url')
    
    if not original_url:
        return jsonify({"error": "No URL provided"}), 400
    
    short_code = generate_short_code()
    url_mapping[short_code] = original_url
    
    short_url = BASE_URL + short_code
    
    return jsonify({"short_url": short_url}), 201

@app.route('/<short_code>', methods=['GET'])
def redirect_url(short_code):
    """Redirect to the original URL using the short code."""
    original_url = url_mapping.get(short_code)
    
    if original_url:
        return redirect(original_url)
    else:
        return jsonify({"error": "URL not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
