
def register_routes(api, app, root="connection_api"):
    from app.udaconnect.controllers.ConnectionController import api as udaconnect_api

    api.add_namespace(udaconnect_api, path=f"/{root}")
