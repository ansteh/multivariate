var Listener = (function(){
  var socket = io.connect('http://' + document.domain + ':' + location.port);

  socket.on('connect', function() {
    console.log('socket ready!');
  });

  var initSocket = function(url, callback){
    socket.on(url, function(data) {
      callback(data);
        socket.emit('my event', {data: 'I\'m connected!'});
    });

    return {
      emit: function(data) {
        socket.emit(url, data);
      }
    }
  };

  return {
    socket: initSocket
  }
}());
