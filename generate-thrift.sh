#!/bin/sh

# generate thrift files for python server
rm -rf ./thrift/gen-py
mkdir -p ./thrift/gen-py
thrift -r -out ./thrift/gen-py --gen py ./thrift/DemoService.thrift

rm -rf ./thrift/gen-go
mkdir -p ./thrift/gen-go
thrift -r -out ./thrift/gen-go --gen go ./thrift/DemoService.thrift

# generate thrift files for react client
cd frontend && \
  npm run codegen
