# Author: Isabela Costa Souza (isabelacsbr@gmail.com) 
# Date: 24.05.2020
# To configurate your enviroment, execute the 'setup.py' file on 'convertapi-python-master' folder

import os
import glob
import convertapi

def get_relevant_info_on_pdf(pdf_url):
    path = os.path.dirname(os.path.abspath(__file__))

    convertapi.api_secret = 'YgzbnxIW6UbmrI3X'
    converted_file = convertapi.convert('txt', {
        'File': pdf_url,
        'PageRange': '1',
        'LineLength': '40'
    }, from_format = 'pdf').save_files(path + "\\reports")

    report_path = path + "\\reports\\" + glob.glob(path + "\\reports\\*.txt")[0].split("\\")[-1]

    report_file = open(report_path)
    contents = list(filter(None, (report_file.read()).split('\n')))
    report_file.close()

    relevant_content = []

    for content in contents:
        if(any(map(str.isdigit, content)) or (content.lower()).find("bito") != -1 or (content.lower()).find("confirma") != -1 or (content.lower()).find("leta") != -1 or (content.lower()).find("negat") != -1 or (content.lower()).find("lise") != -1):
            relevant_content.append(" ".join(content.split()))

    os.remove(report_path)

    return relevant_content

pdf_url = 'http://riobranco.ac.gov.br/images/stories/2020/CORONAVIRUS/BOLETIMCOVID17.05.pdf'

relevant_info = get_relevant_info_on_pdf(pdf_url)
print(relevant_info)