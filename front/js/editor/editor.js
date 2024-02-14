

export function setupEditor(){
    document.addEventListener("mousedown", function(ev){
        console.log(ev.button)
        ev.preventDefault()
    }, true)
}