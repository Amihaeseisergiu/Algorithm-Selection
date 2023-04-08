import { get, getData, click, changed } from "./utils/dom.js";
import { upload } from "./utils/ajax.js";
import { plotMetrics } from "./utils/chart.js";
import { addAlgorithmsMetricsHTML, addLibraryMetricsHTML, updateContainerHeights } from "./components/metrics.js";

window.App = {};
App.socket = io();

App.socket.on('connect', function() {
    App.socket.emit('register_socket', App.socket.id);
});

click(get("send-instance-button"), () => {
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

App.socket.on("library_end", (data) => {
    let libraryName = data["header"]["library_name"];
    if (get(`${libraryName}-spinner`)) {
        get(`${libraryName}-spinner`).remove();
    }
});

App.socket.on("schedule", (data) => {
    let libraryName = data["header"]["library_name"];
    let algorithmName = "algorithm_name" in data["header"] ? data["header"]["algorithm_name"] : null;

    addLibraryMetricsHTML(libraryName);

    if (algorithmName) {
        addAlgorithmsMetricsHTML(libraryName, algorithmName);
    }
});

App.socket.on("metric_emit", (data) => {
    let libraryName = data["header"]["library_name"];
    let algorithmName = data["payload"]["algorithm_name"];

    addLibraryMetricsHTML(libraryName);
    addAlgorithmsMetricsHTML(libraryName, algorithmName);

    let metrics = data["payload"]["metrics"];
    let time = data["payload"]["time"];

    plotMetrics(libraryName, algorithmName, metrics);
    get(`${libraryName}-${algorithmName}-time`).textContent = `${time.toFixed(2)} s`;

    if (time < 1) {
        updateContainerHeights(libraryName, algorithmName);
    }
});

App.socket.on("metric_end", (data) => {
    let libraryName = data["header"]["library_name"];
    let algorithmName = data["payload"]["algorithm_name"];

    addLibraryMetricsHTML(libraryName);
    addAlgorithmsMetricsHTML(libraryName, algorithmName);

    let time = data["payload"]["time"];

    if (get(`${libraryName}-${algorithmName}-spinner`)) {
        get(`${libraryName}-${algorithmName}-spinner`).remove();
        get(`${libraryName}-${algorithmName}-time`).textContent = `${time.toFixed(2)} s`;
    }
});