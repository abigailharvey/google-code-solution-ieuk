"""A video player class."""
from __future__ import print_function
from .video_library import VideoLibrary
from operator import attrgetter
from random import randint
from .video_playlist import Playlist


class VideoPlayer:
    """A class used to represent a Video Player."""
    
    def __init__(self):
        self._video_library = VideoLibrary()
        
    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        alphabetical = sorted(self._video_library.get_all_videos(), key=attrgetter("title"))
        print("Here's a list of all available videos:")
        for video in alphabetical:
            tags = video.tags #use this to format the tuple 
            tag_list = []
            for tag in tags:
                tag_list.append(tag)
            tag_list_print = str(tag_list).replace('\'', '').replace(',', '')
            print(video.title, ("({})".format(video.video_id)), tag_list_print)

    
    currently_playing = ""
    paused_video = ""
    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        
        self.paused_video = ""
        new_vid = self._video_library.get_video(video_id)
        if new_vid == None:
            print("Cannot play video: Video does not exist")
        elif self.currently_playing == "":
            self.currently_playing = new_vid
            print("Playing video:", self.currently_playing.title)
        elif self.currently_playing != "":
            print("Stopping video:", self.currently_playing.title )
            self.currently_playing = new_vid
            print("Playing video:", self.currently_playing.title )
        


    def stop_video(self):
        """Stops the current video."""
        self.paused_video = ""
        if self.currently_playing == "":
            print("Cannot stop video: No video is currently playing")
            self.currently_playing = ""
        else:
            print("Stopping video:", self.currently_playing.title)
            self.currently_playing = ""

    def play_random_video(self):
        """Plays a random video from the video library."""
        self.paused_video = ""
        if self.currently_playing != "":
            print("Stopping video:", self.currently_playing.title)
            self.currently_playing = ""
        
        if len(self._video_library.get_all_videos()) == 0:
            print("No videos available")
        else:
            random_index = randint(0,len(self._video_library.get_all_videos())-1)
            rand_vid = self._video_library.get_all_videos()[random_index]
            self.currently_playing = rand_vid
            print("Playing video:", self.currently_playing.title)

    def pause_video(self):
        """Pauses the current video."""
        if self.currently_playing == "":
            print("Cannot pause video: No video is currently playing")
        elif self.currently_playing == self.paused_video:
            print("Video already paused:", self.paused_video.title)
        else:
            self.paused_video = self.currently_playing
            print("Pausing video:", self.paused_video.title)

        

    def continue_video(self):
        """Resumes playing the current video."""
        if self.currently_playing == "":
            print("Cannot continue video: No video is currently playing")
        elif self.paused_video == "":
            print("Cannot continue video: Video is not paused")
        else:
            self.paused_video = ""
            print("Continuing video:", self.currently_playing.title)


    def show_playing(self):
        """Displays video currently playing."""
        
        if self.currently_playing == "":
            print("No video is currently playing")
        elif self.paused_video == "":
            tags = self.currently_playing.tags #use this to format the tuple 
            tag_list = []
            for tag in tags:
                tag_list.append(tag)
            tag_list_print = str(tag_list).replace('\'', '').replace(',', '')
            print("Currently playing:", self.currently_playing.title, ("({})".format(self.currently_playing.video_id)), tag_list_print )
        else:
            tags = self.currently_playing.tags #use this to format the tuple 
            tag_list = []
            for tag in tags:
                tag_list.append(tag)
            tag_list_print = str(tag_list).replace('\'', '').replace(',', '')
            print("Currently playing:", self.currently_playing.title, ("({})".format(self.currently_playing.video_id)), tag_list_print, "- PAUSED")


    playlist_collection = []
    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_exists = ""
        if self.playlist_collection != []:
            for playlists in self.playlist_collection:
                if playlists._playlist_name.upper() == playlist_name.upper():
                    playlist_exists = True
            if playlist_exists == True:
                print("Cannot create playlist: A playlist with the same name already exists")
            else:
                self.playlist_collection.append(Playlist(playlist_name))
                print("Successfully created new playlist:", playlist_name)
        else:
            self.playlist_collection.append(Playlist(playlist_name))
            print("Successfully created new playlist:", playlist_name)


    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        playlist_exists = ""
        for playlists in self.playlist_collection:
            if playlist_name.upper() == playlists._playlist_name.upper():
                playlist_exists = True
                playlist_selected = playlists
        if playlist_exists != True:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
        
        vid_exists = ""
        if playlist_exists == True:
            for vid in self._video_library.get_all_videos():
                if video_id == vid.video_id:
                    vid_exists = True
            if vid_exists != True:
                print(f"Cannot add video to {playlist_name}: Video does not exist")
        
        vid_in_playlist = ""
        if vid_exists == True and playlist_exists == True:
            for videos in playlist_selected._playlist_videos:
                if videos.video_id == video_id:
                    vid_in_playlist = True
            if vid_in_playlist == True:    
                print(f"Cannot add video to {playlist_name}: Video already added")
            else:
                playlist_selected._playlist_videos.append(self._video_library.get_video(video_id))
                print(f"Added video to {playlist_name}:", self._video_library.get_video(video_id).title )


    def show_all_playlists(self):
        """Display all playlists."""
        if self.playlist_collection == []:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            alphabet_playlists = sorted(self.playlist_collection, key=attrgetter("_playlist_name"))
            for item in alphabet_playlists:
                print("\t"+item._playlist_name)
                
                
    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_exists = ""
        if self.playlist_collection == []:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
        else:
            for playlist in self.playlist_collection:
                if playlist._playlist_name.upper() == playlist_name.upper():
                    playlist_exists = True
                    selected_playlist = playlist
            if playlist_exists != True:
                print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
            else:
                print("Showing playlist:", playlist_name)
                if selected_playlist._playlist_videos == []:
                    print("\t"+"No videos here yet")
                else:
                    for video in selected_playlist._playlist_videos:
                        tags = video.tags #use this to format the tuple 
                        tag_list = []
                        for tag in tags:
                            tag_list.append(tag)
                        tag_list_print = str(tag_list).replace('\'', '').replace(',', '')
                        print(self._video_library.get_video(video.video_id).title,("({})".format(self._video_library.get_video(video.video_id).video_id)), tag_list_print )


    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        playlist_exists = ""
        for playlists in self.playlist_collection:
            if playlist_name.upper() == playlists._playlist_name.upper():
                playlist_exists = True
                selected_playlist = playlists
        if playlist_exists != True:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
        
        vid_exists = ""
        if playlist_exists == True:
            for vid in self._video_library.get_all_videos():
                if video_id == vid.video_id:
                    vid_exists = True
            if vid_exists != True:
                print(f"Cannot remove video from {playlist_name}: Video does not exist")
        
        vid_in_playlist = ""
        if vid_exists == True and playlist_exists == True:
            for videos in selected_playlist._playlist_videos:
                if videos.video_id == video_id:
                    vid_in_playlist = True
            if vid_in_playlist == True: 
                selected_playlist._playlist_videos.remove(self._video_library.get_video(video_id))
                print(f"Removed video from {playlist_name}:", self._video_library.get_video(video_id).title )           
                
            else:
                print(f"Cannot remove video from {playlist_name}: Video is not in playlist")


    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_exists = ""
        for playlists in self.playlist_collection:
            if playlist_name.upper() == playlists._playlist_name.upper():
                playlist_exists = True
                selected_playlist = playlists
        if playlist_exists != True:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
        
        if playlist_exists == True:
            if selected_playlist._playlist_videos != []:
                for videos in selected_playlist._playlist_videos:
                    selected_playlist._playlist_videos.remove(self._video_library.get_video(videos.video_id))
                    print("Successfully removed all videos from:", playlist_name )
            else:
                print(f"Cannot clear playlist {playlist_name}: Playlist is empty")
   

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_exists = ""
        for playlists in self.playlist_collection:
            if playlist_name.upper() == playlists._playlist_name.upper():
                playlist_exists = True
                selected_playlist = playlists
        if playlist_exists != True:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
        
        if playlist_exists == True:
            self.playlist_collection.remove(selected_playlist)
            print("Deleted playlist:", playlist_name)



    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        videos_featuring = []
        vid_selected = ""
        for vids in self._video_library.get_all_videos():
            if search_term.upper() in vids.title.upper():
                videos_featuring.append(vids)
        if videos_featuring == []:
            print("No search results for", search_term)
        else:
            alphabet_videos_featuring = sorted(videos_featuring, key=attrgetter("title"))
            print(f"Here are the results for {search_term}:")
            for vids in alphabet_videos_featuring:
                tags = vids.tags #use this to format the tuple 
                tag_list = []
                for tag in tags:
                    tag_list.append(tag)
                tag_list_print = str(tag_list).replace('\'', '').replace(',', '')
                print(f"\t{alphabet_videos_featuring.index(vids)+1})", vids.title, ("({})".format(vids.video_id)), tag_list_print)
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            vid_index_selected = input()
            if vid_index_selected.isdigit():
                vid_index = int(vid_index_selected)
                for vids in alphabet_videos_featuring:
                    if vid_index == (alphabet_videos_featuring.index(vids)+1):
                        self.play_video(vids.video_id)
                        
    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        videos_featuring = []
        vid_selected = ""
        for vids in self._video_library.get_all_videos():
            if video_tag.lower() in vids.tags:
                videos_featuring.append(vids)
        if videos_featuring == []:
            print("No search results for", video_tag)
        else:
            alphabet_videos_featuring = sorted(videos_featuring, key=attrgetter("title"))
            print(f"Here are the results for {video_tag}:")
            for vids in alphabet_videos_featuring:
                tags = vids.tags #use this to format the tuple 
                tag_list = []
                for tag in tags:
                    tag_list.append(tag)
                tag_list_print = str(tag_list).replace('\'', '').replace(',', '')
                print(f"\t{alphabet_videos_featuring.index(vids)+1})", vids.title, ("({})".format(vids.video_id)), tag_list_print)
            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            vid_index_selected = input()
            if vid_index_selected.isdigit():
                vid_index = int(vid_index_selected)
                for vids in alphabet_videos_featuring:
                    if vid_index == (alphabet_videos_featuring.index(vids)+1):
                        self.play_video(vids.video_id)

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
