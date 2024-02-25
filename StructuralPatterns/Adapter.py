# Дизайн патерн, який дозволяє об'єктам з несумісними інтерфейсами працювати разом.
# Цей патерн діє як міст між двома або більшою к-тю інтерфейсів, перетворюючи інтерфейс одного класу на інтерфейс, очікуваний клієнтами.

# У цьому прикладі AudioPlayer — це клас, який відтворює "mp3" файли. Ми створили MediaAdapter,
# щоб адаптувати AdvancedMediaPlayer до інтерфейсу, який очікує AudioPlayer, дозволяючи відтворювати
# "mp4" та "vlc" файли. Таким чином, за допомогою патерна Адаптер, ми інтегрували
# сторонню функціональність без зміни існуючого коду або інтерфейсу AudioPlayer.


# Типи Адаптерів:
# Об'єктний адаптер: Використовує композицію для з'єднання інтерфейсів.
# Адаптер містить об'єкт класу, який потребує адаптації, і перенаправляє виклики до цього об'єкта.
# Класовий адаптер: Використовує множинне наслідування для адаптації одного інтерфейсу до іншого.
# Клас адаптера наслідується одночасно від адаптованого класу та цільового інтерфейсу.


# Перша бібліотека медіа плеєрів
class MediaPlayer:  # Цей медіа плеєр відтворює тільки mp3 файли
    def play(self, audio_type, file_name):
        if audio_type == "mp3":
            print(f"Playing mp3 file. Name: {file_name}")
        else:
            print("Invalid media. mp3 format supported only")


# Друга бібліотека медіа плеєрів


class AdvancedMediaPlayer:  # Цей медіа плеєр відтворює vlc та mp4 файли
    def play_vlc(self, file_name):
        print(f"Playing vlc file. Name: {file_name}")

    def play_mp4(self, file_name):
        print(f"Playing mp4 file. Name: {file_name}")


class MediaAdapter:  # Адаптер для відтворення vlc та mp4 файлів
    def __init__(self, audio_type):
        if audio_type == "vlc":
            self.advanced_music_player = AdvancedMediaPlayer()
            self.play = self.advanced_music_player.play_vlc
        elif audio_type == "mp4":
            self.advanced_music_player = AdvancedMediaPlayer()
            self.play = self.advanced_music_player.play_mp4


class AudioPlayer(MediaPlayer):  # Основний клас, який використовується клієнтами
    def play(self, audio_type, file_name):
        if audio_type == "mp3":
            super().play(audio_type, file_name)
        elif audio_type in ["vlc", "mp4"]:
            adapter = MediaAdapter(audio_type)
            adapter.play(file_name)
        else:
            print("Invalid media. mp3, vlc, mp4 format supported only")


# Клієнтський код
audio_player = AudioPlayer()
audio_player.play("mp3", "beyond the horizon.mp3")
audio_player.play("mp4", "alone.mp4")
audio_player.play("vlc", "far far away.vlc")
# Invalid media. mp3, vlc, mp4 format supported only
audio_player.play("avi", "mind me.avi")
