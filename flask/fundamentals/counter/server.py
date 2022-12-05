from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def counter():
    if 'times' in session:
        session['times']+=1
    else:
        session['times']=1

    return render_template('index.html', times=session['times'])

@app.route('/destroy_session')
def reset_times():
    session.clear()

    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)
