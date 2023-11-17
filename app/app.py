from flask import Flask, render_template, request, redirect, url_for

app = Flask(_name_)

if _name_ == "_main_":
    app.run(debug=True)