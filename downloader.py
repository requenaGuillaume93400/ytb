from pytube import YouTube, contrib

class Downloader():
    def __init__(self, TO_FOLDER_PATH: str) -> None:
        self.TO_FOLDER_PATH = TO_FOLDER_PATH

    # Private functions
    def download(self, link: str, audio: bool) -> None:
        youtube = YouTube(link)

        if(audio):
            media = youtube.streams.get_audio_only()
        else:
            media = youtube.streams.get_highest_resolution()
        
        media.download(self.TO_FOLDER_PATH)

    def download_playlist(self, link: str, audio: bool) -> None:
        playlist = contrib.playlist.Playlist(link)
        medias = playlist.videos

        for media in medias:
            print("Downloading : " + media.title)

            if(audio):
                media = media.streams.get_audio_only()
            else:
                media = media.streams.get_highest_resolution()
            
            media.download(self.TO_FOLDER_PATH)

    # Public functions
    def download_video(self, link: str) -> None:
        self.download(link, False)

    def download_audio(self, link: str) -> None:
        self.download(link, True)

    def download_playlist_video(self, link: str) -> None:
        self.download_playlist(link, False)

    def download_playlist_audio(self, link: str) -> None:
        self.download_playlist(link, True)
