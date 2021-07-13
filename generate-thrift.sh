#!/bin/sh

# generate thrift files for python server
rm -rf ./thrift/gen-py
mkdir -p ./thrift/gen-py
thrift -r -out ./thrift/gen-py --gen py ./thrift/DemoService.thrift

# generate thrift files for react client
npm run codegen
