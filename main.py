from flask import Flask
import content
app = Flask(__name__)

@app.route("/")
def default():
    return content.TEMPLATE

def main():
    app.run()

if __name__ == "__main__":
    main()
