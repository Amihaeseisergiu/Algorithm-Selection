import { get, click } from "./utils/dom.js";
import { upload } from "./utils/ajax.js";

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

let sendInstanceButton = get('send-instance-button');
let instanceFileInput = get('instance-file-input');

click(sendInstanceButton, (e) => {
    let fileData = instanceFileInput.files[0]

    upload(fileData, 'http://localhost:5000/upload', (fileId) => {
       console.log("Uploaded file uuid: ", fileId);

       socket.emit(
            'send_instance',
            {
                "socket_id": socket.id,
                "file_id": fileId
            }
        );
    });
});

socket.on("receive_algorithm_response", (data, acknowledge) => {
    console.log(data);

    if (acknowledge) {
        acknowledge();
    }
});