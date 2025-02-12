import unittest
from app import app, db
from app.models import Building

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_building(self):
        response = self.app.post('/buildings', json={
            'name': 'Test Building',
            'area': 100.0,
            'materials': 'Brick',
            'windows': 5,
            'orientation': 'South',
            'insulation': 'Good',
            'hvac': 'Central'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Building', response.get_data(as_text=True))

    def test_get_buildings(self):
        response = self.app.get('/buildings')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()