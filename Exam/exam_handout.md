Programming Task – Music Player

1. The Scenario
You have been hired to create the logic for a new music streaming app. Your job is to build a text-based prototype that manages the song queue and the play history.
You need to maintain two main data structures:
The Playlist: Songs waiting to be played.
The History: Song that is now playing, or ones that have just finished playing.

2. Functional Requirements
Your program must implement the following five functionalities(doesn’t have to be a function) and a main menu loop.

A. add_song(song_title, song_year)
Input: A string (e.g., "Infestis"), followed by an integer (e.g., 2025). Can be 2 separate inputs, or both in one if you feel like dealing with string methods.
Action: Adds the song and the year to the end of the Playlist as a list (adds [“Infestis”, 2025] to the Playlist).
Output: Print "Added [Song, Year] to queue."

B. play_next()
Action:
Check if the Playlist is empty. If yes, print "No songs in queue."
If not empty:
Remove the first song from the Playlist.
Add that song to the top of the History.
Print "Now Playing: [Song Name]".

C. view_song_year()
Action:
Check if the History is empty. If yes, print "No song is playing."
If not empty:
Access the song year from the top of the stack without returning it, and print the year.
Print “The song was released in [Year].”

D. play_previous() (The "Back" Button)
Action:
Check if the History is empty. If yes, print "No history available."

If not empty:
Remove the most recent song from the History.
Insert it back at the start (front) of the Playlist (so it plays next).
Print "Rewinding to: [Song Name]".

E. view_status()
Action: Use a Loop to iterate through and print all items currently in the History and the Playlist.
