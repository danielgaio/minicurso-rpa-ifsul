import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Browser:
    def __init__(self, link):
        self.driver = webdriver.Chrome('/bin/chromedriver')
        self.driver.get(link)
        self.driver.maximize_window()

    def search_for_a_job(self, job):
        search_box = self.driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/section/section[2]/form/section[1]/input')
        search_box.send_keys(job)
        search_box.send_keys(Keys.RETURN)
        print('Busca concluida.')

    def get_jobs_list(self):
        jobs_list = self.driver.find_elements(By.XPATH, '//*[@id="main-content"]/section/ul/li')
        return jobs_list

    def get_jobs_information(self, jobs_list):
        def wait_for_for_title():
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/section/div[2]/section/div/div[1]/div/a/h2')))

        jobs_information = []

        for i, job in enumerate(jobs_list):
            time.sleep(1)
            job.find_element(By.TAG_NAME, 'a').click()
            try:
                wait_for_for_title()
            except TimeoutException as ex:
                print(ex)
                jobs_list[i-1].find_element(By.TAG_NAME, 'a').click()
                time.sleep(1)
                job.find_element(By.TAG_NAME, 'a').click()
                time.sleep(1)

            job_information = {
                'job_title': self.driver.find_element(By.XPATH, '/html/body/div[1]/div/section/div[2]/section/div/div[1]/div/a/h2').text,
                'long_description': self.driver.find_element(By.XPATH, '/html/body/div[1]/div/section/div[2]/div/section[1]/div/div/section/div').text,
                'experience_level': self.driver.find_element(By.XPATH, '/html/body/div[1]/div/section/div[2]/div/section[1]/div/ul/li[1]/span').text,
                'job_type': self.driver.find_element(By.XPATH, '/html/body/div[1]/div/section/div[2]/div/section[1]/div/ul/li[2]/span').text,
                'role': self.driver.find_element(By.XPATH, '/html/body/div[1]/div/section/div[2]/div/section[1]/div/ul/li[3]/span').text,
                'sector': self.driver.find_element(By.XPATH, '/html/body/div[1]/div/section/div[2]/div/section[1]/div/ul/li[4]/span').text
            }
            jobs_information.append(job_information)

        print('Coleta de informações concluida.')
        return jobs_information
