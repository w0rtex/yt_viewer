from selenium import webdriver
from func_timeout import func_timeout, FunctionTimedOut

i = 1

import threading

video_link = input("Link URI: ")
count = int(input("Enter views count: "))
driver = webdriver.Chrome(executable_path='./chromedriver')
driver1 = webdriver.Chrome(executable_path='./chromedriver')
driver2 = webdriver.Chrome(executable_path='./chromedriver')
driver3 = webdriver.Chrome(executable_path='./chromedriver')
driver4 = webdriver.Chrome(executable_path='./chromedriver')

def printit():
    global i

    if i >= count + 1:
        exit()
        driver0.quit()
        driver1.quit()
        driver2.quit()
        driver3.quit()
        driver4.quit()

    threading.Timer(33.0, printit).start()
    driver.get(video_link)
    driver1.get(video_link)
    driver2.get(video_link)
    driver3.get(video_link)
    driver4.get(video_link)
    print(f"Current loop is {i}'th")
    i += 4

printit()