import { hydrate } from './hydrate.js'
import { saveToLocalstorage, fetchFromLocalstorage } from './settings.js';
/**
 * To select which version of the game data to have
 */
/**@type {import('./compactify.js').CompactGameData} */
export let gameData, compareData;

// each time the data is modified, this is updated
// so the client checks if it have the latest version by checking lo
const LATEST_DATA_VERSION = "1"/*%%VERSION%%*/

const allVersions = [
    "1.6.1",
    "Alpha",
]
const defaultVersion = "1.6.1"

function setAvailableVersion(){
    
}

function changeVersion(version){
    
}

export function setupDataVersionning(){
    fetch(`js/data/gameDataV1.6.1.json`)
        .then((response) => response.json())
        .then((data) => {
            console.log("took gamedata from server")
            gameData = data
            hydrate()
    })
}

