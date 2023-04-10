import {get} from "./dom.js";

export function plotMetrics(libraryName, algorithmName, metricData, time) {
    Object.keys(metricData).forEach((metricName) => {
        let metricPlot = App[`${libraryName}-${algorithmName}-plots`][`${metricName}`];

        addPlotTimeData(metricPlot, metricData[metricName], time);
    });
}

export function addPlotTimeData(plot, data, time) {
    let lastLabelIndex = plot.data.labels.length
    plot.data.labels.push(time.toFixed(2));

    plot.data.datasets.forEach((dataset) => {
        if (!dataset.isAnnotation) {
            dataset.data.push(data);
        }
    });

    plot.update();
}

export function binarySearch(array, el) {
    let m = 0;
    let n = array.length - 1;

    while (m <= n) {
        let k = (n + m) >> 1;
        let cmp = el - array[k];
        if (cmp > 0) {
            m = k + 1;
        } else if(cmp < 0) {
            n = k - 1;
        } else {
            return [k, k + 1];
        }
    }

    return [n, n + 1];
}

export function createPlotsVerticalLine(libraryName, algorithmName, name, xPosition) {
    for (const metricName in App[`${libraryName}-${algorithmName}-plots`]) {
        let plot = App[`${libraryName}-${algorithmName}-plots`][metricName];

        let interval = binarySearch(plot.data.labels, xPosition);
        let position = xPosition - plot.data.labels[interval[0]] < plot.data.labels[interval[1]] - xPosition ?
            interval[0] : interval[1];

        createVerticalLine(App[`${libraryName}-${algorithmName}-plots`][metricName], name, position);
    }
}

export function createVerticalLine(plot, name, xPosition) {
    plot.options.plugins.annotation.annotations[name] = {
        type: 'line',
        borderColor: '#fb7185',
        borderWidth: 5,
        borderDash: [8, 8],
        drawTime: 'beforeDraw',
        scaleID: 'x',
        value: xPosition
    };

    plot.data.datasets.push(
        {
            type: 'line',
            isAnnotation: true,
            label: name,
            backgroundColor: '#fb7185',
            data: []
        }
    );

    plot.update();
}

export function createAlgorithmPlots(libraryName, algorithmName) {
    let memoryCanvas = get(`${libraryName}-${algorithmName}-plot-memory`);
    let cpuCanvas = get(`${libraryName}-${algorithmName}-plot-cpu`);

    App[`${libraryName}-${algorithmName}-plots`] = {
        "memory": new Chart(memoryCanvas,
            {
                type: 'line',
                data: {
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
                options: {
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
                                text: 'Time (s)',
                                font: {
                                    size: 20
                                }
                            }
                        }
                    },
                    plugins: {
                        annotation: {
                            common: {
                                drawTime: 'beforeDraw'
                            },
                            annotations: {}
                        }
                    }
                }
            }
        ),
        "cpu": new Chart(cpuCanvas,
            {
                type: 'line',
                data: {
                    labels: [],
                    datasets: [
                        {
                            label: 'CPU (%)',
                            data: [],
                            fill: false,
                            borderColor: 'rgb(75, 192, 192)',
                            tension: 0.1,
                            pointStyle: 'circle',
                            pointRadius: 5,
                            pointHoverRadius: 10
                        }
                    ]
                },
                options: {
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
                                text: 'Time (s)',
                                font: {
                                    size: 20
                                }
                            }
                        }
                    },
                    plugins: {
                        annotation: {
                            common: {
                                drawTime: 'beforeDraw'
                            },
                            annotations: {}
                        }
                    }
                }
            }
        )
    };
}