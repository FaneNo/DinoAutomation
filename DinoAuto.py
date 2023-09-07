import time
import pyautogui
from PIL import ImageGrab

def click(key):
    pyautogui.keyDown(key)
    return

while True:  # for infinity loop
    # capture image in black & white format
    image = ImageGrab.grab().convert('L')   
    data = image.load()
    # Draw the rectangle for birds
    for i in range(530, 560):
        for j in range(100, 125):
            data[i, j] = 171
      
    for i in range(5, 500):
        for j in range(130, 200):
            data[i, j] = 0
    image.show()
    break
                  
            


# def isCollision(data):
# # Check colison for birds
#     for i in range(530,560):
#         for j in range(80, 127):
#             if data[i, j] < 171:
#                 click("down")
#                 return
#  # Check colison for cactus
#     for i in range(530, 620):
#         for j in range(130, 160):
#             if data[i, j] < 100:
#                 click("up")
#                 return
#     return

# if __name__ == "__main__":
#     time.sleep(5)
#     click('up') 
    
#     while True:
#         image = ImageGrab.grab().convert('L')  
#         data = image.load()
#         isCollision(data)
