from time import sleep
import pyautogui
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'  
import cv2
import re
from english_words import english_words_lower_set
from nltk.corpus import wordnet
import json

firstdoc = [600, 390]
between = 60
perpage = 11
scrollAmount = -630
arr=[]

def convert(filename):
    img = cv2.imread(filename)
    hImg, wImg, _ = img.shape
    out=pytesseract.image_to_string(img).strip()
    return out.split("-")[0]

def analyzeDocument():
    pyautogui.click(clicks=2, interval=0.25)
    sleep(2.5) #wait for page to load

    myScreenshot = pyautogui.screenshot(region=(80, 170, 400, 40))
    myScreenshot.save(r'name.png')
    name = convert('name.png')

    pyautogui.keyDown("ctrl"); pyautogui.keyDown("shift"); sleep(0.2); pyautogui.press("c"); pyautogui.keyUp("shift"); pyautogui.keyUp("ctrl"); #check word count
    sleep(1)
    myScreenshot = pyautogui.screenshot(region=(1060, 490, 70, 35))
    myScreenshot.save(r'word.png')
    word = convert('word.png')
    print(name, word)
    while(not word.isdigit()):
        sleep(2)
        myScreenshot = pyautogui.screenshot(region=(1060, 490, 70, 35))
        myScreenshot.save(r'word.png')
        sleep(2)
        word = convert('word.png')
        print("YO TOO FAST SLOW DOWN", word)
    wordCount=int(word)

    term=[name, wordCount]
    if(term not in arr):
        arr.append(term)

    pyautogui.keyDown("ctrl"); pyautogui.press("w"); pyautogui.keyUp("ctrl") #close tab

#MAIN STARTS HERE TODO

pyautogui.keyDown("alt")
pyautogui.press("tab")
pyautogui.keyUp("alt")
for i in range(3): #need to scroll 3 times
    for i in range(perpage):
        pyautogui.moveTo(600, 390 + i*between)
        sleep(0.2)
        analyzeDocument()

    pyautogui.scroll(scrollAmount)

for i in range(5): #LAST PAGE (5 people on the last page)
    pyautogui.moveTo(600, 990 - i*between)
    sleep(0.2)
    analyzeDocument()

arr = sorted(arr, key = lambda x: x[1], reverse=True)
print("LENGTH: ", len(arr))
for i in arr:
    print(i)

