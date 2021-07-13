#!/usr/bin/env python
import sys

sys.path.append('./thrift/gen-py')

from DemoService import *
from DemoService.ttypes import *

# Thrift files
from thrift import Thrift
from thrift.transport import THttpClient
from thrift.protocol import TJSONProtocol
from thrift.protocol import TBinaryProtocol

# Init thrift connection and protocol handlers
transport = THttpClient.THttpClient('http://localhost:9090/')
#protocol = TJSONProtocol.TJSONProtocol(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

# Set client to our DemoService
client = DemoService.Client(protocol)

# Connect to server
transport.open()

hello = client.hello()
print(hello)

# Close connection
transport.close()

