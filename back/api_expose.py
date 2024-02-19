#Class to expose the API to the front end
import re
import json
from .data_types import *
class ApiExpose:
    path = ""


    def test(self):
        self.path = "C:\\Users\\Jadiel\\Desktop\\decomps\\eliteredux\\"
        self.get_wild_encounters()

    #Function to set what version of the game the API will be reading from
    def set_path(self, path):
        self.path = path
        if path != None:
            self.init_data()
        

    

    def init_data(self):
        print("Initializing data")
        with open(self.path + "src//data//pokemon//base_stats.h", "r") as bsf:
            bsf = bsf.readlines()
        for i in range(len(bsf)):
            bsf[i] = re.sub(r'\s','',bsf[i])
        #parse line by line, save species name and parse all stats until next species is encountered
        #to be completed later since missing features from OG editor got pushed to the top of the priority list
            
    def get_wild_encounters(self):
        locations = []
        with open(self.path + "src//data//wild_encounters.json","r") as js:
            js = json.load(js)
        wildEncounters = js["wild_encounter_groups"][0]["encounters"]
        for enc in wildEncounters:
            name = enc["map"]
            Loc = Location(name)
            if "land_mons" in enc:
                landmons = enc["land_mons"]
                Loc.landR = landmons["encounter_rate"]
                mons = []
                for mon in landmons["mons"]:
                    mons.append(Encounter(mon["min_level"],mon["max_level"],mon["species"]))
                Loc.land = mons
                locations.append(Loc)
            if "water_mons" in enc:
                watermons = enc["water_mons"]
                Loc.waterR = watermons["encounter_rate"]
                mons = []
                for mon in watermons["mons"]:
                    mons.append(Encounter(mon["min_level"],mon["max_level"],mon["species"]))
                Loc.water = mons
                locations.append(Loc)
        
        for loc in locations:
            print(loc.name)
            if loc.land != None:
                print(len(loc.land))
            if loc.water != None:
                print(len(loc.water))
            


    