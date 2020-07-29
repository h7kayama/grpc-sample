# gRPC Sample

refered to https://knowledge.sakura.ad.jp/24059/


## Python

### Setup
```
$ python3 -m venv venv
$ . venv/bin/activate
(venv) $ pip3 install grpcio grpcio-tools
```

### Generate
```
$ python3 -m grpc_tools.protoc -I./protos --python_out=./python --grpc_python_out=. ./protos/user.proto
```
