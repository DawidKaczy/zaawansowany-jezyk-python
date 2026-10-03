

class Playlist:
    def __init__(self, songs):
        self.songs = songs

    @property
    def songs(self):
        return self.__songs.copy()

    @songs.setter
    def songs(self, songs):
        if not isinstance(songs, list):
            raise TypeError("songs must be a list")
        for song in songs:
            if not isinstance(song, str):
                raise TypeError("song must be a string")
            if not song.strip():
                raise ValueError("song cannot be empty")
        self.__songs = songs.copy()


v1 = Playlist([])




