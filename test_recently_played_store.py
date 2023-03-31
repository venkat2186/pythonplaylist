from RecentlyPlayedStore import RecentlyPlayedStore


def test_RecentlyPlayedSongs():

 # creating a recent playlist with capacity of 3
    obj_rp = RecentlyPlayedStore(3,3,2)

    obj_rp.play_song(user_id="user1", song_id="song1", timestamp=1.0)
    obj_rp.play_song(user_id="user1", song_id="song2", timestamp=2.0)
    obj_rp.play_song(user_id="user1", song_id="song3", timestamp=3.0)

    obj_rp.play_song(user_id="user2", song_id="song1", timestamp=4.0)

    obj_rp.play_song(user_id="user1", song_id="song4", timestamp=5.0)
    obj_rp.play_song(user_id="user1", song_id="song2", timestamp=6.0)

    user1_recently_played = obj_rp.recently_played("user1")
    print(user1_recently_played)

    user2_recently_played = obj_rp.recently_played("user2")
    print(user2_recently_played)