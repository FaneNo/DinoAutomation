
import time
import pyautogui
from PIL import ImageGrab, ImageOps

#coordinate for the restart button
restart = (1282, 778 )

#the coordinate of the left side of the dino and the right side
dino = (10, 795, 175, 980)   

def image():
    #find the box that only have the dino in it
    box = (dino[0] + 350, dino[1], dino[2] + 350, dino[3] - 45)
    img = ImageGrab.grab(box)
    #convert the image to grayscale
    grayScale = ImageOps.grayscale(img)
    #get the color
    b = grayScale.getcolors()
    #sum the tuple number up from the getcolors function
    a = sum(map(sum, b))
    return a
      
def main():
    pyautogui.click(restart)
    while True:
        #continously capture the state of the game
        image()
        #if the image sum is not value 23355 from the capture box jump
        if(image() != 23355):
            pyautogui.keyDown('space')
            time.sleep(0.001)
            pyautogui.keyUp('space')
            time.sleep(0.001)
            
if __name__ == "__main__":
    main()           