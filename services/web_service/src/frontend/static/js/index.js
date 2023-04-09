import { get, getData, click, changed } from "./utils/dom.js";
import { upload } from "./utils/ajax.js";
import {initializeApp} from "./app/app.js";

click(get("send-instance-button"), () => {
    initializeApp();

    let fileData = get('upload-instance-input').files[0];
    let algorithmType = getData("instance-metadata", "algorithmType");
    let mode = getData("instance-metadata", "mode") === 0 ? 'sequential' : 'parallel';

    upload(fileData, 'http://localhost:5000/upload', (fileId) => {
       console.log("Uploaded file uuid: ", fileId);

       App.socket.emit(
            'send_instance',
            {
                "socket_id": App.socket.id,
                "file_id": fileId,
                "algorithm_type": algorithmType,
                "mode": mode
            }
        );
    });
});

click(get('upload-instance-button'), () => {
    get("upload-instance-input").click();
});

changed(get('upload-instance-input'), () => {
    let fileData = get('upload-instance-input').files[0];
    get('upload-instance-button').value = `Selected ${fileData.name}`;
});