#!/usr/bin/env python
import sys
sys.path.append('./thrift/gen-py')

from DemoService import DemoService
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TJSONProtocol
from thrift.server import THttpServer

class DemoServiceHandler:
    def hello(self):
        print("Hello Called")
        return "hello from Python"

processor = DemoService.Processor(DemoServiceHandler())
#protoFactory = TJSONProtocol.TJSONProtocolFactory()
protoFactory = TBinaryProtocol.TBinaryProtocolFactory()

port = 9090
server = THttpServer.THttpServer(processor, ("localhost", port), protoFactory)
print("Python server running on port " + str(port))
server.serve()
