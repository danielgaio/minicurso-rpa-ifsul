import time
import pandas as pd
from browser import Browser
from mail import Mail

def run_automation():
    b = Browser(link='https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs')
    time.sleep(3)
    b.search_for_a_job(job='rpa')
    time.sleep(3)
    jobs_list = b.get_jobs_list()
    time.sleep(3)
    jobs_information = b.get_jobs_information(jobs_list)

    jobs_information_df = pd.DataFrame.from_dict(jobs_information)
    jobs_information_df.to_excel('data/jobs_information.xlsx')

    m = Mail()
    m.send_mail()

    print('Processo da automação concluido.')

    return True
