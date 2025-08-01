from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    mobile = db.Column(db.String(15), nullable=False)
    date = db.Column(db.String(20), nullable=False)  # Storing as string for simplicity
    time = db.Column(db.String(20), nullable=False)  # Storing as string for simplicity

    def __repr__(self):
        return f"<Appointment {self.name} on {self.date} at {self.time}>"
