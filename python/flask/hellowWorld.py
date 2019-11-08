from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    #hello = "Hello World"
    #return hello
    html = render_teplate('index.html')
    return html

if __name__ == "__main__":
    app.run()

