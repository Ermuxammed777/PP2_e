import pygame
import os
import time

class MusicPlayer:
    def __init__(self, music_dir="music"):
        pygame.mixer.init()
        self.tracks = self._load_tracks(music_dir)
        self.index = 0
        self.playing = False
        self.paused = False
        self.start_time = 0
        self.elapsed = 0

    def _load_tracks(self, music_dir):
        if not os.path.exists(music_dir):
            os.makedirs(music_dir)
        exts = (".mp3", ".wav", ".ogg")
        tracks = [os.path.join(music_dir, f)
                  for f in sorted(os.listdir(music_dir))
                  if f.lower().endswith(exts)]
        if not tracks:
            print("Нет треков в папке music/")
        return tracks

    def play(self):
        if not self.tracks:
            return
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
            self.start_time = time.time() - self.elapsed
        else:
            pygame.mixer.music.load(self.tracks[self.index])
            pygame.mixer.music.play()
            self.start_time = time.time()
            self.elapsed = 0
        self.playing = True

    def pause(self):
        if self.playing and not self.paused:
            pygame.mixer.music.pause()
            self.elapsed = time.time() - self.start_time
            self.paused = True
            self.playing = False

    def toggle_play(self):
        if self.playing:
            self.pause()
        else:
            self.play()

    def stop(self):
        pygame.mixer.music.stop()
        self.playing = False
        self.paused = False
        self.elapsed = 0

    def next_track(self):
        self.stop()
        self.index = (self.index + 1) % len(self.tracks)
        self.play()

    def prev_track(self):
        self.stop()
        self.index = (self.index - 1) % len(self.tracks)
        self.play()

    def get_position(self):
        if self.playing:
            return time.time() - self.start_time
        return self.elapsed

    def current_name(self):
        if not self.tracks:
            return "Нет треков"
        return os.path.basename(self.tracks[self.index])

    def status(self):
        if self.playing: return "▶  PLAYING"
        if self.paused:  return "⏸  PAUSED"
        return "⏹  STOPPED"

    def is_finished(self):
        return (self.playing and
            not pygame.mixer.music.get_busy() and
            not self.paused)