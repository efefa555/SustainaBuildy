import unittest
from app import app, db
from app.models import Building

class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_building_model(self):
        building = Building(name="Test Building", area=100.0, materials="Brick", windows=5,
                            orientation="South", insulation="Good", hvac="Central")
        db.session.add(building)
        db.session.commit()
        
        retrieved = Building.query.first()
        self.assertEqual(retrieved.name, "Test Building")

if __name__ == '__main__':
    unittest.main()