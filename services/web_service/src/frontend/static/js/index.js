import {get, getData, click, changed} from "./utils/dom.js";
import {upload} from "./utils/ajax.js";
import {initializeApp} from "./app/app.js";
import {addAlgorithmSelectionPanel} from "./components/selection.js";

click(get("send-instance-button"), () => {
    initializeApp(() => {
        let fileData = get('upload-instance-input').files[0];
        let fileName = fileData.name;
        let algorithmType = getData("instance-metadata", "algorithmType");
        let mode = getData("instance-metadata", "mode");

        upload(fileData, 'http://localhost:5000/upload', (fileId) => {
            console.log("Uploaded file uuid: ", fileId);
            addAlgorithmSelectionPanel();

            App.socket.emit(
                mode === 0 ? 'send_instance_sequential' : 'send_instance_parallel',
                {
                    "socket_id": App.socket.id,
                    "file_id": fileId,
                    "file_name": fileName,
                    "algorithm_type": algorithmType
                }
            );
        });
    });
});

click(get('upload-instance-button'), () => {
    get("upload-instance-input").click();
});

changed(get('upload-instance-input'), () => {
    let fileData = get('upload-instance-input').files[0];
    get('upload-instance-button').value = `Selected ${fileData.name}`;
});