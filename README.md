# Recently Played Store

## Description
Recently Played Store is a Python script that creates an in-memory store for recently played songs that can accommodate N songs per user, with a fixed initial capacity. It allows you to store a list of song-user pairs and fetch recently played songs based on the user. When the store becomes full, it automatically eliminates the least recently played songs.

## Getting Started

These instructions will guide you on how to run the Recently Played Store on your local machine.

## Prerequisites

To run the script, you'll need:

Python 3.x installed on your local machine
A code editor such as Visual Studio Code, PyCharm, or Sublime Text

## Installing

1. Clone this repository to your local machine.
```git clone https://github.com/venkat2186/pythonplaylist.git ```

2. Change the current directory to the cloned repository.
```cd recently-played-store ```

3. Install the required packages by running the following command.
```pip install -r requirements.txt ```

## Running the script
1. Open the Python script in your preferred code editor.
2. Create a new instance of the RecentlyPlayedStore class with the desired initial capacity and max songs per user.
```store = RecentlyPlayedStore(initial_capacity, max_songs_per_user)```

3. Use the play_song method to add a new song to the store for a user.
```store.play_song(song, user)```

4. Use the recently_played method to fetch the recently played songs for a user.
```store.recently_played(user)```

## Running the tests
1. Open the terminal or command prompt.
2. Change the current directory to the cloned repository.
```cd recently-played-store```
3. Run the tests using the following command.
```pytest```

## Authors
venkateshbabu, venkatbalasundaram3@gmail.com

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
