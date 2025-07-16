from flask import Blueprint, render_template

about_bp = Blueprint('about', __name__)

@about_bp.route('/about')
def about():
    """Render the about page with personal details."""
    return render_template('about.html')