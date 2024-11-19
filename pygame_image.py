import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん") #ウィンドウのタイトル
    screen = pg.display.set_mode((800, 600)) #ウィンドウのサイズ
    clock  = pg.time.Clock() #フレームレート調整
    bg_img = pg.image.load("fig/pg_bg.jpg") #背景surfaceを作成（今回は背景）
    tori_img = pg.image.load("fig/3.png") #こうかとんのsurfaceを作成
    tori_img = pg.transform.flip(tori_img, True, False) #こうかとんsurfaceを左右反転　変数(画像（surface）, 左右反転, 上下反転)
    bghanten_img = pg.transform.flip(bg_img, True, False) #背景surfaceを左右反転
    tmr = 0 #時間カウンター(while1回で1増加)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return #✕ボタンを押したら終了

        size = 1600
        x = -(tmr%(size*2))

        screen.blit(bg_img, [x, 0]) #screen surfaceに背景画像surfaceを貼り付ける（blit→貼り付け）、[横, 縦]で位置指定
        screen.blit(bghanten_img, [x+size, 0])
        screen.blit(bg_img, [x+(size*2), 0]) 
        screen.blit(bghanten_img, [x+(size*3), 0])

        screen.blit(tori_img, [300, 200]) #screen surfaceにこうかとんsurfaceを貼り付ける

        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()