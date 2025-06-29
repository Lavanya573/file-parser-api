#music library manager
def add_album(library, album_info):
    artist, title, year, songs = album_info
    library[title] = (artist, year, songs)
    return library

def create_playlist(library, song_selections):
    playlist = []
    for album_title, song_title in song_selections:
        if album_title in library:
            _, _, songs = library[album_title]
            if song_title in songs:
                playlist.append(song_title)
    return playlist

def add_song_to_album(library, album_title, new_song):
    if album_title in library:
        artist, year, songs = library[album_title]
        if new_song not in songs:
            songs.append(new_song)
        library[album_title] = (artist, year, songs)
    return library

def remove_song_from_playlist(playlist, song):
    if song in playlist:
        playlist.remove(song)
    return playlist

def display_library(library):
    print("\n--- Music Library ---")
    for title, (artist, year, songs) in library.items():
        print(f"Album: {title}")
        print(f"  Artist: {artist}")
        print(f"  Year: {year}")
        print(f"  Songs: {songs}")
    print()

def display_playlist(playlist):
    print("\n--- Playlist ---")
    print(playlist)
    print()

def main():
    library = {}
    playlist = []
    unique_artists = set()
    genres = set()  # Currently unused but could be extended

    while True:
        print("\n===== Music Library Manager =====")
        print("1. Add a New Album")
        print("2. Create Playlist")
        print("3. Add Song to Album")
        print("4. Remove Song from Playlist")
        print("5. Show Library")
        print("6. Show Playlist")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            artist = input("Enter artist name: ")
            title = input("Enter album title: ")
            year = int(input("Enter release year: "))
            songs = input("Enter songs separated by commas: ").split(",")
            songs = [song.strip() for song in songs]
            album_info = (artist, title, year, songs)
            library = add_album(library, album_info)
            unique_artists.add(artist)
            print("Album added successfully!")

        elif choice == '2':
            song_selections = []
            n = int(input("How many songs do you want to add to the playlist? "))
            for _ in range(n):
                album_title = input("Enter album title: ")
                song_title = input("Enter song title: ")
                song_selections.append((album_title, song_title))
            playlist = create_playlist(library, song_selections)
            print("Playlist created successfully!")

        elif choice == '3':
            album_title = input("Enter album title: ")
            new_song = input("Enter new song to add: ")
            library = add_song_to_album(library, album_title, new_song)
            print("Song added successfully!")

        elif choice == '4':
            song = input("Enter song to remove from playlist: ")
            playlist = remove_song_from_playlist(playlist, song)
            print("Song removed successfully!")

        elif choice == '5':
            display_library(library)

        elif choice == '6':
            display_playlist(playlist)

        elif choice == '7':
            print("Exiting Music Library Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please select between 1 to 7.")

if __name__ == "__main__":
    main()
