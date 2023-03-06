let socket = io();
let id = null;

socket.on('connect', function() {
    console.log('Socket id: ' + socket.id);
    socket.emit('register');
});

socket.on("register", (data, acknowledge) => {
    console.log(data);
    id = data['id'];

    if (acknowledge) {
        acknowledge();
    }
});

sendInstanceButton = document.getElementById('send-instance-button');

sendInstanceButton.addEventListener('click', (e) => {
    socket.emit(
        'send_instance',
        {
            "socket_id": socket.id,
            "data": "test"
        }
    );
});

socket.on("receive_algorithm_response", (data, acknowledge) => {
    console.log(data);

    if (acknowledge) {
        acknowledge();
    }
});