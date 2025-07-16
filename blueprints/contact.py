from flask import Blueprint, request, jsonify, render_template

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """Handle contact form submission and render contact page."""
    if request.method == 'POST':
        data = request.form
        # Simulate email sending by printing to console (replace with actual email service in production)
        print(f"Received contact form: Name={data['name']}, Email={data['email']}, Message={data['message']}")
        return jsonify({"message": "Form submitted successfully!"})
    return render_template('contact.html')