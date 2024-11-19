import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん") #ウィンドウのタイトル
    screen = pg.display.set_mode((800, 600)) #ウィンドウのサイズ
    clock  = pg.time.Clock() #フレームレート調整
    bg_img = pg.image.load("fig/pg_bg.jpg") #画像を読み込む関数（今回は背景）

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return #✕ボタンを押したら終了
        screen.blit(bg_img, [100, 0]) #screen surfaceに背景画像surfaceを貼り付ける（blit→貼り付け）、[横, 縦]で位置指定
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()