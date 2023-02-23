import os
from pytube import YouTube
from pytube import Playlist


class Youtube:

    def __init__(self):
        self.path = os.getcwd()
        self.playlist = None
        self.file_type = None

    def input_path(self):
        while True:
            path = input("Location: ")
            try:
                os.chdir(path)
                break
            except:
                print("Invalid Path.")
                continue
        self.path = path

    def input_playlist_url(self):
        while True:
            url = input("Playlist url: ")
            try:
                pl = Playlist(url)
                if pl:
                    self.playlist = pl
                    break
                else:
                    print("This is empty Playlist.")
                    continue
            except:
                print("Invalid URL.")

    def input_file_type(self):
        type_list = {"mp3": "mp3", "0": "mp3",
                     "mp4": "mp4", "1": "mp4"}
        while True:
            file_type = input("mp3[0]/mp4[1]: ")
            if file_type in type_list:
                file_type = type_list[file_type]
                break
            print("Invalid Type.")
        self.file_type = file_type

    def download(self):
        i = 1
        for yt in self.playlist:
            yt = YouTube(yt)
            print(f"{i}:", yt.title)

            if self.file_type == "mp4":
                yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            elif self.file_type == "mp3":
                yt = yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first()

            try:
                yt.download(output_path=self.path, filename=f"{yt.title}.{self.file_type}")
            except:
                yt.download(output_path=self.path, filename=f"Untitle{i}.{self.file_type}")

            i += 1


if __name__ == "__main__":
  youtube = Youtube()

  while True:
    path_setting = input("path setting - True[1], False[0]\n(if you choice False, path is now dir.): ")
    if path_setting in ["1", "0"]:
      youtube.input_path() if int(path_setting) else None
      break
  youtube.input_playlist_url()
  youtube.input_file_type()
  youtube.download()

  print("done.")
  input("Program is finished")