const grpc = require('grpc');
const messages = require('./user_pb');
const services = require('./user_grpc_pb');

function main() {
  if (process.argv.length < 3) {
    console.log(`usage: node ${process.argv[1]} <user_id>`);
    return;
  }
  const userId = Number(process.argv[2]);
  if (isNaN(userId)) {
    console.log(`error: invalid user_id \`${process.argv[2]}'`);
    console.log(`usage: node ${process.argv[1]} <user_id>`);
    return;
  }

  const request = new messages.UserRequest();
  request.setId(userId);

  const client = new services.UserManagerClient('localhost:1234',
                                                grpc.credentials.createInsecure());
  client.get(request, function(err, response) {
    console.log(response.toObject());
  });
}

main();
