const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');
const PROTO_PATH = __dirname + '/../../protos/user.proto';
const packageDefinition = protoLoader.loadSync(PROTO_PATH);
const proto = grpc.loadPackageDefinition(packageDefinition);
const users = require('../../data/users.json');

function get(call, callback) {
  const userId = call.request.id;
  const user = users[userId];

  if (!user) {
    const response = { error: true, message: "not found" };
    callback(null, response);
    return;
  }

  const response = { error: false,
                     user: { id: user.id,
                             nickname: user.nickname,
                             mailAddress: user.mail_address,
                             userType: user.user_type },
                   };

  callback(null, response);
}

function main() {
  const server = new grpc.Server();
  server.addService(proto.UserManager.service, {get: get});
  server.bind('0.0.0.0:1234', grpc.ServerCredentials.createInsecure());
  server.start();
}

main();
