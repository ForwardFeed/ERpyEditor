#Class to expose the API to the front end
import re
import json
import os
from PIL import Image
from .data_types import *
from .user_settings import Settings
class ApiExpose:
    path = ""
    debug = True
    test_locations = []
    species =[] #list of CompactSpecies objects
    workingdir = os.getcwd()


    def test(self):
        
        user_settings = Settings()
        user_settings.fetch().verify().save()
        self.path = user_settings.user_settings.project_path
        self.get_sprites()
        #print(self.workingdir)
        





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
        name_r = re.compile(r"\[(?P<NAME>SPECIES_\w*)\]")
        for i in range(len(bsf)):
            if name_r.match(bsf[i]):
                name = name_r.match(bsf[i]).group("NAME")
                spe = CompactSpecies(name)
                spe.name = self.stripName(name)
                self.species.append(spe)

            
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
            
           
    def get_trainer_teams(self):
        trainers = {}
        with open(os.path.join(self.path, "src/data/trainer_parties.h"),"r") as lines:
            lines = lines.readlines()
        
    def stripName(self, name):
        name = name.replace("SPECIES_","")
        name = name.lower().split("_")
        for i in range(len(name)):
            name[i] = name[i].capitalize()
        return " ".join(name)

    def get_sprites(self):
        sprites = {}
        old_sprites = set()
        gp = self.path + "\\graphics\\pokemon\\"
        for root, dirs, files in os.walk(os.path.join(self.workingdir +"\\front\\sprites")):
            for file in files:
                if file.endswith(".png"):
                    old_sprites.add(file)
        for dir in os.listdir(os.path.join(gp)):
            if not os.path.isdir(os.path.join(gp + dir)):
                continue
            for ls in os.listdir(os.path.join(gp + dir)):
                if ls == "front.png" and dir.upper() + ".png" not in old_sprites:
                    img = Image.open(os.path.join(gp + dir + "\\front.png"))
                    sprites[dir.upper()] = img
                elif os.path.isdir(os.path.join(gp + dir + "\\" + ls)):
                    for file in os.listdir(os.path.join(gp + dir + "\\" + ls)):
                        if file == "front.png" and dir.upper() + "_" + ls.upper() + ".png" not in old_sprites:
                            img = Image.open(os.path.join(gp + dir + "\\" + ls + "\\front.png"))
                            sprites[dir.upper() + "_" + ls.upper()] = img
        for key in sprites:
            img = sprites[key]
            img.save(os.path.join(self.workingdir +"\\front\\sprites\\" + key + ".png"))




    