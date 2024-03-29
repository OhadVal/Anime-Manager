from Anime.AnimeScraper import *
from Anime.AnimeDB import *


class AnimeManager:
    def __init__(self):
        self.db = AnimeDB()
        self.scraper = AnimeScraper()

    def download_new_episodes(self):
        self.__update_last_episodes()

        return_message = ''
        # Download new episodes if exist and update DB
        for anime in self.db.data:
            current_anime = self.db.data[anime]
            if int(current_anime.last_episode_downloaded) == (current_anime.last_episode_aired - 1):
                self.scraper.get_episode(current_anime, current_anime.last_episode_aired)
                self.db.data[current_anime.title].last_episode_downloaded = \
                    current_anime.last_episode_aired  # Update data
                self.db.data[current_anime.title].last_episode_watched = \
                    current_anime.last_episode_aired  # Update data
                return_message += str(current_anime.title + 's new episode downloaded!\n')
        self.db.update()  # Update DB
        if return_message == '':
            return_message = 'No New Episodes!'
        return return_message

    def __update_last_episodes(self):
        for anime in self.db.data:
            last_episode_aired = self.scraper.get_last_episode_number(self.db.data[anime])
            if last_episode_aired > self.db.data[anime].last_episode_aired:
                self.db.data[anime].last_episode_aired = last_episode_aired
        self.db.update()

    def download_episode(self, anime, episode):
        if self.validate_episode(anime, episode):
            self.scraper.get_episode(anime, episode)  # Download
            self.db.data[anime.title].last_episode_downloaded = episode  # Update data
            self.db.data[anime.title].last_episode_watched = episode  # Update data
            self.db.update()  # Update DB
            return anime.title + "'s episode " + str(episode) + " downloaded successfully"
        return "Please enter a valid episode"

    def download_multiple_episodes(self, anime, start, end):
        if self.validate_episode(anime, start) and self.validate_episode(anime, end):
            self.scraper.get_multiple_episodes(anime, start, end)  # Download
            self.db.data[anime.title].last_episode_downloaded = end  # Update data
            self.db.data[anime.title].last_episode_watched = end  # Update data
            self.db.update()  # Update DB
            return anime.title + "'s episodes " + str(start) + " to " + str(end) + " downloaded successfully"
        return "Please enter a valid episode"

    def add(self, anime_dict):
        answer = self.db.add(anime_dict)
        return answer

    def delete(self, anime_to_delete):
        return self.db.delete(anime_to_delete)

    def animeNames(self):
        return [name['title'] for name in self.db.data_to_list()]

    def validate_episode(self, anime, episode):
        self.__update_last_episodes()
        if episode < 1 or episode > anime.last_episode_aired:
            return False
        return True

    def update(self, anime, episode):
        if self.db.update_episode(anime, episode):
            return "Anime Updated Successfully!"
        return "Couldn't Update Anime"
