import pyautogui
import os
import time 
import cv2
import sys

#open visual studio
def OpenVisual():
    VisualFound = None
    VisualPath = os.path.join(os.getcwd(), "VisualIcon.png")

    pyautogui.press('win')
    time.sleep(1)
    pyautogui.typewrite('visual studio')
    time.sleep(1)

    timeout = time.time() + 5  # Set a timeout of 5 seconds

    # Check if the file exists and is a valid image
    if not os.path.exists(VisualPath):
        print(f"Error: The file {VisualPath} does not exist.")
        sys.exit()
    elif not cv2.imread(VisualPath) is not None:
        print(f"Error: The file {VisualPath} is not a valid image or cannot be read.")
        sys.exit()
    else:
        while VisualFound is None:
            try:
                VisualFound = pyautogui.locateOnScreen(VisualPath,confidence=0.7)
                if VisualFound is not None:
                    pyautogui.click(VisualFound)
                    time.sleep(3)

                if time.time() > timeout:
                    print("Timed out: Visual not found")
                    break
            except Exception as e:
                print(f"Error: {e}")


def CloseVisual():
    pyautogui.hotkey('alt','f4')


Extensions = {
            "clangd" : "clangdIcon.png",
            "c++ testmate" : "TestmateIcon.png",
            "c++ helper" : "CHelperIcon.png",
            "cmake" : "CmakeIcon.png",
            "cmake tools" : "CmakeToolsIcon.png"
            }

#check the extensions
def CheckExtension():
    ClearPath=os.path.join(os.getcwd(), "clearsearchextension.png")
    InstalledPath=os.path.join(os.getcwd(), "InstalledIcon.png")
    UninstalledPath=os.path.join(os.getcwd(), "ToinstallIcon.png")
    UninstalledPath_=os.path.join(os.getcwd(), "ToinstallIcon_.png")

    if not os.path.exists(InstalledPath):
        print(f"Error: The file {InstalledPath} does not exist.")
    elif not os.path.exists(UninstalledPath):
        print(f"Error: The file {UninstalledPath} does not exist.")
    elif not os.path.exists(UninstalledPath_):
        print(f"Error: The file {UninstalledPath_} does not exist.")
    elif not os.path.exists(ClearPath):
        print(f"Error: The file {ClearPath} does not exist.")
    else:
        pyautogui.hotkey('ctrl','shift','x')
        for extension in Extensions.keys():
            ExtensionFound = None
            InstalledExtension = None

            ExtensionPath=os.path.join(os.getcwd(), Extensions[extension])
            timeout = time.time() + 5  # Set a timeout of 5 seconds
            print(f"searching for extension {Extensions[extension]}")
            pyautogui.typewrite(extension)
            time.sleep(3)

            # Check if the file exists and is a valid image
            if not os.path.exists(ExtensionPath):
                print(f"Error: The file {ExtensionPath} does not exist.")
            elif not cv2.imread(ExtensionPath) is not None:
                print(f"Error: The file {ExtensionPath} is not a valid image or cannot be read.")
            else:
                while ExtensionFound is None:
                    try:
                        ExtensionFound = pyautogui.locateOnScreen(ExtensionPath,confidence=0.7)
                        if ExtensionFound is not None:
                            pyautogui.click(ExtensionFound)
                            try:
                                InstalledExtension = pyautogui.locateOnScreen(UninstalledPath,confidence=0.9)
                                if InstalledExtension is not None:
                                    print(f"{Extensions[extension]} will be installed")
                                    pyautogui.click(InstalledExtension)
                            except:
                                    InstalledExtension = pyautogui.locateOnScreen(UninstalledPath_,confidence=0.9)
                                    if InstalledExtension is not None:
                                        print(f"{Extensions[extension]} will be installed")
                                        pyautogui.click(InstalledExtension) 
                        if time.time() > timeout:
                            print(f"Timed out: {ExtensionPath} not found")
                            break
                    except Exception as e:
                        if ExtensionFound is not None:
                            if (InstalledExtension is None) and (pyautogui.locateOnScreen(InstalledPath,confidence=0.7) is not None):
                                print(f"{Extensions[extension]} is already installed")
                        else:
                            print(f"Error: {e}")


            pyautogui.click(pyautogui.locateOnScreen(ClearPath,confidence=0.7))
            pyautogui.hotkey('ctrl','a')
            pyautogui.press('del')

OpenVisual()
CheckExtension()
CloseVisual()
