from django.shortcuts import render
import requests
import smtplib
from bs4 import BeautifulSoup

def Home(request):
    if request.method == "POST":
        search = request.POST.get('search')
        search_list = search.split(" ")
        search_string = ""
        for i in search_list:
            search_string = search_string + "+" + i
        search_string = search_string[1:]
        URL = "https://www.google.com/search?q={}&sxsrf=AJOqlzV9hhQbn79gVzi_coW26FdbrUx4Gg%3A1674279807648&source=hp&ei=f3vLY6SsJcCtseMP3-yW8Ac&iflsig=AK50M_UAAAAAY8uJj5pL9kfW3eymvH4NK3uqOrN5Kyau&ved=0ahUKEwjk57-p-tf8AhXAVmwGHV-2BX4Q4dUDCAg&uact=5&oq=akshay+vayak&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBwgAEA0QgAQyBwgAEA0QgAQyBwgAEA0QgAQyBwgAEA0QgAQyBwgAEA0QgAQyBwgAEA0QgAQyBwgAEA0QgAQyBwgAEA0QgAQyBggAEB4QDToECC4QJzoECC4QQzoFCAAQkQI6BAgAEEM6CgguEIMBELEDEEM6BwgAELEDEEM6CwguEIAEELEDEIMBOggILhCDARCxAzoLCAAQgAQQsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOgUILhCRAjoNCAAQgAQQFBCHAhCxAzoLCC4QrwEQxwEQgAQ6CAguEIAEELEDOggIABCABBCxAzoOCC4QrwEQxwEQsQMQgAQ6CAguELEDEJECOgUIABCABDoKCC4QgAQQFBCHAjoQCC4QFBCvARDHARCHAhCABDoFCC4QgAQ6DQguEIAEEMcBEK8BEAo6CwguEIAEEMcBEK8BOgcILhCABBAKOg0ILhANEK8BEMcBEIAEOg0ILhANEIAEEMcBEK8BUABYphBg4BJoAHAAeACAAYMCiAHMEpIBBTAuOC40mAEAoAEB&sclient=gws-wiz".format(search_string)
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
        r = requests.get(url=URL, headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")
        datas = soup.find_all('div', attrs={'class': 'egMi0 kCrYT'})
        all_data = []
        for i in datas:
            dic = {}
            url = 'https://www.google.com/' + i.find('a').get("href")
            heading = i.find('div', attrs={'class': 'BNeawe vvjwJb AP7Wnd'})
            sitename = i.find('div', attrs={'class': 'BNeawe UPmit AP7Wnd lRVwie'})
            dic["url"] = url
            dic["heading"] = heading.text
            dic["sitename"] = sitename.text
            all_data.append(dic)
        return render(request, "Mynews/index.html",{"data":all_data})
    return render(request, "Mynews/index.html")