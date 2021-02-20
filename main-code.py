from flask import Flask, render_template, url_for, redirect, request, session, \
    flash
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from sports import *
from weather import *
from todo import *

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=1)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


@app.route("/login", methods=["POST", "GET"])
@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user1 = request.form["myname"]
        session["user"] = user1
        return redirect(url_for("home_page"))
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("home_page", user=session["user"]))
        return render_template("login.html")


@app.route("/home")
def home_page():
    if "user" in session:
        incomplete = Todo.query.filter_by(complete=False).all()
        return render_template("home.html", username=session["user"],
                               next_game=next_game, news_lst1=news_lst1,
                               temp=temp, time=time, wthr_img=wthr_img,
                               team_img2=team_img2, next_game2=next_game2,
                               todo=incomplete, lst_len=len(incomplete))
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    if "user" in session:
        flash("You have been logged out", "info")
    session.pop("user", None)
    return redirect(url_for("login"))


# todolist
class Todo(db.Model):
    id2 = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(150))
    complete = db.Column(db.Boolean)


@app.route("/todo")
def todo():
    todos = Todo.query.all()
    return render_template("todolist.html", values=todos)


@app.route("/todo/add", methods=["POST"])
def add():
    todo_item = Todo(item=request.form["todoitem"], complete=False)
    db.session.add(todo_item)
    db.session.commit()
    return redirect(url_for("todo"))


@app.route("/todo/comp/<id1>")
def task_completed(id1):
    todo_item = Todo.query.filter_by(id2=int(id1)).first()
    todo_item.complete = True
    db.session.commit()
    return redirect(url_for("todo"))


@app.route("/todo/del/<del_id>")
def delete(del_id):
    Todo.query.filter_by(id2=int(del_id)).delete()
    db.session.commit()
    return redirect(url_for("todo"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
