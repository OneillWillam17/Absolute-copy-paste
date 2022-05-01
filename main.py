import pytesseract
import pyautogui
from pynput.mouse import Listener
import keyboard
import time
import random
from string import ascii_lowercase

location = {
    "mouse-down": {
        "x": None,
        "y": None
    },
    "mouse-up": {
        "x": None,
        "y": None
    }
}


# This function will be called when any key of mouse is pressed
def on_click(*args):
    # print(args)
    is_pressed = args[-1]
    button = args[-2]
    global location

    if is_pressed:
        print(f"{button.name} is down")
        # print(f"x: {args[0]}, y: {args[1]}")
        location['mouse-down']['x'] = args[0]
        location['mouse-down']['y'] = args[1]
    else:
        print(f"{button.name} is up")
        # print(f"x: {args[0]}, y: {args[1]}")
        location['mouse-up']['x'] = args[0]
        location['mouse-up']['y'] = args[1]
        # cancels infinite loop caused by listener.start()
        raise Listener.StopException


def get_screenshot_loc(time_before_screenshot=3):
    # checks for user mouse inputs
    with Listener(on_click=on_click) as listener:
        listener.join()

    left = location['mouse-down']['x']
    top = location['mouse-down']['y']
    width = location['mouse-up']['x'] - location['mouse-down']['x']
    height = location['mouse-up']['y'] - location['mouse-down']['y']

    region = (left, top, width, height)
    print(f"Capturing screen in {time_before_screenshot} seconds")
    time.sleep(time_before_screenshot)
    image = pyautogui.screenshot(region=region)
    image.save('image.png')
    return image


def type_letters(words, error_chance=4, remove_enter=True):
    """uses pyautogui to send keystrokes of the words passed in args, can define the % chance that program makes
    an 'error' and has to go back and delete it, remove_enter: stops the program from inputting enter or
    making new lines, useful for notepad / something like that """
    if remove_enter:
        list_letters = [letter if letter != '\n' else " " for letter in words]
    else:
        list_letters = [letter for letter in words]
    print(words)

    for letter in list_letters:
        delay_in_typing = random.uniform(0.0, 0.15)
        if random.randint(1, 100) < error_chance:
            # simulate errors in typing
            pyautogui.press(random.choice(ascii_lowercase))
            time.sleep(delay_in_typing * 9)
            pyautogui.press('backspace')
        time.sleep(delay_in_typing)
        pyautogui.press(letter)


# remove the pause, so we can manually adjust how fast program types
# tesseract cmd is changed to path installed on this computer
pyautogui.PAUSE = 0
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def main():
    image = get_screenshot_loc()
    current_words = pytesseract.image_to_string(image)

    # stops program til user enters key combination
    print("Ready to type....")
    keyboard.wait('ctrl+space')
    type_letters(current_words)


if __name__ == '__main__':
    main()
