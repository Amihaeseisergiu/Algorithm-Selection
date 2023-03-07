export function get(id) {
    return document.getElementById(id);
}

export function click(element, action) {
    element.addEventListener("click", action);
}