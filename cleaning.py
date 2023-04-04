import re

import pandas as pd

keywords = []
urls = ['https://www.healthline.com/nutrition/10-proven-benefits-of-blueberries?slot_pos=article_1&utm_source=Sailthru%20Email&utm_medium=Email&utm_campaign=authoritynutrition&utm_content=2022-04-04&apid=489524',
        'https://www.nytimes.com/2023/04/05/technology/apple-virtual-reality-headset.html?action=click&module=Top%20Stories&pgtype=Homepage',
        'https://www.forbes.com/sites/forbestechcouncil/2023/04/04/why-ai-and-ml-in-cybersecurity-are-the-future/?sh=4668f0c21e71',
        'https://www.businessinsider.com/best-wireless-charging-phones-2022-11?IR=T',
        'https://www.travelandleisure.com/trip-ideas/best-places-to-travel-in-may?utm_source=sailthru&utm_medium=email&utm_campaign=2022_04_04_tl&utm_content=final&utm_term=1397634'
        ]




for url in urls:
    url = url.lower()
    url = url.strip()
    url = url[url.index('//') + 2:]
    url = url[url.index('/')+1:]
    url = re.sub(r"[!@#$%^&*()_\-\?=\.]+", " ", url)

    url = url.replace("  ", " ")
    # print(url)
    url = re.sub(r" ?\d ?", "", url)
    # print(url)
    url = url.strip()
    # print(url)
    urlkwlst = []
    for u in url.split("/"):
        if u != "":
            urlkwlst.append(u.strip())
    print(urlkwlst)
    urlkwlst.sort()
    print(urlkwlst)




