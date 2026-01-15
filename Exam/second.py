# I just thought deque might be a good option
from collections import deque

# We can use for the playlist the queue sicne its FIFO
# and for history we can use LIFO.

playlist = deque()
history = []

while True:
    print("\n1. Add Song")
    print("2. Play Next")
    print("3. View Current Song Year")
    print("4. Play Previous")
    print("5. View Status")
    print("6. Exit")
    choice = input("What option?").strip()

    # A. add_song(song_title, song_year)
    # Input: A string (e.g., "Infestis"), followed by an integer (e.g., 2025).
    # Can be 2 separate inputs, or both in one if you feel like dealing with string methods.
    # Action: Adds the song and the year to the end of the Playlist as a list (adds [“Infestis”, 2025] to the Playlist).
    # Output: Print "Added [Song, Year] to queue."
    if choice == "1":
        title = input("Song title: ").strip()
        year = int(input("Song year: ").strip())
        song = [title, year]
        playlist.append(song)
        print(f"Added {song} to queue.")

    # B. play_next()
    # Action:
    # Check if the Playlist is empty. If yes, print "No songs in queue."
    # If not empty:
    # Remove the first song from the Playlist.
    # Add that song to the top of the History.
    # Print "Now Playing: [Song Name]".
    elif choice == "2":
        if not playlist:
            print("No songs in queue")
        else:
            song = playlist.popleft()  # front dequeue
            history.append(song)       # push to history
            print(f"Now Playing: {song[0]}")


    # C. view_song_year()
    # Action:
    # Check if the History is empty. If yes, print "No song is playing."
    # If not empty:
    # Access the song year from the top of the stack without returning it, and print the year.
    # Print “The song was released in [Year].”
    elif choice == "3":
        if not history:
            print("No song is playing.")
        else:
            current_song = history[-1]  # peek top of stack
            print(f"The song was released in {current_song[1]}.")

    # D. play_previous() (The "Back" Button)
    # Action:
    # Check if the History is empty. If yes, print "No history available."
    # If not empty:
    # Remove the most recent song from the History.
    # Insert it back at the start (front) of the Playlist (so it plays next).
    # Print "Rewinding to: [Song Name]".
    elif choice == "4":
        if not history:
            print("No history available")
        else:
            song = history.pop()        # pop
            playlist.appendleft(song)   # put back to the front
            print(f"Rewinding to: {song[0]}")


    # E. view_status()
    # Action: Use a Loop to iterate through and print all items currently in the History and the Playlist.
    elif choice == "5":
        print("\nPlaylist:")
        if not playlist:
            print("  (it's empty)")
        else:
            for i, song in enumerate(playlist, start=1):
                print(f"  {i}. {song[0]} ({song[1]})")

        print("History:")
        if not history:
            print("  (it's empty)")
        else:
            for i, song in enumerate(history, start=1):
                print(f"  {i}. {song[0]} ({song[1]})")

    elif choice == "6":
        print("Done!")
        break

    else:
        print("wrong choice.")


"""
Exam/ $ python3 second.py

1. Add Song
2. Play Next
3. View Current Song Year
4. Play Previous
5. View Status
6. Exit
What option?1
Song title: Test
Song year: 2020
Added ['Test', 2020] to queue.

1. Add Song
2. Play Next
3. View Current Song Year
4. Play Previous
5. View Status
6. Exit
What option?1
Song title: john
Song year: 2018
Added ['john', 2018] to queue.

1. Add Song
2. Play Next
3. View Current Song Year
4. Play Previous
5. View Status
6. Exit
What option?2
Now Playing: Test

1. Add Song
2. Play Next
3. View Current Song Year
4. Play Previous
5. View Status
6. Exit
What option?5

Playlist:
  1. john (2018)
History:
  1. Test (2020)

1. Add Song
2. Play Next
3. View Current Song Year
4. Play Previous
5. View Status
6. Exit
What option?4
Rewinding to: Test

1. Add Song
2. Play Next
3. View Current Song Year
4. Play Previous
5. View Status
6. Exit
What option?5

Playlist:
  1. Test (2020)
  2. john (2018)
History:
  (it's empty)

1. Add Song
2. Play Next
3. View Current Song Year
4. Play Previous
5. View Status
6. Exit
What option?2
Now Playing: Test

1. Add Song
2. Play Next
3. View Current Song Year
4. Play Previous
5. View Status
6. Exit
What option?5

Playlist:
  1. john (2018)
History:
  1. Test (2020)

1. Add Song
2. Play Next
3. View Current Song Year
4. Play Previous
5. View Status
6. Exit
What option?
"""
