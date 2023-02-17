from browser import Browser

def run_automation():
    print('Running')

    b = Browser(link='https://www.linkedin.com/')
    b.search_for_a_job(job='rpa')

    print('fim')

    return True
