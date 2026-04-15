import pygame
from player import MusicPlayer

def draw_ui(screen, player, fonts, W, H):
    BG     = (20,  20,  35)
    CARD   = (35,  35,  60)
    ACCENT = (127, 119, 221)
    WHITE  = (240, 240, 240)
    GRAY   = (140, 140, 160)
    GREEN  = (50,  200, 130)

    screen.fill(BG)

    # Карточка трека
    pygame.draw.rect(screen, CARD, (40, 40, W-80, 140), border_radius=16)

    # Номер / всего треков
    idx_txt = fonts['sm'].render(
        f"{player.index+1} / {len(player.tracks)}", True, GRAY)
    screen.blit(idx_txt, (60, 56))

    # Название трека
    name = player.current_name()
    name_surf = fonts['md'].render(name[:38], True, WHITE)
    screen.blit(name_surf, (60, 82))

    # Статус
    status_surf = fonts['sm'].render(player.status(), True, GREEN)
    screen.blit(status_surf, (60, 122))

    # Прогресс-бар
    bar_x, bar_y, bar_w, bar_h = 40, 200, W-80, 8
    pygame.draw.rect(screen, CARD,   (bar_x, bar_y, bar_w, bar_h), border_radius=4)
    pos = player.get_position()
    fill = min(pos / 200, 1.0) * bar_w  # 200с макс длина
    if fill > 0:
        pygame.draw.rect(screen, ACCENT,
                         (bar_x, bar_y, int(fill), bar_h), border_radius=4)

    # Время
    mins, secs = divmod(int(pos), 60)
    time_txt = fonts['sm'].render(f"{mins:02d}:{secs:02d}", True, GRAY)
    screen.blit(time_txt, (bar_x, bar_y + 16))

    # Плейлист
    pl_y = 260
    hdr = fonts['sm'].render("PLAYLIST", True, GRAY)
    screen.blit(hdr, (40, pl_y))
    pl_y += 28
    for i, path in enumerate(player.tracks[:6]):
        color = ACCENT if i == player.index else GRAY
        prefix = "▶ " if i == player.index else f"{i+1}. "
        import os
        nm = os.path.basename(path)[:40]
        surf = fonts['sm'].render(prefix + nm, True, color)
        screen.blit(surf, (40, pl_y))
        pl_y += 26

    # Подсказка клавиш
    hints = ["[P] Play/Pause", "[S] Stop", "[N] Next", "[B] Back", "[Q] Quit"]
    hint_y = H - 44
    x = 40
    for h in hints:
        surf = fonts['xs'].render(h, True, (80, 80, 110))
        screen.blit(surf, (x, hint_y))
        x += surf.get_width() + 20

def main():
    pygame.init()
    W, H = 600, 480
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Music Player")
    clock_tick = pygame.time.Clock()

    fonts = {
        'md': pygame.font.SysFont("arial", 22, bold=True),
        'sm': pygame.font.SysFont("arial", 16),
        'xs': pygame.font.SysFont("arial", 13),
    }

    player = MusicPlayer("music")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if   event.key == pygame.K_p: player.toggle_play()
                elif event.key == pygame.K_s: player.stop()
                elif event.key == pygame.K_n: player.next_track()
                elif event.key == pygame.K_b: player.prev_track()
                elif event.key == pygame.K_q: running = False

        # Автопереход к следующему треку
        if player.is_finished() and player.tracks:
            player.next_track()

        draw_ui(screen, player, fonts, W, H)
        pygame.display.flip()
        clock_tick.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()