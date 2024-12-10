from flask import app


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:98521Tds@4444@localhost/myappdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
