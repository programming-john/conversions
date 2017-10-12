from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("canadatounited")
def render_page1():
    return render_template('canadatounited.html')

@app.route("eurotodollar")
def render_page2():
    return render_template('eurotodollar.html')

@app.route("dollartoeuro")
def render_page3():
    return render_template('dollartoeuro.html')

if __name__=="__main__":
    app.run(debug=False, port=54321)
