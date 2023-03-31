from SongNodeee import SongNode


class RecentlyPlayedStore:
    def __init__(self, initial_capacity, max_songs_per_user, user_id):
        self.capacity = initial_capacity
        self.max_songs_per_user = max_songs_per_user
        self.user_id=user_id
        self.head = None
        self.tail = None
        self.played_songs = {}

    def play_song(self, song, user):
            if user not in self.played_songs:
                self.played_songs[user] = []
            node = SongNode(song, user)
            self.played_songs[user].append(node)
            if self.head is None:
                self.head = node
                self.tail = node
            else:
                node.next = self.head
                self.head.prev = node
                self.head = node
            if len(self.played_songs[user]) > self.max_songs_per_user:
                self.remove_song(self.played_songs[user][0])

    def remove_song(self, node):
            if node.prev is None:
                self.head = node.next
            else:
                node.prev.next = node.next
            if node.next is None:
                self.tail = node.prev
            else:
                node.next.prev = node.prev
            self.played_songs[node.user].remove(node)

    def recently_played(self, user):
            if user not in self.played_songs:
                return []
            return [node.song for node in self.played_songs[user]]
