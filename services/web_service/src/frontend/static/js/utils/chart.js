import { get } from "./dom.js";

export function addPlotTimeData(plot, data) {
    let last_label_index = plot.data.labels.length

    plot.data.labels.push(last_label_index);
    plot.data.datasets.forEach((dataset) => {
        dataset.data.push(data);
    });

    plot.update();
}

export function createAlgorithmPlots(libraryName) {
    let memoryCanvas = get(`${libraryName}-plot-memory`);
    let cpuCanvas = get(`${libraryName}-plot-cpu`);

    window[`${libraryName}-memory-plot`] = new Chart(memoryCanvas,
        {
            type: 'line',
            data : {
                labels: [],
                datasets: [
                    {
                        label: 'Memory (MB)',
                        data: [],
                        fill: false,
                        borderColor: 'rgb(51, 102, 255)',
                        tension: 0.1,
                        pointStyle: 'circle',
                        pointRadius: 5,
                        pointHoverRadius: 10
                    }
                ]
            },
            options : {
                maintainAspectRatio: false,
                scales: {
                    y: {
                        title: {
                            display: true,
                            text: 'Memory (MB)',
                            font: {
                                size: 20
                            }
                        }
                    },
                    x: {
                        title: {
                            display: true,
                            text: 'Time (ds)',
                            font: {
                                size: 20
                            }
                        }
                    }
                }
            }
        }
    );

    window[`${libraryName}-cpu-plot`] = new Chart(cpuCanvas,
        {
            type: 'line',
            data : {
                labels: [],
                datasets: [
                    {
                        label: 'CPU (%)',
                        data: [],
                        fill: false,
                        borderColor: 'rgb(75, 192, 192)',
                        tension: 0.1
                    }
                ]
            },
            options : {
                maintainAspectRatio: false,
                scales: {
                    y: {
                        title: {
                            display: true,
                            text: 'CPU %',
                            font: {
                                size: 20
                            }
                        }
                    },
                    x: {
                        title: {
                            display: true,
                            text: 'Time (ds)',
                            font: {
                                size: 20
                            }
                        }
                    }
                }
            }
        }
    );
}