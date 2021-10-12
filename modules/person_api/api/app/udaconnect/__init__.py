
def register_routes(api, app, root="person_api"):
    from app.udaconnect.controllers.PersonController import api as udaconnect_api

    api.add_namespace(udaconnect_api, path=f"/{root}")
