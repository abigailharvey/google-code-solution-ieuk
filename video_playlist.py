"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
 
    #playlist_collection = []

    
    def __init__(self, playlist_name):
        """The Playlist class is initialized."""
        self._playlist_name = playlist_name
        self._playlist_videos = []
        
    def add_playlist(self, playlist_name):    
        Playlist.playlist_collection.append(playlist_name)
        
        
    def get_playlist(self, playlist_name):
        """Returns the playlist object (title, url, tags) from the video library.

        Args:
            video_id: The video url.

        Returns:
            The Video object for the requested video_id. None if the video
            does not exist.
        """
        return self._playlist_videos.get(playlist_name, None)