from flask_login import login_user,logout_user, login_required
from . import auth
from flask import render_template,redirect,url_for


@auth.route('/register',methods = ["GET","POST"])
def register():

    
    return render_template("auth/signup.html")


@auth.route("/login",methods = ["GET","POST"])
def login():

    return render_template("auth/login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main/index.html"))