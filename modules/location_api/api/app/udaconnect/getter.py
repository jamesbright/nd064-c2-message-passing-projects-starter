import grpc
import location_pb2
import location_pb2_grpc


channel = grpc.insecure_channel("localhost:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)

data = stub.Get(location_pb2.Empty())
print(data)
