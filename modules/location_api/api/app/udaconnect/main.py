import time
from concurrent import futures

import grpc
import location_pb2
import location_pb2_grpc


class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Get(self, request, context):
        first_location = location_pb2.LocationMessage(
            id = 1,
            person_id = 2,
            longitude = '45.4323323',
            latitude = '4.55433353',
            creation_time = "2019-01-01T00:00:00Z"
        )

        second_location = location_pb2.LocationMessage(
            id = 2,
            person_id = 3,
            longitude = '7.4323323',
            latitude = '5.55433353',
            creation_time = "2019-01-01T00:00:00Z"
        )

        result = location_pb2.LocationMessageList()
        result.locations.extend([first_location, second_location])
        return result

    def Create(self, request, context):
        print("Received a message!")

        request_value = {
            "id": request.id,
            "person_id": request.person_id,
            "longitude": request.longitude,
            "latitude": request.latitude,
            "creation_time": request.creation_time
        }
        print(request_value)

        return location_pb2.LocationMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
