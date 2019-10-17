import tkinter as tk
import UserInterface.Style
import Anime.AnimeManager as AnimeManager
from tkinter import messagebox
from tkinter import font

anime_manager = AnimeManager.AnimeManager()


class MyApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for frame in (StartPage, AddPage, DownloadPage, UpdatePage):
            new_frame = frame(container, self)
            self.frames[frame] = new_frame
            new_frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


def display_main_menu(my_frame, controller):
    home_button = tk.Button(my_frame, text="Home",
                            command=lambda: controller.show_frame(StartPage), font=UserInterface.Style.SMALL_FONT)
    add_button = tk.Button(my_frame, text="Add",
                           command=lambda: controller.show_frame(AddPage), font=UserInterface.Style.SMALL_FONT)
    remove_button = tk.Button(my_frame, text="Remove",
                              command=lambda: controller.show_frame(StartPage), font=UserInterface.Style.SMALL_FONT)
    update_button = tk.Button(my_frame, text="Update",
                              command=lambda: controller.show_frame(UpdatePage), font=UserInterface.Style.SMALL_FONT)
    download_button = tk.Button(my_frame, text="Download",
                                command=lambda: controller.show_frame(DownloadPage),
                                font=UserInterface.Style.SMALL_FONT)

    home_button.place(relx=0.18)
    add_button.place(relx=0.303)
    remove_button.place(relx=0.401)
    update_button.place(relx=0.553)
    download_button.place(relx=0.691)


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Home", font=UserInterface.Style.LARGE_FONT)
        label.place(relx=0.45, rely=0.1)
        display_main_menu(self, controller)

        new_episodes_button = tk.Button(self, text="Download New Episodes",
                                        command=self.download_new_episodes, font=UserInterface.Style.MEDIUM_FONT)
        new_episodes_button.place(relx=0.26, rely=0.4, relwidth=0.54, relheight=0.1)

        # var2 = tk.StringVar()
        # animes = var2.set(anime_manager.animeNames())
        lb = tk.Listbox(self, font=font.Font(size=15))
        scrollbar = tk.Scrollbar(lb, orient="vertical")
        scrollbar.config(command=lb.yview())
        scrollbar.place(relx=0.97, relheight=1.0, bordermode="inside")
        for anime in anime_manager.animeNames():
            lb.insert(tk.END, anime)
        lb.place(relx=0.20, rely=0.6, relwidth=0.66, relheight=0.3)

    def download_new_episodes(self):
        message = anime_manager.download_new_episodes()
        messagebox.showinfo("Finished!", message)


class AddPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add New Anime", font=UserInterface.Style.LARGE_FONT)
        label.place(relx=0.35, rely=0.1)

        display_main_menu(self, controller)

        # Buttons
        add_button = tk.Button(self, text="Add", bg=UserInterface.Style.BUTTON_COLOR,
                               command=self.add_button_clicked)

        # Inputs
        self.title_input = tk.Entry(self, width=50, font=UserInterface.Style.SMALL_FONT)
        self.last_episode_watched_input = tk.Entry(self, width=50, font=UserInterface.Style.SMALL_FONT)

        # Labels
        title = tk.Label(self, text="Anime:", font=UserInterface.Style.MEDIUM_FONT)
        last_episode_watched = tk.Label(self, text="Last Episode Watched:", font=UserInterface.Style.MEDIUM_FONT)

        # Place
        title.place(rely=0.4)
        self.title_input.place(rely=0.5, relwidth=0.8, relheight=0.1)
        last_episode_watched.place(rely=0.6)
        self.last_episode_watched_input.place(rely=0.7, relwidth=0.8, relheight=0.1)
        add_button.place(rely=0.88, relwidth=1, relheight=0.12)

    def add_button_clicked(self):
        title = self.title_input.get()
        last_episode_watched = self.last_episode_watched_input.get()
        answer = anime_manager.add({"title": title, "last_episode_watched": last_episode_watched})
        messagebox.showinfo("Message", answer)


class RemovePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Home", font=UserInterface.Style.LARGE_FONT)
        label.pack(pady=10, padx=10)

        display_main_menu(self, controller)


class UpdatePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Update", font=UserInterface.Style.LARGE_FONT)
        label.place(relx=0.43, rely=0.1)
        display_main_menu(self, controller)

        # Dropdown List
        variable = tk.StringVar(self)
        variable.set("Default")
        anime_dropdown = tk.OptionMenu(self, variable, "one", "two", "three")

        # Labels
        last_episode_watched_label = tk.Label(self, text="Last Episode Watched:", font=UserInterface.Style.MEDIUM_FONT)
        last_episode_downloaded_label = tk.Label(self, text="Last Episode Downloaded:",
                                                 font=UserInterface.Style.MEDIUM_FONT)
        anime_to_update_label = tk.Label(self, text="Anime:", font=UserInterface.Style.MEDIUM_FONT)

        # Inputs
        last_episode_watched_input = tk.Entry(self, width=50, font=UserInterface.Style.SMALL_FONT)
        last_episode_downloaded_input = tk.Entry(self, width=50, font=UserInterface.Style.SMALL_FONT)

        # Buttons
        update_button = tk.Button(self, text="Update", bg=UserInterface.Style.BUTTON_COLOR)

        # Place
        anime_to_update_label.place(rely=0.25)
        anime_dropdown.place(rely=0.25, relx=0.15, relwidth=0.2, relheight=0.09)
        last_episode_watched_label.place(rely=0.4)
        last_episode_watched_input.place(rely=0.5, relwidth=0.8, relheight=0.1)
        last_episode_downloaded_label.place(rely=0.6)
        last_episode_downloaded_input.place(rely=0.7, relwidth=0.8, relheight=0.1)
        update_button.place(rely=0.88, relwidth=1, relheight=0.12)


class DownloadPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Download", font=UserInterface.Style.LARGE_FONT)
        label.place(relx=0.42, rely=0.1)

        display_main_menu(self, controller)

        # Dropdown List
        animes = anime_manager.animeNames()
        self.choice = animes[0]
        variable = tk.StringVar(self)
        variable.set(animes[0])
        anime_dropdown = tk.OptionMenu(self, variable, *animes, command=self.get_choice)

        # Buttons
        download_button = tk.Button(self, text="Download", bg=UserInterface.Style.BUTTON_COLOR,
                                    command=self.download_button_clicked)

        # Inputs
        self.specific_episode_input = tk.Entry(self, width=50, font=UserInterface.Style.SMALL_FONT)
        self.from_episode_input = tk.Entry(self, width=20, font=UserInterface.Style.SMALL_FONT)
        self.to_episode_input = tk.Entry(self, width=20, font=UserInterface.Style.SMALL_FONT)

        # Labels
        title_label = tk.Label(self, text="Anime:", font=UserInterface.Style.MEDIUM_FONT)
        specific_episode_label = tk.Label(self, text="Download a Single Episode:", font=UserInterface.Style.MEDIUM_FONT)
        from_episode_label = tk.Label(self, text="Or Episodes From:", font=UserInterface.Style.MEDIUM_FONT)
        to_episode_label = tk.Label(self, text="To:", font=UserInterface.Style.MEDIUM_FONT)

        # Place
        anime_dropdown.place(relx=0.15, rely=0.35, relwidth=0.2, relheight=0.09)
        title_label.place(rely=0.35)
        specific_episode_label.place(rely=0.55)
        self.specific_episode_input.place(relx=0.53, rely=0.55, relwidth=0.1)
        from_episode_label.place(rely=0.7)
        self.from_episode_input.place(relx=0.35, rely=0.7, relwidth=0.1)
        to_episode_label.place(relx=0.5, rely=0.7)
        self.to_episode_input.place(relx=0.58, rely=0.7, relwidth=0.1)

        download_button.place(rely=0.88, relwidth=1, relheight=0.12)

    def get_choice(self, value):
        self.choice = value

    def download_button_clicked(self):
        single_episode = self.specific_episode_input.get()
        from_episode = self.from_episode_input.get()
        to_episode = self.to_episode_input.get()

        if single_episode == "" and (from_episode == "" or to_episode == ""):
            messagebox.showinfo("Error!", "Please enter the episode/episodes you wish to download!")

        else:
            anime = anime_manager.db.find(self.choice)

            # Download single episode
            if single_episode != "":
                single_episode = int(single_episode)
                response = anime_manager.download_episode(anime, single_episode)

            # Download multiple episodes
            else:
                from_episode = int(from_episode)
                to_episode = int(to_episode)
                response = anime_manager.download_multiple_episodes(anime, from_episode, to_episode)

        messagebox.showinfo("Error!", response)

        # Reset to default
        self.specific_episode_input.delete(0, tk.END)
        self.from_episode_input.delete(0, tk.END)
        self.to_episode_input.delete(0, tk.END)

    def validate_episode(self, anime, episode):
        if 0 < episode <= anime.last_episode_aired:
            return True
        return False