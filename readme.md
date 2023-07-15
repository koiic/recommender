#### PYTHON MICROSERVICE WITH GRPC 

## Implement microservices in Python that communicate with one another over gRPC
- [x] command line interface - This generates several Python files from the .proto file. Here’s a breakdown:
  
  - `python -m grpc_tools.protoc` runs the protobuf compiler, which will generate Python code from the protobuf code. 
  - `-I ../protobufs` tells the compiler where to find files that your protobuf code imports. You don’t actually use the import feature, but the -I flag is required nonetheless.
  - `--python_out=. --grpc_python_out=.` tells the compiler where to output the Python files. As you’ll see shortly, it will generate two files, and you could put each in a separate directory with these options if you wanted to.
  - `../protobufs/recommendations.proto` is the path to the protobuf file, which will be used to generate the Python code.
  - Full command is `python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/recommendations.proto` 
  
## Implement middleware to monitor microservices
## Unit test and integration test your microservices and middleware
## Deploy microservices to a Python production environment with Kubernetes
