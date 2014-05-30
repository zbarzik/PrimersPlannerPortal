from flask import Flask
import content
app = Flask(__name__)

@app.route("/")
def home():
    return content.generatePage()
    
def main():
    app.run()

if __name__ == "__main__":
    main()
