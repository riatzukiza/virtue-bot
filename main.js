require('babel-polyfill');
require('isomorphic-fetch');
if (!global.WebSocket) {
  global.WebSocket = require('ws');
}
const Client4 = require('./client/client4.js').default;
const client = new Client4;
const wsClient = require('./client/websocket_client.js').default;
var token;

wsClient.setEventCallback(function(event){
  console.log(event);
});

client.setUrl('https://your-mattermost-url.com');
client.login(username, password)
  .then(function(me){
    console.log(`logged in as ${me.email}`);
    token = client.getToken();
  })
  .then(function(){
    wsClient.initialize(token, {}, {}, {connectionUrl: 'wss://your-mattermost-url.com/api/v4/websocket'});
  })
  .catch(function(err){
    console.error(err);
  });
