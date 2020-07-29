const grpc = require('grpc');
const messages = require('./user_pb');
const services = require('./user_grpc_pb');
const users = require('../data/users.json');

function get(call, callback) {
  const userId = call.request.getId();
  const user = users[userId];

  if (!user) {
    const response = new messages.UserResponse();
    response.setError(true);
    response.setMessage("not found");
    callback(null, response);
    return;
  }

  const target = new messages.User();
  target.setId(user.id);
  target.setNickname(user.nickname);
  target.setMailAddress(user.mail_address);
  target.setUserType(messages.User.UserType[user.user_type]);

  const response = new messages.UserResponse();
  response.setError(false);
  response.setUser(target);

  callback(null, response);
}

function main() {
  const server = new grpc.Server();
  server.addService(services.UserManagerService, { get: get });
  server.bind('0.0.0.0:1234', grpc.ServerCredentials.createInsecure());
  server.start();
}

main();
