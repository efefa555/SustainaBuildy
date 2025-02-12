from app import db

class Building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    area = db.Column(db.Float, nullable=False)
    materials = db.Column(db.String(200), nullable=False)
    windows = db.Column(db.Integer, nullable=False)
    orientation = db.Column(db.String(50), nullable=False)
    insulation = db.Column(db.String(200), nullable=False)
    hvac = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())