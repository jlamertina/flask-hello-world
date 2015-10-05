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

# dyanmic routes that accept int, float, and file path
@app.route("/int_test/<int:value>")
def int_type(value):
	print ("Int: incrementing {} is {}".format(value, value+1))   # print to console
	return "correct"
@app.route("/float_test/<float:entry>")
def float_type(entry):
	print ("Float: incrementing {} is {}".format(entry, entry+1))
	return "correct"
@app.route("/path_test/<path:input>")
def path_type(input):
	print ("Path: input path is {}".format(input))
	return "correct"

if __name__ =="__main__":
    app.run()
# run this file: python app.py
# open browser url: http://127.0.0.1:5000/
#  or equivalently: http://localhost:5000