# Absolute-copy-paste
The intention of the program was to make copying info from PDF files or websites that dont allow native copy and paste to be easier 
and to not require manually typing.

# How it works
On program start, keeps track of users mouse inputs to determine where to take a screenshot. Gets x and y coordinates of mouse down, then again when button released.
We then pass those coords to the region arguement for pyautogui's screenshot function.

Once we have the screenshot we pass that image file to pytessaract and pass the letters it found within the image to the type_letters function.

We then wait until the user enters a specifc keyboard combination to start typing the characters passed in.

I designed the type_letters function to be very modular, allowing you to determine the amount of 'errors' the program will make while typing (ie to simular human typos and such)
