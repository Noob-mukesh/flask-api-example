


from flask import Flask, jsonify,render_template
import random
import datetime


app=Flask(__name__)

@app.route("/")


def main_x():
    year=datetime.datetime.now().year

    random_num=random.randint(1,30)

    return render_template("index.html",ran=random_num,year=year)

@app.route("/docs")

def docs_y():
    return render_template("doc.html")