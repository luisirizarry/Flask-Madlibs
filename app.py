from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story


app = Flask(__name__)
app.config['SECRET_KEY'] = "idontknowwhatthisisfor"
debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    """Show homepage."""
    words = story.prompts
    return render_template("home.html", words=words)

@app.route('/story')
def show_story():
    """Show story result."""
    text = story.generate(request.args)
    return render_template("story.html", text=text)