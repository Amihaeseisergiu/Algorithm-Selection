import {get, setData} from "../utils/dom.js";

export function addAlgorithmSelectionPanel() {
    get('algorithm-selection').innerHTML = `
        <div class="flex flex-col items-center w-full popIn py-1"
             x-data="{selected: false}"
             id="algorithm-selection-parent">
            <div class="flex flex-row items-center text-2xl w-full font-semibold rounded-2xl border-2 border-solid border-gray-300
                 text-neutral-400 py-2 px-4 my-2 cursor-pointer duration-500 hover:border-rose-400
                 hover:text-neutral-500 hover:scale-[1.02] hover:shadow-xl"
                 :class="selected ? 'shadow-xl text-neutral-500 border-rose-400 scale-[1.02]' : 'shadow'"
                 @click="selected = !selected">
                <div>
                    Algorithm Selection
                </div>
                <div id="algorithm-selection-spinner"
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
                 flex flex-col items-left"
                 x-ref="algorithm_selection_container"
                 id="algorithm-selection-results"
                 :style="selected ? 'max-height: ' + 
                 ($refs.algorithm_selection_container.scrollHeight > 0 ? $refs.algorithm_selection_container.scrollHeight : 350) + 'px' : ''">
            </div>
        </div>
    `;
}

export function addAlgorithmSelectionResults(data) {
    if ('error' in data['header']) {
        get('algorithm-selection-results').innerHTML = `
            <div class="w-full p-5 text-2xl font-semibold text-neutral-500">
                ${data['header']['error']}
            </div>
        `;
    } else {
        get('algorithm-selection-results').innerHTML = `
            <div class="w-full flex flex-col p-5">
                <div class="p-1 text-2xl font-semibold text-neutral-500 flex flex-row">
                    Selected library:
                    <div class="text-rose-400 ml-2">
                        ${data['payload']['library']}
                    </div>
                </div>
                <div class="p-1 text-2xl font-semibold text-neutral-500 flex flex-row">
                    Selected algorithm:
                    <div class="text-rose-400 ml-2">
                        ${data['payload']['algorithm']}
                    </div>
                </div>
            </div>
        `;
    }

    setData("algorithm-selection-parent", "selected", true);
    get("algorithm-selection-spinner").remove();
}