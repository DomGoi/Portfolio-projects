import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AnkiBot:
    def __init__(self, mail_my, password_1,txt):
        self.chrome_opt = webdriver.ChromeOptions()
        self.chrome_opt.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=self.chrome_opt)
        self.URL_ANKI = "https://ankiweb.net/about"
        self.mail = mail_my
        self.password = password_1
        self.txt_name=txt

    def get_german_phrases(self):
         with open(self.txt_name, 'r', encoding='utf') as file:
             content=json.load(file)
         return content


    def get_anki(self):
        self.driver.get(self.URL_ANKI)
        time.sleep(20)

        # Corrected WebDriverWait usage
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/nav/div/div[2]/ul[2]/li[1]/a"))
        )
        login_button = self.driver.find_element(By.XPATH, "/html/body/div/nav/div/div[2]/ul[2]/li[1]/a")
        login_button.click()

        time.sleep(10)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/main/form/div[1]/input"))
        )
        email = self.driver.find_element(By.XPATH, "/html/body/div/main/form/div[1]/input")
        email.send_keys(self.mail)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div/main/form/div[2]/input"))
        )
        password = self.driver.find_element(By.XPATH, "/html/body/div/main/form/div[2]/input")
        password.send_keys(self.password)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/form/div[3]/button"))
        )
        log_in = self.driver.find_element(By.XPATH, "/html/body/div/main/form/div[3]/button")
        log_in.click()

        time.sleep(5)

    def adding_phrase(self):

        german_dict=self.get_german_phrases()

        #Editing german list
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(((By.XPATH,"/html/body/div/nav/div/div[2]/ul[1]/li[2]/a")))
        )
        add=self.driver.find_element(By.XPATH,"/html/body/div/nav/div/div[2]/ul[1]/li[2]/a")
        add.click()


        for german_phrase, english_translation in german_dict.items():

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/form/div[1]/div/div"))
            )
            front=self.driver.find_element(By.XPATH,"/html/body/div/main/form/div[1]/div/div")
            front.send_keys(german_phrase)

            WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable((By.XPATH,"/html/body/div/main/form/div[2]/div/div"))
            )
            back=self.driver.find_element(By.XPATH,"/html/body/div/main/form/div[2]/div/div")
            back.send_keys(english_translation)

            time.sleep(2)

            WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable((By.XPATH,"/html/body/div/main/form/button"))
            )
            add_button=self.driver.find_element(By.XPATH,"/html/body/div/main/form/button")
            add_button.click()

            time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/nav/div/div[2]/ul[1]/li[1]/a"))
        )
        decks_button=self.driver.find_element(By.XPATH,"/html/body/div/nav/div/div[2]/ul[1]/li[1]/a")
        decks_button.click()

        self.driver.quit()




