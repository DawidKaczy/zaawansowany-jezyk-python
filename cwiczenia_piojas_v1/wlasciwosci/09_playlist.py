class Playlist:
    def __init__(self, songs):
        self.__songs = songs


    @property
    def songs(self):
        return self.__songs.copy()

    @songs.setter
    def songs(self, songs):
        if not songs: raise TypeError("songs cannot be None")
        if not isinstance(songs, list):
            raise TypeError('songs must be a list')
        for song in songs:
            if not isinstance(song, str) or len(song.strip()) == 0:
                raise TypeError('songs must be a string i nie może byc pusty')
        self.__songs = songs.copy()

    def __repr__(self):
        return 'Playlist(songs={})'.format(self.songs)

v1 = Playlist(["Wielki bu", "Kronkel dom"])
print(v1)
v1.songs = [] #if not songs: raise TypeError("songs cannot be None")
print(v1)

