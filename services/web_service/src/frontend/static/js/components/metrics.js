import {get, getData, setData} from "../utils/dom.js";
import {createAlgorithmPlots} from "../utils/chart.js";

export function addLibraryMetricsHTML(libraryName) {
    if (!get(`${libraryName}-metrics`)) {
        let librariesElement = get("libraries");

        let newLibraryElement = createLibraryMetricsHTML(libraryName);
        librariesElement.appendChild(newLibraryElement);
    } else if(get(`${libraryName}-scheduled`)) {
        setData(`${libraryName}-metrics`, "selected", true);
        get(`${libraryName}-scheduled`).remove();
    }
}

export function updateContainerHeights(libraryName, algorithmName) {
    let libraryElement = get(`${libraryName}-algorithms`);
    let algorithmsElement = get(`${libraryName}-${algorithmName}-metrics-container`);

    algorithmsElement.style.maxHeight = algorithmsElement.scrollHeight + "px";
    libraryElement.style.maxHeight = libraryElement.scrollHeight + algorithmsElement.scrollHeight + "px";
}

export function addAlgorithmsMetricsHTML(libraryName, algorithmName) {
    if (!get(`${libraryName}-${algorithmName}-metrics`)) {
        let libraryElement = get(`${libraryName}-algorithms`);

        let newAlgorithmElement = createAlgorithmMetricsHTML(libraryName, algorithmName);
        libraryElement.appendChild(newAlgorithmElement);

        if (!(`${libraryName}-${algorithmName}-plots` in App)) {
            createAlgorithmPlots(libraryName, algorithmName);
        }

        VanillaTilt.init(get(`${libraryName}-${algorithmName}-plot-memory-container`), {max: 5, scale:1.02, reverse: true});
        VanillaTilt.init(get(`${libraryName}-${algorithmName}-plot-cpu-container`), {max: 5, scale:1.02, reverse: true});
    } else if(get(`${libraryName}-${algorithmName}-scheduled`)) {
        setData(`${libraryName}-${algorithmName}-metrics`, "selected_algorithm", true);
        get(`${libraryName}-${algorithmName}-scheduled`).remove();
    }
}

export function createLibraryMetricsHTML(libraryName) {
    let div = document.createElement('div');

    div.innerHTML = `
        <div class="flex flex-col items-center w-full popIn py-1"
             x-data="{selected: false}"
             id="${libraryName}-metrics">
            <div class="flex flex-row items-center text-2xl w-full font-semibold rounded-2xl border-2 border-solid border-gray-300
                 text-neutral-400 py-2 px-4 my-2 cursor-pointer duration-500 hover:border-rose-400
                 hover:text-neutral-500 hover:scale-[1.02] hover:shadow-xl"
                 :class="selected ? 'shadow-xl text-neutral-500 border-rose-400 scale-[1.02]' : 'shadow'"
                 @click="selected = !selected">
                <div id="${libraryName}-scheduled" class="pr-2">
                    Scheduled:
                </div>
                <div>
                    ${libraryName}
                </div>
                <div id="${libraryName}-spinner"
                     class="inline-block h-4 w-4 animate-spin rounded-full ml-2 text-rose-400
                            border-4 border-solid border-current border-r-transparent
                            align-[-0.125em] motion-reduce:animate-[spin_1.5s_linear_infinite]"
                    role="status">
                    <span class="!absolute !-m-px !h-px !w-px !overflow-hidden
                                 !whitespace-nowrap !border-0 !p-0 ![clip:rect(0,0,0,0)]">
                        Loading...
                    </span>
                </div>
            </div>

            <div class="max-h-0 w-[99%] overflow-hidden transition-all duration-500 bg-white rounded-b-2xl shadow-lg -mt-2
                 flex flex-col items-center"
                 x-ref="${libraryName}_algorithms_container"
                 id="${libraryName}-algorithms"
                 :style="selected ? 'max-height: ' + 
                 ($refs.${libraryName}_algorithms_container.scrollHeight > 0 ? $refs.${libraryName}_algorithms_container.scrollHeight : 350) + 'px' : ''">
            </div>
        </div>
    `;

    return div.firstElementChild;
}

export function createAlgorithmMetricsHTML(libraryName, algorithmName) {
    let div = document.createElement('div');

    div.innerHTML = `
        <div class="flex flex-col w-full p-4"
             x-data="{selected_algorithm: false}"
             id="${libraryName}-${algorithmName}-metrics">
            <div class="flex flex-row justify-between items-center text-2xl font-semibold text-neutral-500 border-b-4
                        rounded-b-md hover:border-rose-400 transition-all duration-500 cursor-pointer"
                 @click="selected_algorithm = !selected_algorithm;
                    $refs.${libraryName}_algorithms_container.style.maxHeight = $refs.${libraryName}_algorithms_container.scrollHeight +
                        $refs.${libraryName}_${algorithmName.replace(/[^A-Z0-9]+/ig, "_")}_metrics_container.scrollHeight + 'px';">
                <div class="flex items-center px-2 pb-2">
                    <div class="pr-2" id="${libraryName}-${algorithmName}-scheduled">
                        Scheduled:
                    </div>
                    <div>
                        ${algorithmName}
                    </div>
                </div>
                <div class="flex flex-row items-center justify-center">
                    <div id="${libraryName}-${algorithmName}-time">
                    </div>
                    <div id="${libraryName}-${algorithmName}-spinner"
                         class="inline-block h-4 w-4 animate-spin rounded-full ml-2 text-rose-400
                                border-4 border-solid border-current border-r-transparent
                                align-[-0.125em] motion-reduce:animate-[spin_1.5s_linear_infinite]"
                        role="status">
                        <span class="!absolute !-m-px !h-px !w-px !overflow-hidden
                                     !whitespace-nowrap !border-0 !p-0 ![clip:rect(0,0,0,0)]">
                            Loading...
                        </span>
                    </div>
                </div>
            </div>
            
            <div class="max-h-0 w-full overflow-hidden transition-all duration-500 rounded-b-2xl -mt-2
                 flex flex-col items-center"
                 x-ref="${libraryName}_${algorithmName.replace(/[^A-Z0-9]+/ig, "_")}_metrics_container"
                 id="${libraryName}-${algorithmName}-metrics-container"
                 :style="selected_algorithm ? 'max-height: ' + 
                    $refs.${libraryName}_${algorithmName.replace(/[^A-Z0-9]+/ig, "_")}_metrics_container.scrollHeight + 'px' : ''">
                 
                 <div class="flex items-center w-full pb-2">
                    <div id="${libraryName}-${algorithmName}-plot-memory-container"
                         class="grow w-1/2 h-64 mt-4 mx-2 rounded-lg border border-solid border-gray-300">
                        <div class="flex flex-col divide-y-2">
                            <div class="p-1 text-neutral-400 font-semibold flex justify-center">
                                Memory usage over time
                            </div>
                            <div class="h-56">
                                <canvas id="${libraryName}-${algorithmName}-plot-memory"></canvas>
                            </div>
                        </div>
                    </div>
    
                    <div id="${libraryName}-${algorithmName}-plot-cpu-container"
                         class="grow w-1/2 h-64 mt-4 mx-2 rounded-lg border border-solid border-gray-300">
                        <div class="flex flex-col divide-y-2">
                            <div class="p-1 text-neutral-400 font-semibold flex justify-center">
                                CPU usage over time
                            </div>
                            <div class="h-56">
                                <canvas id="${libraryName}-${algorithmName}-plot-cpu"></canvas>
                            </div>
                        </div>
                    </div>
                 </div>
            </div>
        </div>
    `;

    return div.firstElementChild;
}