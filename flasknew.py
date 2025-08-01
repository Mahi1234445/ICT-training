from flask import Flask, render_template, request, redirect, url_for
from models import db, Appointment

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db
db.init_app(app)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form['name']
        mobile = request.form['mobile']
        date = request.form['date']
        time = request.form['time']

        # Save to database
        new_appointment = Appointment(name=name, mobile=mobile, date=date, time=time)
        db.session.add(new_appointment)
        db.session.commit()

        # Redirect to the page showing all appointments
        return redirect(url_for('appointment_page'))

    return render_template('home.html')

@app.route("/appointments")
def appointment_page():
    # Fetch all appointments
    appointments = Appointment.query.all()
    return render_template('appointments.html', appointments=appointments)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Creates tables if not already created
    app.run(debug=True)
