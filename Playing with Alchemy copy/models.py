from sqla_wrapper import SQLAlchemy

db = SQLAlchemy("sqlite:///localhost.sqlite?check_same_thread=False")

class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String, nullable=False)
    lastName = db.Column(db.String, nullable=False)
    company = db.Column(db.String, nullable=True)
    street = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    phone = db.Column(db.String, nullable=False)

class Bike(db.Model):
    __tablename__ = "bikes"
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    purchase_date = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)

class Invoice(db.Model):
    __tablename__ = "invoices"
    id = db.Column(db.Integer, primary_key=True)
    bike_id = db.Column(db.Integer, db.ForeignKey('bikes.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    date_borrowed = db.Column(db.String, nullable=False)
    date_returned = db.Column(db.String, nullable=False)
    lending_time = db.Column(db.Integer, nullable=False)
    price_per_minute = db.Column(db.Float, nullable=False)
    vat = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)