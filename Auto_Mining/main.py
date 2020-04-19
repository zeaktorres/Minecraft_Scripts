from helperFunctions.Hardware_Input.mouseAndKeyboardPress import allMouseInputs, sendInstruction, stopInstruction, allInstructions
from helperFunctions.Retrieve_SSIM.takeScreenshotHearts import takeScreenshotHearts
from helperFunctions.Retrieve_SSIM.compareImages import compareImages
from helperFunctions.mouseMovement.mouseMovement import lookUp, lookDown, turnLeft, turnRight
from helperFunctions.readTextFromImage.readImageText import detectLava, detectLavaNoQueue
import multiprocessing
import time
from pynput import keyboard
import os
import ctypes
from pynput.keyboard import Key, Controller
THRESHOLD = 0.55
TIMETOMINEBLOCK = 0.95
#Die on ESC
def onPress(key):
    if key == keyboard.Key.esc:
        print("Exiting")
        # Stop listener
        os._exit(1)
        return False

def startUp():
    #Die on ESC  
    listener = keyboard.Listener(
        on_press=onPress)
    listener.start()

    #Wait then reset click
    time.sleep(4)


#Mine block
def mineOneBlock():
    sendInstruction(allInstructions.MINE)
    time.sleep(TIMETOMINEBLOCK)
    stopInstruction(allInstructions.MINE)

def mineBothBlocks():
    mineOneBlock()
    lookDown()
    mineOneBlock()

def moveForwardOneBlock():
    sendInstruction(allInstructions.FORWARD)
    time.sleep(.24)
    stopInstruction(allInstructions.FORWARD)

def retreat():
    keyboard = Controller()
    sendInstruction(allInstructions.BACKWARD)
    print("Running")
    sendInstruction(allInstructions.SPACE)
    time.sleep(5)
    #with keyboard.pressed(Key.alt):
        #sendInstruction(allInstructions.F4); stopInstruction(allInstructions.F4)

def placeTorch(pickAxeNumber, torchNumber):
    turnRight()

    #Choose which torch
    if torchNumber == 1:
        sendInstruction(allInstructions.NINE)
    elif torchNumber == 2:
        sendInstruction(allInstructions.EIGHT)
    elif torchNumber == 3:
        sendInstruction(allInstructions.SEVEN)
    elif torchNumber == 4:
        sendInstruction(allInstructions.SIX)
    elif torchNumber == 5:
        sendInstruction(allInstructions.FIVE)
    
    time.sleep(1)
    sendInstruction(allInstructions.PLACE_TORCH)
    time.sleep(.1)
    stopInstruction(allInstructions.PLACE_TORCH)
    turnLeft()

    #Choose which pickaxe
    if pickAxeNumber == 1:
        sendInstruction(allInstructions.ONE)   
    elif pickAxeNumber == 2:
        sendInstruction(allInstructions.TWO)
    elif pickAxeNumber == 3:
        sendInstruction(allInstructions.THREE)
    elif pickAxeNumber == 4:
        sendInstruction(allInstructions.FOUR)
    elif pickAxeNumber == 5:
        sendInstruction(allInstructions.FIVE)
    time.sleep(.5) 
def scanForLava(number):
    ctypes.windll.user32.mouse_event(0x0001 , 0, number * -1, 0, 0)
    if (detectLavaNoQueue(2)):
        retreat()
        lava = True
        break
    ctypes.windll.user32.mouse_event(0x0001 , 0, number, 0, 0)


if __name__ == "__main__":
    startUp()
    lava = False
    sendInstruction(allInstructions.MINE)
    stopInstruction(allInstructions.MINE)
    pickAxeNumber = 1
    torchNumber = 1
    torchesPlaced = 0
    counter = 0
    while 1 == 1:
        
        
        #Determine pickaxe number
        counter += 1
        if counter > 100:
            counter = 0
            pickAxeNumber += 1
        if torchesPlaced >= 64:
            torchesPlaced = 0
            torchNumber += 1


        detectLavaNoQueue(0)

        #Screenshot Hearts 1
        takeScreenshotHearts(0)
        
        #Take screenshot and detect if lava
        queue_lava = multiprocessing.Queue()
        thread1 = multiprocessing.Process(target=detectLava, args=(queue_lava,1,))
        thread1.start()

        #Mining
        mineBothBlocks()

        #Screenshot Hearts 2
        takeScreenshotHearts(1)

        #Compare screenshots of hearts
        queue_screenshot = multiprocessing.Queue()
        thread2 = multiprocessing.Process(target=compareImages, args=(queue_screenshot,))
        thread2.start()

        #Placing a torch
        if counter % 8 == 0 and counter != 0:
            torchesPlaced += 1
            placeTorch(pickAxeNumber, torchNumber)

        #Before moving check hearts and lava
        thread1.join()
        thread2.join()

        #check middle
        scanForLava(750)

        #check far below
        scanForLava(850)

        #If lava or have taken damage, finish
        if queue_screenshot.get() < THRESHOLD or queue_lava.get() or detectLavaNoQueue(4) or lava:
            retreat()
            i = 100
            break
        else:
            #Movement
            moveForwardOneBlock()
            lookUp()

    print("Finishing")



#Look up