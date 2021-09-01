from flask import Blueprint, render_template, redirect, session

mainPages = Blueprint("mainPages", __name__)

@mainPages.route("/")
def mainPage():
    if 'loggedIn' in session:
        loggedIn = True
        username = session['username']
    else:
        loggedIn = False
        username = 'not logged in >:('
    return render_template("main.html", isLoggedIn=loggedIn, username=username)