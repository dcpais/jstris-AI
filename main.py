#-------------- IMPORTS --------------#
import cv2
import time
# We will use pygame for a basic GUI we can run in parallel
import pygame as pg 

# Selenium Stuff
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#-------------- CONSTANTS --------------#
FPS = 60
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
BACKGROUND = (255, 255, 255)

#-------------- FUNCTIONS --------------# 
def get_screenshot():
    pass

def convert_to_state():
    pass

#-------------- CLASSES --------------#
class State:

    def __init__(self, board, held, next_piece) -> None:
        self._board = board
        self._held = held
        self._next_piece = next_piece

#-------------- ENTRY POINT --------------#
if __name__ == "__main__":
    # Selenium setup
    driver = webdriver.Chrome()
    driver.get("https://jstris.jezevec10.com/")
    running = True

    # Pygame setup
    pg.init()
    WINDOW = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pg.display.set_caption('Jstris-AI controller')
    clock = pg.time.Clock()
    
    # Main Loop
    while running:

        # Get inputs
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                running = False

        # Update display
        WINDOW.fill(BACKGROUND)
        pg.display.update()
        clock.tick(FPS)


    # Clean up
    pg.quit()  
    driver.close()