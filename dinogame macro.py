import time
import pyautogui
from PIL import ImageGrab, ImageOps
from numpy import *

replaybtn = (480,500)
din = (185,520)
tree_position = (240, 540)

def restartGame():
    pyautogui.click(replaybtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')

def imageGrab():
    box = (din[0] + 80, din[1], din[0] + 120, din[1] + 30 )
    image = ImageGrab.grab(box)
    grayImage =ImageOps.grayscale(image)
    a = array(grayImage.getcolors())

    return a.sum()

def main():
    restartGame()
    while True:
        if(imageGrab() != 1447 ):
            pressSpace()

main()

