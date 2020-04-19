import multiprocessing
from helperFunctions.Hardware_Input.keyPresses import press_key, release_key
from enum import Enum
from pynput.mouse import Button, Controller as CM
import os


#Setup mouse input
mouse = CM()


#HEX for keyboard input
DIK_W = 0x11 
DIK_S = 0x1F
DIK_1 = 0x02
DIK_2 = 0x03
DIK_3 = 0x04
DIK_4 = 0x05
DIK_5 = 0x06
DIK_6 = 0x07
DIK_7 = 0x08
DIK_8 = 0x09
DIK_9 = 0x0A
DIK_SPACE = 0x39
DIK_LMENU = 0x38    
DIK_F4 = 0x3E              

class allMouseInputs(Enum):
    leftClick = 1
    leftRelease = 2
    rightClick = 3
    rightRelease = 4
    leftHold = 5
    rightHold = 6

class allInstructions(Enum):
    FORWARD = DIK_W
    BACKWARD = DIK_S
    ONE = DIK_1
    TWO = DIK_2
    THREE = DIK_3
    FOUR = DIK_4
    FIVE = DIK_5
    SIX = DIK_6
    SEVEN = DIK_7
    EIGHT = DIK_8
    NINE = DIK_9
    SPACE = DIK_SPACE
    MINE = allMouseInputs.leftHold
    PLACE_TORCH = allMouseInputs.rightHold
    ALT= DIK_LMENU 
    F4 = DIK_F4


def sendInstruction(argument):
    if (argument != allInstructions.MINE and argument != allInstructions.PLACE_TORCH):
        press_key(argument.value)
    else:
        mouseInput(argument.value)

def stopInstruction(argument):
    if (argument != allInstructions.MINE and argument != allInstructions.PLACE_TORCH):
        release_key(argument.value)
    else:
        if argument == allInstructions.MINE:
            mouseInput(allMouseInputs.leftRelease)
        if argument == allInstructions.PLACE_TORCH:
            mouseInput(allMouseInputs.rightRelease)


def mouseInput(argument):
    mouseInputNumber = argument.value
    if mouseInputNumber == 1:
        mouse.click(Button.left)
    elif mouseInputNumber == 2:
        mouse.release(Button.left)
    elif mouseInputNumber == 3:
        mouse.click(Button.right)
    elif mouseInputNumber == 4:
        mouse.release(Button.right)
    elif mouseInputNumber == 5:
        mouse.press(Button.left)
    elif mouseInputNumber == 6:
        mouse.press(Button.right)