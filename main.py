
# importing webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import time

try:
    print("Program started")

    # Here Chrome will be used
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach',True)
    driver = webdriver.Chrome(options=options)

    # URL of website
    url = "https://www.vidyavision.com/results/apssc2023.htm"

    # Opening the website
    driver.get(url)


    for i in range(3580,3590):
    # get element
        Roll_no_field = driver.find_element(By.ID, "rollno")
        Roll_no_field.clear()
        val1 = 2321100000+i
        val = str(val1)

    # send keys
        Roll_no_field.send_keys(val)
        time.sleep(2)
        Total_marks = driver.find_element(By.ID,"r25")
        Student_dist = driver.find_element(By.ID,'r3')
        Student_name = driver.find_element(By.ID,'r2')
        Student_rollno = driver.find_element(By.ID,'r1')

        if Student_dist.text == "KURNOOL" and int(Total_marks.text)>=550:
            print(f"{Student_name.text}:{Total_marks.text}")

    # saving screenshot
        driver.save_screenshot(f"image{i}.png")
        time.sleep(2)

    # getting the button by class name
    # button = driver.find_element(By.CLASS_NAME, "orangelinks")
    # clicking on the button
    # button.click()

    # saving screenshot
    # driver.save_screenshot(f"image{i}.png")



    # Loading the image
        image = Image.open(f"image{i}.png")
    #
    # Showing the image
        image.show()
        time.sleep(2)


    print("Program End")
except Exception as e:
    print("target window closed")

