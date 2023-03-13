import { get, getData, click, changed } from "./utils/dom.js";
import { upload } from "./utils/ajax.js";
import { plotMetrics } from "./utils/chart.js";
import { addAlgorithmsMetricsHTML, addLibraryMetricsHTML } from "./components/metrics.js";

window.App = {};
App.socket = io();

App.socket.on('connect', function() {
    console.log('Socket id: ' + App.socket.id);
    App.socket.emit('register');
});

App.socket.on("register", (data, acknowledge) => {
    console.log(data);

    acknowledge();
});

click(get("send-instance-button"), () => {
    let fileData = get('upload-instance-input').files[0];
    let algorithmType = getData("instance-metadata", "algorithmType");

    upload(fileData, 'http://localhost:5000/upload', (fileId) => {
       console.log("Uploaded file uuid: ", fileId);

       App.socket.emit(
            'send_instance',
            {
                "socket_id": App.socket.id,
                "file_id": fileId,
                "algorithm_type": algorithmType
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

App.socket.on("library_emit", (data) => {
    let libraryName = data["header"]["library_name"];
    get(`${libraryName}-spinner`).remove();
});

App.socket.on("metric_emit", (data) => {
    let emitState = data["payload"]["emit_state"];
    let libraryName = data["header"]["library_name"];
    let algorithmName = data["payload"]["algorithm_name"];

    if (emitState === "intermediate") {
        addLibraryMetricsHTML(libraryName);
        addAlgorithmsMetricsHTML(libraryName, algorithmName);

        let metrics = data["payload"]["metrics"];

        plotMetrics(libraryName, algorithmName, metrics);
    } else if (emitState === "end") {
        get(`${libraryName}-${algorithmName}-spinner`).remove();
    }
});