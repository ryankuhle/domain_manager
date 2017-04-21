from flask import render_template
from flask import request, redirect, url_for

from . import app
from .database import session, Entry

@app.route("/")
def entries():
    entries = session.query(Entry)
    entries = entries.order_by(Entry.datetime.desc())
    entries = entries.all()
    return render_template("entries.html",
        entries=entries
    )

@app.route("/entry/add", methods=["GET"])
def add_entry_get():
    return render_template("add_entry.html")



@app.route("/entry/add", methods=["POST"])
def add_entry_post():
    entry = Entry(
        url = request.form["url"],
        date_added = request.form["date_added"],
        web_host = request.form["web_host"],
        host_login = request.form["host_login"],
        username = request.form["username"],
        password = request.form["password"],
        city = request.form["city"],
        niche = request.form["niche"],
        forwarding_email = request.form["forwarding_email"],
        # datetime = "12345"
    )
    session.add(entry)
    session.commit()
    return redirect(url_for("entries"))
