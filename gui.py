

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img


model1=tf.keras.models.load_model('model.h5')


from pathlib import Path

from future.moves import tkinter
from tkinter import Tk, Canvas, Entry, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1215x630")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 630,
    width = 1215,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    607.0,
    315.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    607.0,
    315.0,
    image=image_image_2
)

canvas.create_text(
    128.0,
    494.0,
    anchor="nw",
    text="3. Press esc key\n    to exit camera",
    fill="#FFFFFF",
    font=("Roboto Bold", 36 * -1)
)

canvas.create_text(
    131.0,
    308.0,
    anchor="nw",
    text="2. Press spacebar \nto capture an image",
    fill="#FFFFFF",
    font=("Roboto Bold", 32 * -1)
)

canvas.create_text(
    113.0,
    193.0,
    anchor="nw",
    text="Click on camera\nto open camera",
    fill="#FFFFFF",
    font=("Roboto Bold", 36 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    85.0,
    82.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    458.0,
    545.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    649.0,
    377.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    671.0,
    177.0,
    image=image_image_6
)

canvas.create_text(
    113.0,
    49.0,
    anchor="nw",
    text="Website Name",
    fill="#FFFFFF",
    font=("Merriweather Bold", 42 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=893.0,
    y=92.0,
    width=150.0,
    height=71.0
)
window.resizable(False, False)
window.mainloop()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


PATH ="Downloads\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://gourmetgarden.in/account/login")

search1 = driver.find_element_by_class_name('modal__store-pick-link').click()

search2 = driver.find_element_by_id('CustomerEmail')
search2.send_keys('deekkshitha02@gmail.com')

search3 = driver.find_element_by_id('CustomerPassword')
search3.send_keys('2002@Dee')

search4 = driver.find_element_by_class_name('user-account__login-btn-wrapper').click()

search5 = driver.find_element_by_id('SearchInput')
search5.send_keys('mango')

time.sleep(30)


search6 = driver.find_element_by_css_selector('#shopify-section-header > header > div.site-header_inner > div > div.site-header_buttons > a > svg').click()
search7 = driver.find_element_by_css_selector('#shopify-section-cart-template > div.page-width--wide.page-container > form > footer > div > div.cart_cta-buttons > button').click()

search8 = driver.find_element_by_id('pincodeInput')
search8.send_keys(560008)


search9 = driver.find_element_by_css_selector('#deliveryPincode > div > button').click()

search10 = driver.find_element_by_css_selector('#continue_button').click()