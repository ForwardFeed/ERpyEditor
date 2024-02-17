#Class to expose the API to the front end
import re
class ApiExpose:
    path = ""


    

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
            




    