#Class to expose the API to the front end
import re
import json
import os
from .data_types import *
class ApiExpose:
    path = ""
    debug = True
    test_locations = []



    def test(self):
        self.path = "C:\\Users\\Jadiel\\Desktop\\decomps\\eliteredux\\"
        self.get_wild_encounters()
        #sreverse pokemon just to see if its backwards
        self.write_wild_encounters(self.test_locations[::-1])





    #Function to set what version of the game the API will be reading from
    def set_path(self, path):
        self.path = path
        if path != None:
            self.init_data()
        
    def init_data(self):
        print("Initializing data")
        with open(self.path + "src\\data\\pokemon\\base_stats.h", "r") as bsf:
            bsf = bsf.readlines()
        for i in range(len(bsf)):
            bsf[i] = re.sub(r'\s','',bsf[i])
        #parse line by line, save species name and parse all stats until next species is encountered
        #to be completed later since missing features from OG editor got pushed to the top of the priority list
            
    def get_wild_encounters(self):
        locations = []
        with open(self.path + "src\\data\\wild_encounters.json","r") as js:
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
            if "honey_mons" in enc:
                honeymons = enc["honey_mons"]
                Loc.honeyR = honeymons["encounter_rate"]
                mons = []
                for mon in honeymons["mons"]:
                    mons.append(Encounter(mon["min_level"],mon["max_level"],mon["species"]))
                Loc.honey = mons
                locations.append(Loc)
            if "honey_mons" in enc:
                honeymons = enc["honey_mons"]
                Loc.honeyR = honeymons["encounter_rate"]
                mons = []
                for mon in honeymons["mons"]:
                    mons.append(Encounter(mon["min_level"],mon["max_level"],mon["species"]))
                Loc.honey = mons
                locations.append(Loc)
            if "hidden_mons" in enc:
                hiddenmons = enc["hidden_mons"]
                Loc.hiddenR = hiddenmons["encounter_rate"]
                mons = []
                for mon in hiddenmons["mons"]:
                    mons.append(Encounter(mon["min_level"],mon["max_level"],mon["species"]))
                Loc.hidden = mons
                locations.append(Loc)
            if "rock_smash_mons" in enc:
                rockmons = enc["rock_smash_mons"]
                Loc.rockR = rockmons["encounter_rate"]
                mons = []
                for mon in rockmons["mons"]:
                    mons.append(Encounter(mon["min_level"],mon["max_level"],mon["species"]))
                Loc.rock = mons
                locations.append(Loc)
        self.test_locations = locations
        return locations


    #locations is a list of Location objects
    def write_wild_encounters(self, locations):
        with open(self.path + "src\\data\\wild_encounters.json","r") as js:
            js = json.load(js)
        #wildEncounters = js["wild_encounter_groups"][0]["encounters"]
        wildEncounters = []
        for loc in locations:
            enc = {}
            enc["map"] = loc.name
            if loc.land != None:
                landmons = {}
                landmons["encounter_rate"] = loc.landR
                mons = []
                for mon in loc.land:
                    mons.append({"min_level":mon.min,"max_level":mon.max,"species":mon.species})
                landmons["mons"] = mons
                enc["land_mons"] = landmons
            if loc.water != None:
                watermons = {}
                watermons["encounter_rate"] = loc.waterR
                mons = []
                for mon in loc.water:
                    mons.append({"min_level":mon.min,"max_level":mon.max,"species":mon.species})
                watermons["mons"] = mons
                enc["water_mons"] = watermons
            if loc.honey != None:
                honeymons = {}
                honeymons["encounter_rate"] = loc.honeyR
                mons = []
                for mon in loc.honey:
                    mons.append({"min_level":mon.min,"max_level":mon.max,"species":mon.species})
                honeymons["mons"] = mons
                enc["honey_mons"] = honeymons
            if loc.hidden != None:
                hiddenmons = {}
                hiddenmons["encounter_rate"] = loc.hiddenR
                mons = []
                for mon in loc.hidden:
                    mons.append({"min_level":mon.min,"max_level":mon.max,"species":mon.species})
                hiddenmons["mons"] = mons
                enc["hidden_mons"] = hiddenmons
            if loc.rock != None:
                rockmons = {}
                rockmons["encounter_rate"] = loc.rockR
                mons = []
                for mon in loc.rock:
                    mons.append({"min_level":mon.min,"max_level":mon.max,"species":mon.species})
                rockmons["mons"] = mons
                enc["rock_smash_mons"] = rockmons
            wildEncounters.append(enc)
        js["wild_encounter_groups"][0]["encounters"] = wildEncounters
        if self.debug:
            curdir = os.getcwd()
            with open(curdir + "\\back\\tests\\test.json","w") as file:
                json.dump(js,file,indent=4)
        else:
            with open(self.path + "src\\data\\wild_encounters.json","w") as file:
                json.dump(js,file,indent=4)
            
           


    