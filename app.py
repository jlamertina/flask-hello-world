from flask import Flask

app = Flask(__name__)

# Enable debugging in the browser
app.config["DEBUG"] = True

# static routes "/"" and "/hello" aligned with hello_world()
@app.route("/")
@app.route("/hello")
def hello_world():
    return "Hello SFU World! You have changed!"
# dynamic route "/test/..." aligned with search()
@app.route("/test/<search_query>")
def search(search_query):
	return search_query

# dyanmic routes that accept int, float, and file path
@app.route("/int_test/<int:value>")
def int_type(value):
	print ("Int: incrementing {} is {}".format(value, value+1))   # print to console
	return "correct! Integer {}".format(value)
@app.route("/float_test/<float:entry>")
def float_type(entry):
	print ("Float: incrementing {} is {}".format(entry, entry+1))
	return "correct! Float {}".format(entry)
@app.route("/path_test/<path:input>")
def path_type(input):
	print ("Path: input path is {}".format(input))
	return "correct! Path is {}".format(input)

@app.route("/name/<userName>")
def index(userName):
	low = userName.lower()
	if low =="francis":
		print("Match {} = {}".format(userName,low))
		# return userName with 200 status code (200 = ok)
		return "Ok, {}".format(userName), 200
	else:
		# return 400 status code (requested information not found)
		return "Not found", 404

if __name__ =="__main__":
    app.run()

# run this file: python app.py
# open browser url: http://127.0.0.1:5000/
#  or equivalently: http://localhost:5000
# 
# Common HTTP status codes:
#   200 - OK
#   400 Series (typically indicates client error)
#	   401 - Authorization required
#      404 - Not Found
# 	500 Series (typically indicates server error)
#	500 - Internal Error