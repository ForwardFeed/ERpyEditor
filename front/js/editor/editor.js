import { overlayEditLocation } from "./locations.js"

/**
 * @type {Array.<Array<RegExp | string, ()=>void>>}
 */
const targetibleMap = [
    [new RegExp("\.stat-"), ()=>{
        console.log('species base stats')
    }], //
    [new RegExp("\.location-"), (ev)=>{
        overlayEditLocation(ev)
    }],
]
/**
 * 
 * @returns {string}
 * @param {HTMLElement} node 
 */
function nodeToTargetible(node){
    let targetible = node.tagName.toLowerCase()
    targetible += "#" + node.id.toLowerCase()
    targetible += "." + node.className
    return targetible
}
/**
 * 
 * @param {Event} ev 
 * @returns 
 */
function onRightClick(ev){
    const node = ev.target
    const targetible = nodeToTargetible(node)
    for (const target of targetibleMap){
        if (!targetible.match(target[0])) continue
        target[1](ev)
    }
}

export function setupEditor(){
    (function( $ ) {
        $.fn.replaceTag = function(newTag) {
          var originalElement = this[0]
          , originalTag = originalElement.tagName
          , startRX = new RegExp('^<'+originalTag, 'i')
          , endRX = new RegExp(originalTag+'>$', 'i')
          , startSubst = '<'+newTag
          , endSubst = newTag+'>'
          , newHTML = originalElement.outerHTML
          .replace(startRX, startSubst)
          .replace(endRX, endSubst);
          this.replaceWith(newHTML);
        };
      })(jQuery);
      
    document.body.oncontextmenu = function() {return false;}
    document.addEventListener("mousedown", function(ev){
        if (ev.button != 2) return
        onRightClick(ev)
    }, true)
}