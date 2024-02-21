#Class to expose the API to the front end
import re
import json
import os
from .data_types import *
from .user_settings import Settings
class ApiExpose:
    path = ""
    debug = True
    test_locations = []



    def test(self):
        user_settings = Settings()
        user_settings.fetch().verify().save()
        self.path = user_settings.user_settings.project_path
        self.get_wild_encounters()
        #sreverse pokemon just to see if its backwards
        #self.write_wild_encounters(self.test_locations[::-1])





    #Function to set what version of the game the API will be reading from
    def set_path(self, path):
        self.path = path
        if path != None:
            self.init_data()
        
    def init_data(self):
        print("Initializing data")
        with open(os.path.join(self.path, "src/data/pokemon/base_stats.h"), "r") as bsf:
            bsf = bsf.readlines()
        for i in range(len(bsf)):
            bsf[i] = re.sub(r'\s','',bsf[i])
        #parse line by line, save species name and parse all stats until next species is encountered
        #to be completed later since missing features from OG editor got pushed to the top of the priority list
            
    def get_wild_encounters(self):
        locations = []
        with open(os.path.join(self.path, "src/data/wild_encounters.json"),"r") as js:
            js = json.load(js)
        wildEncounters = js["wild_encounter_groups"][0]["encounters"]
        #todo could  be eefractored but low priority
        for enc in wildEncounters:
            name = enc["map"]
            loc = Location(name)
            encounters_type_list = (
                    ("land_mons", "land"),
                    ("water_mons", "water"),
                    ("honey_mons", "honey"),
                    ("hidden_mons", "hidden"),
                    ("rock_smash_mons", "rock")
                )
            for encounter_type in encounters_type_list:
                field_in = encounter_type[0]
                field_out = encounter_type[1]
                if not field_in in enc:
                    continue
                field_mons = enc[field_in]
                setattr(loc, field_out + "R", field_mons["encounter_rate"])
                mons = []
                for mon in field_mons["mons"]:
                    mons.append(Encounter(mon["min_level"],mon["max_level"],mon["species"]).__dict__)
                setattr(loc, field_out, mons)
                locations.append(loc.__dict__)
        self.test_locations = locations
        return json.dumps(locations)


    #locations is a list of Location objects
    def write_wild_encounters(self, locations):
        with open(os.path.join(self.path, "src/data/wild_encounters.json"),"r") as js:
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
            
           


    