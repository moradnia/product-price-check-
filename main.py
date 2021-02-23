import requests
from bs4 import BeautifulSoup
import arabic_reshaper
from bidi.algorithm import get_display
from unidecode import unidecode
import smtplib

url = 'https://www.digikala.com/product/dkp-2361428/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8' \
      '%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-a51-sm-a515fdsn-%D8%AF%D9%88-%D8%B3%DB%8C%D9' \
      '%85-%DA%A9%D8%A7%D8%B1%D8%AA-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-128%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA '
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/85.0.4183.102 Safari/537.36'}

page = requests.get(url, headers=header)
soup = BeautifulSoup(page.content, 'html.parser')


def check_price():
    title = soup.select_one('h1.c-product__title').get_text().strip()
    # also
    # title = soup.find(attrs={'c-product__title'}).get_text().strip()
    price = soup.select_one('div.c-product__seller-price-raw').get_text().strip().replace(",", "")
    # for change type en num to farsi num use unidecode library 
    price_en = unidecode(price)
    if int(price_en) > 8000000:
        send_email()


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('src-email', 'email-password')
    subject = 'price feel down !'
    body = 'https://www.digikala.com/product/dkp-2361428/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9' \
           '%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-a51-sm-a515fdsn-%D8%AF%D9%88-%D8' \
           '%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-128%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8' \
           '%D8%A7%DB%8C%D8%AA '
    msg = f"{subject}\n\n{body}"
    server.sendmail('src-email', 'dst-email', msg)
    print('SEND EMAIL')
    server.quit()


check_price()
