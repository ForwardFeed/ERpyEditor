from dataclasses import dataclass
import os.path
import json
import crossfiledialog

DEFAULT_PATH_SAVE = "user_setttings.json"

@dataclass
class UserSettings:
    project_path: str
    def __init__(self) -> None:
        self.project_path = ""
    
    def from_json(self, json_data):
        print(json_data)
        for field in json_data:
            #may thow here and cause issues where an unknown field to be added
            setattr(self, field, json_data[field])
        return self

# user settings
class Settings:
    user_settings: UserSettings
    def __init__(self) -> None:
        self.user_settings = UserSettings()

    def fetch(self):
        if os.path.isfile(DEFAULT_PATH_SAVE):
            with open(DEFAULT_PATH_SAVE, 'r') as file:
                file_data = file.read()
                # may throw here and cause a massive breaking bug if the data isn't a valid json file
                file_jsonified = json.loads(file_data)
                self.user_settings = UserSettings().from_json(file_jsonified)
        else:
            self.save()
        return self
        
    # recurively ask you for the right path
    # a bit agressive tho
    def verify(self):
        if not self.user_settings.project_path:
            self.user_settings.project_path = crossfiledialog.choose_folder("please, choose the pokeemerald project folder")
            return self.verify()
        if not os.path.isdir(self.user_settings.project_path):
            self.user_settings.project_path = crossfiledialog.choose_folder("please, choose the pokeemerald project folder")
            return self.verify()
        #make checks if it's it a valid elite_redux, could be a better check that said
        if not os.path.isfile(os.path.join(self.user_settings.project_path, "elite-redux-title-screen.png")):
            self.user_settings.project_path = crossfiledialog.choose_folder("please, choose a valid elite-redux folder")
            return self.verify()
        return self
    
    def save(self):
        with open(DEFAULT_PATH_SAVE, 'w') as file:
            file.write(json.dumps(self.user_settings.__dict__))
        return self
        


if __name__ == '__main__':
    user_settings = Settings()
    user_settings.fetch().verify().save()

    print(user_settings)