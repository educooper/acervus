# models/password_reset_code.py

from app.extensions import db
from datetime import datetime, timedelta

class PasswordResetCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), nullable=False)
    code = db.Column(db.String(6), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def is_valid(self):
        return datetime.utcnow() - self.created_at < timedelta(minutes=10)
