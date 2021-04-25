import requests
from bs4 import BeautifulSoup
import re

URL = "https://seaportai.com/blog-predictive-maintenance/"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
table = soup.find('div', attrs = {'id':'main-content'})
text = table.text
cleaned_text = re.sub('\t', "", text)
cleaned_texts = re.split('\n', cleaned_text)
cleaned_texts_list = "".join(cleaned_texts)
file1 = open('seaportai.txt', 'w')
file1.writelines(cleaned_texts_list)
file1.close()