import grpc
import location_pb2
import location_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)

# Update this with desired payload
location = location_pb2.LocationMessage(
    id = 1,
    person_id = 2,
    longitude = '6.4323323',
    latitude = '4.55433353',
    creation_time = '2019-01-01T00:00:00Z'
)


response = stub.Create(location)
