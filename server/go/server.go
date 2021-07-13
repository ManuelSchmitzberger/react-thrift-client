package main

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"time"

	"demo.com/gen-go/demoservice"
	"github.com/apache/thrift/lib/go/thrift"
)

type DemoServiceHandler struct {
}

func (p *DemoServiceHandler) Hello(ctx context.Context) (string, error) {
	fmt.Print("Hello Called\n")
	return "Hello from go.", nil
}

func main() {
	protocolFactory := thrift.NewTBinaryProtocolFactoryDefault()
	processor := demoservice.NewDemoServiceProcessor(&DemoServiceHandler{})

	multiplexed := thrift.NewTMultiplexedProcessor()
	multiplexed.RegisterProcessor("Demo", processor)

	mux := http.NewServeMux()
	mux.HandleFunc("/", thrift.NewThriftHandlerFunc(processor, protocolFactory, protocolFactory))

	server := http.Server{
		Addr:         "localhost:9090",
		Handler:      mux,
		ReadTimeout:  5 * time.Second,
		WriteTimeout: 5 * time.Second,
	}

	if err := server.ListenAndServe(); err != nil {
		log.Fatalf("failed to start Apache Thrift server: %v", err)
	}
}
