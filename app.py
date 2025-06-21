from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "blog.db")
app.config["SQLALCHEMY_DATABASE_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id
#  при запросе в бд выйдет объект и его id


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/empty_error')
def empty_error():
    return render_template("empty_error.html")


@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    if request.method == "POST":
        title = request.form.get('title', '').strip()
        intro = request.form.get('intro', '').strip()
        text = request.form.get('text', '').strip()

        if not title or not intro or not text:
            return redirect('/empty_error')

        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/posts')
        except Exception as e:
            return f"An error occurred while adding the article: {e}"

    return render_template("create-article.html")


@app.route('/posts')
def posts():
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template("posts.html", articles=articles)


@app.route('/posts/<int:id>')
def post_detail(id):
    article = Article.query.get(id)
    return render_template("post_detail.html", article=article)


@app.route('/posts/<int:id>/del')
def post_delete(id):
    article = Article.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect('/posts')
    except:
        return "An error occurred while deleting article"


@app.route('/posts/<int:id>/update', methods=['POST', 'GET'])
def post_update(id):
    article = Article.query.get(id)
    if request.method == "POST":
        article.title = request.form.get('title', '').strip()
        article.intro = request.form.get('intro', '').strip()
        article.text = request.form.get('text', '').strip()

        if not article.title or not article.intro or not article.text:
            return redirect('/empty_error')

        try:
            db.session.commit()
            return redirect('/posts')
        except Exception as e:
            return f"An error occurred while editing the article: {e}"
    else:
        article = Article.query.get(id)
        return render_template("post_update.html", article=article)


'''
@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User Page: " + name + " - " + str(id)
'''

if __name__ == "__main__":
    app.run(debug=True)


