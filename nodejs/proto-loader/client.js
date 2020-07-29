const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');
const PROTO_PATH = __dirname + '/../../protos/user.proto';
const packageDefinition = protoLoader.loadSync(PROTO_PATH);
const proto = grpc.loadPackageDefinition(packageDefinition);

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

  const client = new proto.UserManager('localhost:1234',
                                       grpc.credentials.createInsecure());

  client.get({id: userId}, function(err, response) {
    console.log(response);
  });
}

main();
