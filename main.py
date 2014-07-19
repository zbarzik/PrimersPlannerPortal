import flask
import content
import primer_generator
app = flask.Flask(__name__)
app._static_folder = "./app/static"

@app.route("/", methods=["GET", "POST"])
def home():
    form = None
    if flask.request.method == "POST":
        form = flask.request.form
        wtForm = content.validateForm(form)
        if wtForm != None:
            if primer_generator.issue_request(wtForm):
                return flask.redirect(flask.url_for("submitted", result="success"))
            return flask.redirect(flask.url_for("submitted", result="failed"))
    return content.generatePage(form)

@app.route("/submitted/<result>")
def submitted(result):
    return "thanks for submitting! " + result  #placeholder
    
def main():
    app.run()

if __name__ == "__main__":
    main()
