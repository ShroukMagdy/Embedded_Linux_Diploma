import pyautogui
import os
import time 
import cv2
import sys

def ClickOnImage(ImageName):
    ImageFound = None
    ImagePath = os.path.join(os.getcwd(), ImageName)
    timeout = time.time() + 5  # Set a timeout of 5 seconds
    # Check if the file exists and is a valid image
    if not os.path.exists(ImagePath):
        print(f"Error: The file {ImagePath} does not exist.")
        sys.exit()
    elif not cv2.imread(ImagePath) is not None:
        print(f"Error: The file {ImagePath} is not a valid image or cannot be read.")
        sys.exit()
    else:
        while ImageFound is None:
            try:
                ImageFound = pyautogui.locateOnScreen(ImagePath,confidence=0.7)
                if ImageFound is not None:
                    pyautogui.click(ImageFound)
                    time.sleep(3)

                if time.time() > timeout:
                    print("Timed out: Browser not found")
                    break
            except Exception as e:
                print(f"Error: {e}")
                sys.exit()

#open browser studio
def OpenBrowser():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.typewrite('edge')
    time.sleep(1)

    ClickOnImage("EdgeIcon.png")


def CloseBrowser():
    pyautogui.hotkey('alt','f4')

def OpenGmail():
    pyautogui.write("https://mail.google.com/mail/u/0/?hl=ar#inbox")
    pyautogui.press('enter')
    time.sleep(10)

    ClickOnImage("SelectIcon.png")
    ClickOnImage("UnReadIcon.png")
    ClickOnImage("MarkReadIcon.png")
    

OpenBrowser()
OpenGmail()
CloseBrowser()