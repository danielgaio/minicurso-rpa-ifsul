import time
import pandas as pd
from browser import Browser

def run_automation():
    print('Running')

    b = Browser(link='https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs')
    b.search_for_a_job(job='rpa')
    time.sleep(3)

    jobs_list = b.get_jobs_list()
    jobs_information = b.get_jobs_information(jobs_list)

    jobs_information_df = pd.DataFrame.from_dict(jobs_information)

    jobs_information_df.to_excel('data/jobs_information.xlsx')

    # TODO enviar por email

    print(jobs_information)

    print('fim')

    return True
