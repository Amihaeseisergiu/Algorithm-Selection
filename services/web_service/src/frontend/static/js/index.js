import { get, click } from "./utils/dom.js";
import { upload } from "./utils/ajax.js";
import { addPlotTimeData, createAlgorithmPlots } from "./utils/chart.js";
import { createLibraryHTML } from "./components/metrics.js";

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

socket.on("metric_emit", (data, acknowledge) => {
    let emitState = data["payload"]["emit_state"];
    let libraryName = data["header"]["library_name"];

    if (emitState === "start") {
        let librariesElement = get("libraries");

        let newLibraryElement = createLibraryHTML(libraryName);
        librariesElement.appendChild(newLibraryElement);

        createAlgorithmPlots(libraryName);
    } else if (emitState === "intermediate") {
        let metrics = data["payload"]["metrics"];

        let memoryPlot = window[`${libraryName}-memory-plot`];
        let cpuPlot = window[`${libraryName}-cpu-plot`];

        addPlotTimeData(memoryPlot, metrics["memory"]);
        addPlotTimeData(cpuPlot, metrics["cpu"]);
    } else if (emitState === "end") {
        get(`${libraryName}-spinner`).remove();
    }
});