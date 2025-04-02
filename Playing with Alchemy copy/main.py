from flask import Flask, render_template, request
from datetime import datetime
from models import Customer, Bike, Invoice, db

app = Flask(__name__)
db.create_all()

@app.route('/', methods=['GET'])
def index():
    customers = db.query(Customer).all()
    bikes = db.query(Bike).all()
    return render_template('index.html', customers=customers, bikes=bikes)

@app.route('/submit_rental', methods=['POST'])
def submit_rental():
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    email = request.form.get('email')
    company = request.form.get('company')
    city = request.form.get('city')
    street = request.form.get('street')
    phone = request.form.get('phone')

    existing_customer = db.query(Customer).filter_by(email=email).first()

    if existing_customer:
        customer_id = existing_customer.id
    else:
        new_customer = Customer(
            firstName=first_name,
            lastName=last_name,
            email=email,
            company=company,
            city=city,
            street=street,
            phone=phone
        )
        db.session.add(new_customer)
        db.session.commit()
        customer_id = new_customer.id

    bike_id = request.form.get('bike')
    rental_start = datetime.strptime(request.form.get('rental-start'), '%Y-%m-%dT%H:%M')
    rental_end = datetime.strptime(request.form.get('rental-end'), '%Y-%m-%dT%H:%M')

    lending_time = (rental_end - rental_start).total_seconds() / 60

    price_per_minute = 0.5
    vat = 0.2
    total = lending_time * price_per_minute * (1 + vat)

    invoice = Invoice(
        bike_id=bike_id,
        customer_id=customer_id,
        date_borrowed=rental_start,
        date_returned=rental_end,
        lending_time=lending_time,
        price_per_minute=price_per_minute,
        vat=vat,
        total=total
    )
    
    db.session.add(invoice)
    db.session.commit()

    return render_template("success.html")

if __name__ == '__main__':
    app.run(debug=True, port=5020)