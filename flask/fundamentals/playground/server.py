from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/<number>/<color>')
def play(number,color):
    return render_template('index.html', times=int(number), color=color)


if __name__=="__main__":
    app.run(debug=True)
