from Anime.Anime import *
import io
import json
from Anime import UtilFunctions
import os

class AnimeDB:
    def __init__(self):
        self.file_path = UtilFunctions.safely_get_folder_path(os.path.dirname(os.path.dirname(__file__))) + '/data.json'
        self.file_data = {}
        self.data = {}
        self.startup_check()
        
    # make sure there's a file to work with
    def startup_check(self):
        if not (os.path.isfile(self.file_path) and os.access(self.file_path, os.R_OK)):
            print("Either file is missing or is not readable, creating file...")
            with io.open(os.path.join(self.file_path), 'w+') as db_file:
                db_file.write(json.dumps({'anime': [], 'tv_show': []}))

        print("File exists and is readable")
        with open(self.file_path) as f_in:
            self.file_data = json.load(f_in)

        self.__json_to_dict()

    def __json_to_dict(self):
        for anime in self.file_data['anime']:
            self.data[anime['title']] = Anime.from_dict(anime)

    def data_to_list(self):
        lst = []
        for anime in self.data:
            lst.append(dict(self.data[anime]))
        return lst


    def update(self):
        data = self.data_to_list()
        self.file_data['anime'] = data
        try:
            json_file = open(self.file_path, "w+")
            json_file.write(json.dumps(self.file_data))
            json_file.close()
        except IOError:
            print("Action failed!")

    def add(self, anime_dict):
        if anime_dict['title'] in self.data:
            return "Anime Already Exists!"
        else:
            if anime_dict['title'] == '' or anime_dict['last_episode_watched'] == '':
                return "Must enter all fields!"
            else:
                anime = Anime.from_dict(anime_dict)
                self.data[anime.title] = anime
                self.update()
                return 'Anime successfully added!'

    def delete(self, anime_to_delete):
        if anime_to_delete.title not in self.data:
            return "Show Doesn't Exist!"
        else:
            del self.data[anime_to_delete.title]
            self.update()
            return 'Show deleted successfully'
