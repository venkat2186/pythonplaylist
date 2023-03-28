class SongNode:
    def __init__(self, song, user):
        self.song = song
        self.user = user
        self.next = None
        self.prev = None