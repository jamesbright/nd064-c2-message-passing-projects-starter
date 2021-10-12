from app.udaconnect.models.LocationModel import Location  # noqa
from app.udaconnect.schemas.LocationSchema import  LocationSchema  # noqa


def register_routes(api, app, root="location_api"):
    from app.udaconnect.controllers.LocationController import api as udaconnect_api

    api.add_namespace(udaconnect_api, path=f"/{root}")
