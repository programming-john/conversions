from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/canadatounited")
def render_page1():
    return render_template('canadatounited.html')

@app.route("/eurotodollar")
def render_page2():
    return render_template('eurotodollar.html')

@app.route("/dollartoeuro")
def render_page3():
    return render_template('dollartoeuro.html')

@app.route("/convertcd")
def render_response():
    memes = float(request.args['dollars'])
    #if 'dollars' in request.args:
        #reply= float(request.args['dollars']) * .80
    return render_template('convertcd.html', response=memes*.80)

@app.route("/convertue")
def render_response2():
    memes = float(request.args['dollars'])
    if 'dollars' in request.args:
        reply= float(request.args['dollars']) * 1.18
    return render_template('convertue.html', response=reply)

@app.route("/converteu")
def render_response3():
    memes= float(request.args['euros'])
    if 'euros' in request.args:
        reply= float(request.args['euros']) * .85
    return render_template('converteu.html', response=reply)

if __name__=="__main__":
    app.run(debug=False, port=54321)
