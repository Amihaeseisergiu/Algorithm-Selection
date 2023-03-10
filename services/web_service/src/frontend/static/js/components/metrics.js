export function createLibraryHTML(libraryName) {
    let div = document.createElement('div');

    div.innerHTML = `
        <div class="flex flex-col w-11/12 bg-white rounded-lg shadow-xl p-4 my-6 divide-y-2 popIn">
            <div class="flex items-center px-2 pb-2 text-2xl font-semibold text-neutral-500">
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

            <div class="flex items-center">
                <div class="grow w-1/2 h-64 mt-4 mx-2 rounded-lg border border-solid border-gray-300">
                    <div class="flex flex-col divide-y-2">
                        <div class="p-1 text-neutral-400 font-semibold flex justify-center">
                            Memory usage over time
                        </div>
                        <div class="h-56">
                            <canvas id="${libraryName}-plot-memory"></canvas>
                        </div>
                    </div>
                </div>

                <div class="grow w-1/2 h-64 mt-4 mx-2 rounded-lg border border-solid border-gray-300">
                    <div class="flex flex-col divide-y-2">
                        <div class="p-1 text-neutral-400 font-semibold flex justify-center">
                            CPU usage over time
                        </div>
                        <div class="h-56">
                            <canvas id="${libraryName}-plot-cpu"></canvas>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;

    return div.firstElementChild;
}