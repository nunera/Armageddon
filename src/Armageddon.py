"""Main file for Armageddon."""
import timeit
from selenium import webdriver

path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
path2 = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

timeit.default_timer()

Options = webdriver.ChromeOptions
Options.add_argument(Options,"--headless")
Options.add_argument(Options,"--window-size=1920x1080")

webdriver.Chrome(Options)
