import requests

api_key = "pub_4345d77a8919e43d5ab144fe978256a72f16"


def get_news():
    category = input("""Which category news do you want? 
Sport - Politics - Technology - Business - Health - Science - Food - World - Top - entertainment - environment : """)
    language = input("which language : ")
    news = 0
    while True:
        respone = requests.get(
            f'https://newsdata.io/api/1/news?apikey={api_key}&q={category}&language={language}')

        if news == 0:
            news = 0

        title = respone.json()["results"][news]["title"]
        link = respone.json()["results"][news]["link"]
        description = respone.json()["results"][news]["description"]
        print(
            f"\ntitle : {title} \n\nlink : {link} \n\ndescription : {description}")

        next_page = int(input("do you want go to next news? yes=0 no=1 : "))

        if next_page == 0:
            news += 1
        else:
            break

get_news()


dsfjasl;joawfoawngvoi3whg8ownoi3h8iwnvl3hfoqifmq'2ujfowsf
gw'g
ewwgowsgvoiwnguwsyhvswm gw

hsgwsifhwsgmwghywsjgmw
ge;gwg9pw,wgg
