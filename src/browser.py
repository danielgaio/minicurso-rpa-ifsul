from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Browser:
    def __init__(self, link):
        self.driver = webdriver.Chrome('/bin/chromedriver')
        self.driver.get(link)
        self.driver.maximize_window()

    def search_for_a_job(self, job):
        print('clicar em jobs')
        # TODO clicar btn jobs
        self.driver.get('https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs')
        self.driver.find_element(By.XPATH, '')
        # TODO digitar termo na caixa de pesquisa
