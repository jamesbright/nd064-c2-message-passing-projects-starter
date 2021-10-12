from app.udaconnect.schemas.LocationSchema import LocationSchema
from app.udaconnect.schemas.PersonSchema import PersonSchema
from geoalchemy2.types import Geometry as GeometryType
from marshmallow import Schema, fields
from marshmallow_sqlalchemy.convert import ModelConverter as BaseModelConverter





class ConnectionSchema(Schema):
    location = fields.Nested(LocationSchema)
    person = fields.Nested(PersonSchema)
