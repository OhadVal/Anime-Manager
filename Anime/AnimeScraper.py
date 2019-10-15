from bs4 import BeautifulSoup
from Anime.UtilFunctions import *
import os
import wget

class AnimeScraper:
    def __init__(self):
        self.url = "http://www.anime1.com/watch/"
        self.folder_path = safely_get_folder_path(os.path.dirname(os.path.dirname(__file__)) + '/Animes/')

    def get_episode(self, anime, episode):
        episode_video_link = self.__get_episode_video_link(anime, episode)
        file_path = self.folder_path + anime.title + ' Episode ' + str(episode)
        print('Downloading ' + anime.title + '\'s New Episode!')
        wget.download(episode_video_link, out=file_path)

    def get_multiple_episodes(self, anime, start, end):
        if (start > 1) and (anime.last_episode_aired <= end):
            for i in range(start, end + 1):
                self.get_episode(anime, i)

    def get_last_episode_number(self, anime):
        links = self.__get_episodes_list(anime)
        return max([int(link.text.split('Episode')[1]) for link in links
                    if (link.text.split('Episode')[1][1:]).isdigit()])

    def __get_episode_url(self, anime, episode):
        return self.url + anime.url_name + "/episode-" + str(episode)

    def __get_episode_video_link(self, anime, episode):
        src = simple_get(self.__get_episode_url(anime, episode))
        soup = BeautifulSoup(src, 'lxml')
        file = soup.findAll("script")
        episode_link = [eps for eps in file if "file" in eps.text]
        link = episode_link[0].text.split('file:')[1].split(',')[0].replace("\"", "")[1:]
        return link.replace("\"", "")

    def __get_episodes_list(self, anime):
        episodes_url = self.url + anime.url_name
        src = simple_get(episodes_url)
        soup = BeautifulSoup(src, 'lxml')
        links = soup.find_all("a")[1:]
        show_links = [s for s in links if anime.url_name in s.attrs['href']]
        for i in range(0, len(show_links)):
            if show_links[i].attrs['href'].endswith('episode-1'):
                index = i
                break
        episode_links = [l for l in show_links[index:] if 'episode-' in l.attrs['href']]
        return episode_links
