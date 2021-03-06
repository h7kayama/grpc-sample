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

## Nodejs

### Setup
```
$ npm install grpc grpc-tools google-protobuf
```

### Generate
```
./node_modules/.bin/grpc_tools_node_protoc -I./protos/ --js_out=import_style=commonjs,binary:./nodejs --grpc_out=./nodejs ./protos/user.proto
```

### Run
```
$ node nodejs/server.js
```

```
$ node nodejs/client.js 1
{
  error: false,
  message: '',
  user: {
    id: 1,
    nickname: 'admin',
    mailAddress: 'admin@example.com',
    userType: 1
  }
}
```
