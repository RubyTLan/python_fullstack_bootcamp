from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return ('Hello World!')

@app.route('/dojo')
def dojo():
    return ('Dojo!')

@app.route('/say/<name>')
def say(name):
    return ('Hi '+name+'!')

@app.route('/repeat/<int:number>/<content>')
def repeat(number,content):
    return (content*number)

# @app.route('<a>')
# def error(a):
#     if a!='/' or a!='/dojo' or a!='/say/<name>' or a!='/repeat/<int:number>/<content>':
#         return('Sorry! No response. Try again')






if __name__=='__main__':
    app.run(debug=True)
