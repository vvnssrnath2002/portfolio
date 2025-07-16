from flask import Flask, render_template, request, jsonify
from blueprints.home import home_bp
from blueprints.about import about_bp
from blueprints.projects import projects_bp
from blueprints.blog import blog_bp
from blueprints.contact import contact_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(home_bp)
app.register_blueprint(about_bp)
app.register_blueprint(projects_bp)
app.register_blueprint(blog_bp)
app.register_blueprint(contact_bp)

if __name__ == '__main__':
    app.run(debug=True)