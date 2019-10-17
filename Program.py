from UserInterface.GUI import *


def main():
    # App Settings
    app = MyApp()
    app_width = app.winfo_screenwidth() / 2.8
    app_height = app.winfo_screenheight() / 2.8
    app_size_str = str(int(app_width)) + 'x' + str(int(app_height))
    app.geometry(app_size_str)
    app.title("Anime Manager")
    app.mainloop()


if __name__ == "__main__":
    main()


