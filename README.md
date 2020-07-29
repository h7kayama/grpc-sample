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
$ python3 -m grpc_tools.protoc -I./protos --python_out=./python --grpc_python_out=./python ./protos/user.proto
```

### Run
```
(venv) $ python3 python/server.py
```

```
(venv) $ python3 python/client.py 1
user {
  id: 1
  nickname: "admin"
  mail_address: "admin@example.com"
  user_type: ADMINISTRATOR
}
```
