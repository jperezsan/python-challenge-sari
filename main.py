import mechanicalsoup
from prettytable import PrettyTable

browser = mechanicalsoup.StatefulBrowser(user_agent='MechanicalSoup')
movie_list = {
    "Minari": "tt10633456",
    "SoundOfMetal": "tt5363618",
    "Mank": "tt10618286",
    "PromisingYoungWoman": "tt9620292",
    "TheFather": "tt10272386",
    "JudasAndTheBlackMessiah": "tt9784798",
    "TheTrialOfTheChicago7": "tt1070874",
    "Nomadland": "tt9770150"
}

print("IMBD Web Crawler")
table = PrettyTable()
table.field_names = ["Year", "Rating", "Directors", "Plot", "Cast", "Genre"]

for movie in movie_list:
    print("Crawling IMBD website for title:", movie)
    print("URL:", "https://www.imdb.com/title/" + movie_list[movie])
    browser.open("https://www.imdb.com/title/" + movie_list[movie])
    year = browser.page.select('.titleBar .title_wrapper .subtext a')[-1].text.split()[2]
    rating = browser.page.select('.ratingValue strong span')[0].text
    directors = browser.page.select('.plot_summary .credit_summary_item a')[0].text
    plot = browser.page.select('.canwrap span')[0].text
    cast = [browser.page.select('.cast_list tr')[1].select('td a')[1].text[:-1],
            browser.page.select('.cast_list tr')[2].select('td a')[1].text[:-1],
            browser.page.select('.cast_list tr')[3].select('td a')[1].text[:-1],
            browser.page.select('.cast_list tr')[4].select('td a')[1].text[:-1],
            browser.page.select('.cast_list tr')[5].select('td a')[1].text[:-1]]
    genre = browser.page.select('.canwrap a')[-1].text

    table.add_row([year, rating, directors, plot, cast, genre])

with open('output.txt', 'w') as file:
    file.write(str(table))