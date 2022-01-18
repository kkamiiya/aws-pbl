from flask import Flask

app = Flask(__name__)

@app.route('/')
def hell():
    return "<h1>hello Flask~~!! hahaha<h1>"

@app.route('/test')
def test():
    #수행해야할 로직이 여기 들어온다.
    return "test"
if __name__=='__main__':
    app.run("0.0.0.0", port ="8080")
