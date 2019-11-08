# from Anime import AnimeManager
import tkinter as tk

def get_anime_list(self):
    animes = self.anime_manager.animeNames()
    if not animes:
        animes = ["Nothing here yet"]
    self.choice = animes[0]
    variable = tk.StringVar(self)
    variable.set(animes[0])
    anime_dropdown = tk.OptionMenu(self, variable, *animes, command=self.get_choice)
    return anime_dropdown
