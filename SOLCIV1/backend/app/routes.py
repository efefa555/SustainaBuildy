from flask import request, jsonify
from app import app, db
from app.models import Building
from app.schemas import BuildingSchema

building_schema = BuildingSchema()
buildings_schema = BuildingSchema(many=True)

@app.route('/buildings', methods=['POST'])
def add_building():
    name = request.json['name']
    area = request.json['area']
    materials = request.json['materials']
    windows = request.json['windows']
    orientation = request.json['orientation']
    insulation = request.json['insulation']
    hvac = request.json['hvac']

    new_building = Building(name=name, area=area, materials=materials, windows=windows,
                            orientation=orientation, insulation=insulation, hvac=hvac)
    db.session.add(new_building)
    db.session.commit()

    return building_schema.jsonify(new_building)

@app.route('/buildings', methods=['GET'])
def get_buildings():
    all_buildings = Building.query.all()
    result = buildings_schema.dump(all_buildings)
    return jsonify(result)

@app.route('/buildings/<id>', methods=['GET'])
def get_building(id):
    building = Building.query.get(id)
    return building_schema.jsonify(building)

@app.route('/buildings/<id>', methods=['PUT'])
def update_building(id):
    building = Building.query.get(id)

    building.name = request.json['name']
    building.area = request.json['area']
    building.materials = request.json['materials']
    building.windows = request.json['windows']
    building.orientation = request.json['orientation']
    building.insulation = request.json['insulation']
    building.hvac = request.json['hvac']

    db.session.commit()

    return building_schema.jsonify(building)

@app.route('/buildings/<id>', methods=['DELETE'])
def delete_building(id):
    building = Building.query.get(id)
    db.session.delete(building)
    db.session.commit()

    return building_schema.jsonify(building)