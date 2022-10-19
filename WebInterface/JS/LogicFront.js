function navigate(path) {
    window.location = path
}


eel.expose(render_output)

function render_output(value) {
    document.getElementById("output").innerText = value
    console.log(value)
}