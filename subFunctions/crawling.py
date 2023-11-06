import requests
from bs4 import BeautifulSoup

def scrape_weather_forPrint_fromGo():
    """
    날씨를 기상청으로부터 스크랩하여 "콘솔창"에 출력합니다
    :return:
    """

    print("Today's weather")
    url = "https://www.weather.go.kr/w/index.do"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    #날씨, 어제보다 n도 높(낮)아요
    cast = soup.find("span",attrs={"class":"wic DB05 large"}).get_text()+", "+soup.find("li",attrs={"class":"w-txt"}).get_text()
    #현재 온도/최저/최고
    curr_temp = soup.find("span",attrs={"class":"tmp"}).get_text() + "/" + soup.find("span",attrs={"class":"chill"}).get_text() + "/" + soup.find("span",attrs={"class":"tminmax"}).get_text()

    print(cast)
    print(curr_temp)

def scrape_weather_forPrintTry_fromGO():
    print("Today's weather")
    url = "https://www.weather.go.kr/w/index.do"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    try:
        # Try to find each element and get its text, if the element is not found, handle it gracefully
        cast_span = soup.find("span", attrs={"class": "wic DB05 large"})
        cast_li = soup.find("li", attrs={"class": "w-txt"})
        cast = (cast_span.get_text() if cast_span else "N/A") + ", " + (cast_li.get_text() if cast_li else "N/A")

        curr_temp_span = soup.find("span", attrs={"class": "tmp"})
        chill_span = soup.find("span", attrs={"class": "chill"})
        tminmax_span = soup.find("span", attrs={"class": "tminmax"})
        curr_temp = (curr_temp_span.get_text() if curr_temp_span else "N/A") + "/" + \
                    (chill_span.get_text() if chill_span else "N/A") + "/" + \
                    (tminmax_span.get_text() if tminmax_span else "N/A")

        print(cast)
        print(curr_temp)
    except AttributeError as e:
        print(f"An attribute error occurred: {e}")

def scrape_weather_forPrint_fromNaver():
    """
    날씨를 네이버로부터 스크랩하여 "콘솔창"에 출력합니다
    :return:
    """

    print("Today's weather")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8&oquery=loby&tqi=iRBC8wqo1SossDgN9WhssssstRK-079882"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    #날씨, 어제보다 n도 높(낮)아요
    cast = soup.find("p",attrs={"class":"summary"}).get_text()
    #현재 온도/최저/최고
    curr_temp = soup.find("div",attrs={"class":"temperature_text"}).get_text().replace("도씨","") + "/" + soup.find("span",attrs={"class":"lowest"}).get_text() + "/" + soup.find("span",attrs={"class":"highest"}).get_text()

    print(cast)
    print(curr_temp)

scrape_weather_forPrint_fromNaver()



