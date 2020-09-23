import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL = 'https://www.amazon.in/GoPro-CHDHX-801-RW-Action-Camera-Adventure/dp/B08D6HYLLX/ref=sr_1_1?crid=2JDZNCG632OGA&dchild=1&keywords=gopro+hero+8+black&qid=1600869702&sprefix=gopro%2Caps%2C332&sr=8-1'

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = 'productTitle').get_text()
    price = soup.find(id = 'priceblock_ourprice').get_text()

    converted_price = price[1:8]

    if converted_price > str(25000):
        send_mail()

    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('ankurdas8017@gmail.com', 'euvgwsyyishctpku')

    subject = 'PRICE FELL DOWN!'
    body = 'Check the amazon link https://www.amazon.in/GoPro-CHDHX-801-RW-Action-Camera-Adventure/dp/B08D6HYLLX/ref=sr_1_1?crid=2JDZNCG632OGA&dchild=1&keywords=gopro+hero+8+black&qid=1600869702&sprefix=gopro%2Caps%2C332&sr=8-1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'ankurdas8017@gmail.com',
        'ankurdas8017@gmail.com',
        msg


    )
    print('HEY EMAIL HAS BEEN SENT')

    server.quit()
    
while(True):
    check_price()
    time.sleep(60*60)   