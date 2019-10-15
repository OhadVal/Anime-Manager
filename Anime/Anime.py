import re

class Anime:
    def __init__(self, title, last_episode_watched):
        self.title = title
        self.url_name = ''.join(re.findall(r'[A-Za-z0-9 -]+', title)).replace(' ', '-').lower()
        self.last_episode_watched = last_episode_watched
        self.last_episode_aired = 0
        self.last_episode_downloaded = last_episode_watched

    @classmethod
    def from_dict(cls, anime_dict):
        anime = Anime(anime_dict['title'], anime_dict['last_episode_watched'])
        return anime

    def __iter__(self):
        yield 'title', self.title
        yield 'last_episode_watched', self.last_episode_watched
        yield 'last_episode_aired', self.last_episode_aired
        yield 'last_episode_downloaded', self.last_episode_downloaded
        yield 'url_name', self.url_name
