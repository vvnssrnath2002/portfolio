from flask import Blueprint, render_template

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/projects')
def projects():
    """Render the projects page with Raghu Nath's projects."""
    projects = [
        {
            "title": "Bone Fracture Detection Using Python",
            "description": "Developed a CNN-based system to classify X-ray images as fractured or normal using the MURA dataset. Built a user-friendly GUI for real-time image upload and classification, leveraging OpenCV for preprocessing.",
            "link": "#",
            "tech": "Python, OpenCV",
            "date": "April 2023 – July 2023"
        },
        {
            "title": "Sentiment Analysis of Twitter Data",
            "description": "Built a sentiment analysis system to classify tweets into Positive, Negative, or Neutral categories using a large Twitter dataset. Developed a Django-based web interface for real-time classification.",
            "link": "#",
            "tech": "Python, Django",
            "date": "November 2023 – May 2024"
        },
        {
            "title": "Explainable AI for Heavy Rainfall Prediction",
            "description": "Developed an XAI-based system to predict high-impact rainfall events using CNNs and LSTMs. Integrated SHAP and LIME for model transparency and deployed via Flask for meteorological applications.",
            "link": "#",
            "tech": "Python, TensorFlow, Scikit-learn, Flask",
            "date": "February 2025 – April 2025"
        }
    ]
    return render_template('projects.html', projects=projects)