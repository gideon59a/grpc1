import grpc
from concurrent import futures
import time

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# import the original calculator.py
import calculator

import os  # for print environment variables
# ADD LOG: per https://github.com/grpc/grpc/blob/master/src/python/grpcio_tests/tests/interop/server.py
#import logging
#logging.basicConfig()
#_LOGGER = logging.getLogger(__name__)

#rint(os.environ.get['http_proxy'])
os.environ["GRPC_VERBOSITY"] = "debug"
#os.environ["GRPC_TRACE"] = "tcp,http,secure_endpoint,transport_security"
#os.environ["GRPC_TRACE"] = "http" ### GRPC VERBOSE DEBUG
print(os.environ.get('GRPC_VERBOSITY'))

# create a class to define the server functions, derived from
# calculator_pb2_grpc.CalculatorServicer
class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

    # calculator.square_root is exposed here
    # the request and response are of the data type
    # calculator_pb2.NumberReply
    def SquareRootFactor(self, request, context):
        print("Request type and dump: ", type(request), '\n', request)
        response = calculator_pb2.NumberReply()  # prepare the response structure
        response.value = calculator.square_root_factor(request.value, request.factor)
        return response

    def Mult(self, request, context):
        print("Request type and dump: ", type(request), '\n', request)
        response = calculator_pb2.MultAll()
        response.multValue = calculator.mult(request.value, request.factor)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
calculator_pb2_grpc.add_CalculatorServicer_to_server(
        CalculatorServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')

# print(os.environ.get('GRPC_VERBOSITY'))

server.start()
#_LOGGER.info('Server serving.')
#server.wait_for_termination()
#_LOGGER.info('Server stopped; exiting.')


# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)

