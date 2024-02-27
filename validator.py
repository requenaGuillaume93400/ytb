from typing import List, Tuple
from os.path import exists

class Validator():
    def __init__(self, OPTIONS_LIST: Tuple[str, str, str, str, str]) -> None:
        self.OPTIONS_LIST = OPTIONS_LIST

    # Private functions
    def help_requested(self, argv: List[str]) -> None:
        if(self.OPTIONS_LIST[-1] in argv):
            print("To define in which folder the downloaded content will spawn, update the 'TO_FOLDER_PATH' const in main.py")
            print("The first argument is the file main_py at the root of the project.")
            print("The second argument is the .txt file where you store all the youtube links you want to download.")
            print("The third argument is the option. Available option are : single_audio, single_video, playlist_audio, playlist_video")
            print("Example : python main.py C:\\full_path\\vids\download_me.txt single_audio")
            exit(0)

    def invalid_number_arguments(self, argv: List[str]) -> None:
        if len(argv) != 3:
            raise ValueError("Invalid number of arguments.")

    def invalid_extension(self, txt_file_path: str) -> None:
        if not txt_file_path.endswith(".txt"):
            raise ValueError("It seems that the file you gave is not a .txt file.")

    def unexistant_file(self, txt_file_path: str) -> None:
        if not exists(txt_file_path):
            raise ValueError("The .txt file you gave does not exist.")

    def invalid_option(self, argv: List[str]) -> None:
        if argv[2] not in self.OPTIONS_LIST:
            raise ValueError("The options you gave is invalid (valid options : single_video, single_audio, playlist_video, playlist_audio).")

    # Public function
    def handle_errors(self, argv: List[str]) -> None:
        self.help_requested(argv)
        self.invalid_number_arguments(argv)
        self.invalid_extension(argv[1])
        self.unexistant_file(argv[1])
        self.invalid_option(argv)
