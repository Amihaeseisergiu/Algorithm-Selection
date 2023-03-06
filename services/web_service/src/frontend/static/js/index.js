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
    console.log("click");

    socket.emit(
        'send_instance',
        {
            "id": id,
            "instance": "test"
        }
    );
});

socket.on("send_instance", (data, acknowledge) => {
    console.log(data);

    if (acknowledge) {
        acknowledge();
    }
});