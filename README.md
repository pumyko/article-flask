Flask Article Blog
A simple web application built with Flask for creating, viewing, updating, and deleting articles.

Features
* Create, view, update, and delete articles
* Input validation and error handling
* SQLite database integration using SQLAlchemy
* Jinja2-based templating
* Deployed to Heroku

Technologies Used
* Python 3.12
* Flask 3.1
* SQLAlchemy
* Bootstrap 5
* Jinja2
* HTML/CSS

Installation
`git clone https://github.com/yourusername/article-flask-blog.git
cd article-flask-blog
python -m venv .venv
.venv\Scripts\activate  # On Unix-based systems: source .venv/bin/activate
pip install -r requirements.txt
python app.py`

Project Structure
blog/
├── static/               # Static files: CSS, images, etc.
│   ├── css/
│   └── images/
├── templates/            # HTML templates (Jinja2)
│   ├── base.html
│   ├── index.html
│   └── ...
├── app.py                # Main Flask application
├── models.py             # SQLAlchemy models
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation

Deployment
The application is deployed on Heroku and accessible at:
https://article-flask-77d7d38ff20c.herokuapp.com