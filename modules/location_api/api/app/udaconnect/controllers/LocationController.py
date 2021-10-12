

from app.udaconnect.models.LocationModel import Location
from app.udaconnect.schemas.LocationSchema import   LocationSchema
from app.udaconnect.services.LocationService import  LocationService
from kafka import KafkaProducer
from flask import  jsonify, request, g
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import  List

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa


# TODO: This needs better exception handling
@api.route('/health')
def health():
    return jsonify({'response': 'Hello World!'})


@api.before_request
def before_request():
    # Set up a Kafka producer
    TOPIC_NAME = 'locations'
    KAFKA_SERVER = 'localhost:9092'
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
    # Setting Kafka to g enables us to use this
    # in other parts of our application
    g.kafka_producer = producer

@api.route("/person")
class LocationResource(Resource):
    @accepts(schema=LocationSchema)
    @responds(schema=LocationSchema)
    def post(self) -> Location:
        payload = request.get_json()
        new_location: Location = LocationService.create(payload)
        return new_location

    @responds(schema=LocationSchema, many=True)
    def get(self) -> List[Location]:
        locations: List[Location] = LocationService.retrieve_all()
        return locations

@api.route("/location/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    @accepts(schema=LocationSchema)
    @responds(schema=LocationSchema)
    def post(self) -> Location:
        request.get_json()
        location: Location = LocationService.create(request.get_json())
        return location

    @responds(schema=LocationSchema)
    def get(self, location_id) -> Location:
        location: Location = LocationService.retrieve(location_id)
        return location

