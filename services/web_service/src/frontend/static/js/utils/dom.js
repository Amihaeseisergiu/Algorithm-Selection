export function get(id) {
    return document.getElementById(id);
}

export function click(element, action) {
    element.addEventListener("click", action);
}

export function changed(element, action) {
    element.addEventListener("change", action);
}

export function getData(element, data) {
    if (get(element)._x_dataStack) {
        return get(element)._x_dataStack[0][data];
    }

    return undefined;
}