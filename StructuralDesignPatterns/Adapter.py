# дизайн патерн, який дозволяє об'єктам з несумісними інтерфейсами працювати разом.
# Цей патерн діє як міст між двома інтерфейсами, перетворюючи інтерфейс одного класу на інтерфейс, очікуваний клієнтами.
# Адаптер дозволяє класам працювати разом, що інакше не було б можливо через несумісність їхніх інтерфейсів.

# У цьому прикладі AudioPlayer — це клас, який відтворює "mp3" файли. Ми створили MediaAdapter,
# щоб адаптувати AdvancedMediaPlayer до інтерфейсу, який очікує AudioPlayer, дозволяючи відтворювати
# "mp4" та "vlc" файли. Таким чином, за допомогою патерна Адаптер, ми інтегрували
# сторонню функціональність без зміни існуючого коду або інтерфейсу AudioPlayer.


# Сценарії використання:
# Інтеграція зі сторонніми бібліотеками: Коли потрібно використовувати класи зі сторонніх бібліотек,
# інтерфейси яких не відповідають інтерфейсам у вашому проекті.
# Рефакторинг системи: Коли ви хочете змінити частини системи, але не хочете, щоб ці зміни вплинули на існуючих клієнтів.


# Типи Адаптерів:
# Об'єктний адаптер: Використовує композицію для з'єднання інтерфейсів.
# Адаптер містить об'єкт класу, який потребує адаптації, і перенаправляє виклики до цього об'єкта.
# Класовий адаптер: Використовує множинне наслідування для адаптації одного інтерфейсу до іншого.
# Клас адаптера наслідується одночасно від адаптованого класу та цільового інтерфейсу.


class MediaPlayer:
    def play(self, audio_type, file_name):
        if audio_type == "mp3":
            print(f"Playing mp3 file. Name: {file_name}")
        else:
            print("Invalid media. mp3 format supported only")


class AdvancedMediaPlayer:
    def play_vlc(self, file_name):
        print(f"Playing vlc file. Name: {file_name}")

    def play_mp4(self, file_name):
        print(f"Playing mp4 file. Name: {file_name}")


class MediaAdapter:
    def __init__(self, audio_type):
        if audio_type == "vlc":
            self.advanced_music_player = AdvancedMediaPlayer()
            self.play = self.advanced_music_player.play_vlc
        elif audio_type == "mp4":
            self.advanced_music_player = AdvancedMediaPlayer()
            self.play = self.advanced_music_player.play_mp4


class AudioPlayer(MediaPlayer):
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
audio_player.play("avi", "mind me.avi")
