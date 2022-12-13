from flask import Flask, render_template, redirect,request
from user import User
app = Flask(__name__)

@app.route("/users")
def read_all():
    users = User.get_all()
    return render_template("read_all.html",users=users)


@app.route("/users/new")
def form():
    return render_template("create.html")


@app.route("/users/create" ,methods=['post'])
def create():
    User.save(request.form)
    return redirect('/users')

@app.route("/users/<int:id>")
def show_one(id):
    data={
        'id':id
    }
    user=User.get_one(data)
    return render_template("read_one.html",user=user)

@app.route("/users/<int:id>/edit")
def display_form(id):
    user=User.get_one({'id':id})
    return render_template('edit.html',user=user)

@app.route("/users/<int:id>/update",methods=['post'])
def update(id):
    data={
        'id':id,
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email']
    }
    User.update(data)
    return redirect('/users/'+str(id))


@app.route("/users/<int:id>/delete")
def delete(id):
    data={
        'id':id,
    }
    User.delete(data)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)
