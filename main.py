from pytube.exceptions import VideoUnavailable
from sys import argv
from downloader import Downloader
from validator import Validator
from typing import List

# Insert your folder path here in TO_FOLDER_PATH
TO_FOLDER_PATH = r"..\vids"
YOUTUBE_BASE_URL = "https://www.youtube.com/"

SINGLE_VIDEO_OPTION = "single_video"
SINGLE_AUDIO_OPTION = "single_audio"
PLAYLIST_VIDEO_OPTION = "playlist_video"
PLAYLIST_AUDIO_OPTION = "playlist_audio"
HELP_OPTION = "help"
OPTIONS_LIST = (SINGLE_VIDEO_OPTION, SINGLE_AUDIO_OPTION, PLAYLIST_VIDEO_OPTION, PLAYLIST_AUDIO_OPTION, HELP_OPTION)

# Private Functions
def verify_link(element: str) ->str:
    if(YOUTUBE_BASE_URL in element):
        return element.strip()
    else:
        raise ValueError(element + " is not a valid youtube media link.")

def list_links(path_to_txt_file: str) -> List[str]:
    try:
        with open(path_to_txt_file, 'r') as file:
            content = file.readlines()
            list = [verify_link(element) for element in content]
            return list
    except FileNotFoundError:
        print("File not found.")
        return []

# Main Script
if __name__ == "__main__":
    print("==== Work begin ! ====")

    downloader = Downloader(TO_FOLDER_PATH)
    validator = Validator(OPTIONS_LIST)

    validator.handle_errors(argv)
    links = list_links(argv[1])
    option = argv[2]

    for link in links:
        print(link)

        try:
            if option == SINGLE_AUDIO_OPTION:
                downloader.download_audio(link)

            elif option == SINGLE_VIDEO_OPTION:
                downloader.download_video(link)

            elif option == PLAYLIST_VIDEO_OPTION:
                downloader.download_playlist_video(link)

            elif option == PLAYLIST_AUDIO_OPTION:
                downloader.download_playlist_audio(link)
            
        except VideoUnavailable:
            print(f'{link} is unavailable, skipping.')
    
print("==== Job Done ! ====")
