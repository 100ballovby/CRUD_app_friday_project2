from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), index=True)
    username = db.Column(db.String(80), index=True, unique=True)
    email = db.Column(db.String(255), index=True, unique=True)
    street = db.Column(db.String(255))
    city = db.Column(db.String(255), index=True)
    phone = db.Column(db.String(255))
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True)
    website = db.Column(db.String(255), index=True)


class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    completed = db.Column(db.Boolean, index=True)






