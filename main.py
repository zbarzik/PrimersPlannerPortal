import flask
import content
app = flask.Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    #return content.generatePage()
    if flask.request.method == "POST":
        form = flask.request.form
        if content.validateForm(form):
            return flask.redirect(flask.url_for('submitted'))
    return content.generatePage()

@app.route("/submitted")
def submitted():
    return "thanks for submitting!" #placeholder
    
def main():
    app.run()

if __name__ == "__main__":
    main()
