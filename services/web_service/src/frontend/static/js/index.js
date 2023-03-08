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
    if (acknowledge) {
        acknowledge();
    }

    let metrics = data["metrics"];
    let data_points = metrics["memory"].length;

    let x_axis = [...Array(data_points).keys()];

    let plotMemory = get("plot-memory");
    let plotCpu = get("plot-cpu");

    console.log(metrics);
    console.log(data_points);
    console.log(x_axis);

    let memoryTrace = {
        x: x_axis,
        y: metrics["memory"],
        mode: 'lines+markers',
        name: 'Memory (MB)'
    };

    let cpuTrace = {
        x: x_axis,
        y: metrics["cpu"],
        mode: 'lines+markers',
        name: 'CPU %'
    };

    let memoryLayout = {
        title: 'Memory usage over time',
        xaxis: {
            title: {
              text: 'Time (s)'
            },
          },
        yaxis: {
            title: {
              text: 'Memory (MB)'
            }
          }
    };

    let cpuLayout = {
        title: 'CPU usage over time',
        xaxis: {
            title: {
              text: 'Time (s)'
            },
          },
        yaxis: {
            title: {
              text: 'CPU (%)'
            }
          }
    };

    Plotly.newPlot(plotMemory, [memoryTrace], memoryLayout);
    Plotly.newPlot(plotCpu, [cpuTrace], cpuLayout);
});