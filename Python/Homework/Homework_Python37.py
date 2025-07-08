#Task 1. Воспроизведение мультимедиа
#Создайте два класса:
#AudioFileMixin — требует наличие поля audio_tracks (список треков).
#Метод play_audio() выводит:
#Воспроизведение аудио для <НазваниеКласса>:
#<название трека>
#<название трека>
# Если нужное поле отсутствует — выбрасывайте AttributeError.

# VideoFileMixin — требует наличие поля video_files (список видео).
# Метод play_video() выводит:
# Воспроизведение видео для <НазваниеКласса>:
# <название видео>
# <название видео>
# Если нужное поле отсутствует — выбрасывайте AttributeError.


'''Task 2 Устройства
Создайте два класса:
MediaPlayer — поддерживает только аудио. Принимает список треков.
Laptop — поддерживает аудио и видео. Принимает списки треков и видео.
Проверьте работу классов, вызвав методы воспроизведения.
Данные:
tracks = ["track1.mp3", "track2.mp3"]
movies = ["movie.mp4", "trailer.mov"]

Пример вывода:
Воспроизведение аудио для MediaPlayer:
track1.mp3
track2.mp3
Воспроизведение аудио для Laptop:
track1.mp3
track2.mp3

Воспроизведение видео для Laptop:
movie.mp4
trailer.mov
'''

'''
Mixin — это способ добавить функциональность к классу без дублирования кода. Они:
- не создают сами по себе экземпляров
- не имеют собственной логики инициализации
- просто добавляют поведение
'''


class AudioFileMixin:
    def play_audio(self):
        if not hasattr(self, "audio_tracks"):
            raise AttributeError(f"{self.__class__.__name__} должен иметь поле 'audio_tracks'")
        print(f"Воспроизведение аудио для {self.__class__.__name__}:")
        for track in self.audio_tracks:
            print(f"\t{track}")

class VideoFileMixin:
    def play_video(self):
        if not hasattr(self, "video_files"):
            raise AttributeError(f"{self.__class__.__name} должен иметь поле 'video_files'")
        print(f"Воспроизведение видео для {self.__class__.__name__}:")
        for file in self.video_files:
            print(f"\t{file}")

# only audio_tracks
class MediaPlayer(AudioFileMixin):
    def __init__(self, audio_tracks):
        self.audio_tracks = audio_tracks

# Класс Laptop наследует оба миксина.
# Это значит:
# у него есть метод play_audio() от AudioFileMixin
# и метод play_video() от VideoFileMixin
class Laptop(AudioFileMixin, VideoFileMixin):
    def __init__(self, audio_tracks, video_files):
        self.audio_tracks = audio_tracks
        self.video_files = video_files

#class Laptop(VideoFileMixin):
#    def __init__(self):
#        self.audio_tracks = ["track4.mp3"]
        #self.video_files = video_files


# main code
tracks = ["track1.mp3", "track2.mp3"]
movies = ["movie.mp4", "trailer.mov"]
#Ошибки инициируются внутри миксинов —
# это логично, потому что они знают, что им нужно.
#Ошибки обрабатываются снаружи,
# чтобы не прерывать всю программу.

# Создание устройств
mp3_player = MediaPlayer(tracks)
#mp3_player = MediaPlayer()
laptop = Laptop(tracks, movies)
#laptop = Laptop() #Error play_video: 'Laptop' object has no attribute 'play_audio'

try:
    mp3_player.play_audio()
except AttributeError as e:
    print("Error play_audio:", e)


try:
    laptop.play_audio()
    laptop.play_video()
except AttributeError as e:
    print("Error play_video:", e)




