import flask
import content
app = flask.Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    form = None
    #return content.generatePage()
    if flask.request.method == "POST":
        form = flask.request.form
        if content.validateForm(form):
            return flask.redirect(flask.url_for('submitted'))
    return content.generatePage(form)

@app.route("/submitted")
def submitted():
    return "thanks for submitting!" #placeholder
    
def main():
    app.run()

if __name__ == "__main__":
    main()
