import {get} from "../utils/dom.js";
import {addAlgorithmsMetricsHTML, addLibraryMetricsHTML} from "../components/metrics.js";
import {plotMetrics} from "../utils/chart.js";

export function initializeApp() {
    window.App = {};
    App.socket = io();

    get("libraries").innerHTML = "";

    App.socket.on('connect', function() {
        App.socket.emit('register_socket', App.socket.id);
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
}