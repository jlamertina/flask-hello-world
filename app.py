from flask import Flask
app = Flask(__name__)
# static routes "/"" and "/hello" aligned with hello_world()
@app.route("/")
@app.route("/hello")
def hello_world():
    return "Hello SFU World!"
# dynamic route "/test/..." aligned with search()
@app.route("/test/<search_query>")
def search(search_query):
	return search_query
if __name__ =="__main__":
    app.run()
# run this file: python app.py
# open browser url: http://127.0.0.1:5000/
#  or equivalently: http://localhost:5000