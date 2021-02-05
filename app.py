from flask import Flask

app = Flask(__name__)

############
## Routes ##

# Landing Page
@app.route("/")
def home():
    pass

# Visualization 1
@app.route("/")
def vis1():
    pass

# Visualization 2
@app.route("/")
def vis2():
    pass

# Visualization 3
@app.route("/")
def vis3():
    pass

# Visualization 4
@app.route("/")
def vis4():
    pass

# Comparisons Page
@app.route("/")
def compare():
    pass

# Data Page
@app.route("/")
def data():
    pass

##  End Routes ##
#################

if __name__ == "__main__":
    app.run()