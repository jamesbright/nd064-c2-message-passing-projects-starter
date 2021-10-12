import time
from concurrent import futures

import grpc
import location_pb2
import location_pb2_grpc


class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Get(self, request, context):
        location1 = location_pb2.LocationMessage(
            id = 1,
            person_id = 2,
            longitude = '6.4323323',
            latitude = '7.55433353',
            creation_time = "2019-01-01T00:00:00Z"
        )

        location2 = location_pb2.LocationMessage(
            id = 2,
            person_id = 3,
            longitude = '7.4323323',
            latitude = '5.55433353',
            creation_time = "2019-01-01T00:00:00Z"
        )

        result = location_pb2.LocationMessageList()
        result.locations.extend([location1, location2])
        return result

    def Create(self, request, context):
        print("Received a message!")

        new_request = {
            "id":request.id,
            "person_id": request.person_id,
            "longitude": request.longitude,
            "latitude": request.latitude,
            "creation_time": request.creation_time
        }
        print(new_request)

        return location_pb2.LocationMessage(**new_request)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)


print("Server starting on port 5007...")
server.add_insecure_port("[::]:5007")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
