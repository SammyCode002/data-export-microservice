from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/export', methods=['POST'])
def export_data():
    """
    Export data to JSON or plain text format.
    
    Request body:
        - data (required): The data object to export
        - format (required): Output format ("json" or "text")
    
    Returns:
        - JSON or plain text formatted data
    """
    
    # Check if request has JSON body
    if not request.is_json:
        return jsonify({
            "success": False,
            "error": "Invalid request",
            "message": "Request must be JSON"
        }), 400
    
    # Get request data
    body = request.get_json()
    
    # Validate required fields
    if 'data' not in body:
        return jsonify({
            "success": False,
            "error": "Missing field",
            "message": "Request must include 'data' field"
        }), 400
    
    if 'format' not in body:
        return jsonify({
            "success": False,
            "error": "Missing field",
            "message": "Request must include 'format' field"
        }), 400
    
    data = body['data']
    output_format = body['format'].lower()
    
    # Validate format
    if output_format not in ['json', 'text']:
        return jsonify({
            "success": False,
            "error": "Invalid format",
            "message": "Format must be 'json' or 'text'"
        }), 400
    
    # Export to JSON
    if output_format == 'json':
        return jsonify({
            "success": True,
            "format": "json",
            "exported_data": data
        }), 200
    
    # Export to plain text
    if output_format == 'text':
        text_output = convert_to_text(data)
        return jsonify({
            "success": True,
            "format": "text",
            "exported_data": text_output
        }), 200


def convert_to_text(data, indent=0):
    """Convert data to readable plain text format."""
    
    lines = []
    prefix = "  " * indent
    
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                lines.append(f"{prefix}{key.upper()}:")
                lines.append(convert_to_text(value, indent + 1))
            else:
                lines.append(f"{prefix}{key}: {value}")
    
    elif isinstance(data, list):
        for i, item in enumerate(data, 1):
            if isinstance(item, dict):
                lines.append(f"{prefix}Item {i}:")
                lines.append(convert_to_text(item, indent + 1))
            else:
                lines.append(f"{prefix}- {item}")
    
    else:
        lines.append(f"{prefix}{data}")
    
    return "\n".join(lines)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
