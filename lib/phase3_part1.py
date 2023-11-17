class Track:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def matches(self, keyword):
        return keyword.lower() in (self.title.lower(), self.artist.lower())


class MusicLibrary:
    def __init__(self):
        self.tracks = []

    def add(self, track):
        if isinstance(track, Track):
            self.tracks.append(track)

    def search(self, keyword):
        return [track for track in self.tracks if track.matches(keyword)]