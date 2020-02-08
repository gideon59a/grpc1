import grpc

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)

# create a valid request message
numberSet = calculator_pb2.NumberRequest(value=16, factor=10)

# make the call
response = stub.SquareRootFactor(numberSet)
print("The whole response: ", response)
print("Just the value: ", response.value)

# make another call with another rpc
response = stub.Mult(numberSet)
print("The whole response: ", response)
print("Just the value: ", response.multValue)