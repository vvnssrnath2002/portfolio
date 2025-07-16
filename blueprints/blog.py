import json
from flask import Blueprint, render_template

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/blog')
def blog():
    """Render the blog page with posts from JSON."""
    with open('static/data/blog_posts.json', 'r') as f:
        posts = json.load(f)
    return render_template('blog.html', posts=posts)