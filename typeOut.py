import config
import keyboard
import random
import time

def type(text):
    characters = []
    
    for char in text:
        characters.append(char)
        
    for i in range(len(characters)):
        keyboard.press_and_release(characters[i])
        time.sleep(random.uniform(config.min, config.max))
        
    keyboard.press_and_release('enter')