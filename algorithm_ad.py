import re
import pandas as pd

class keyword_search:

    def url_cleaning(self, url):
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
        urlkwlst.sort()
        return urlkwlst

    def algo(self, url_keyword_list, ):




