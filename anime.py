from jikanpy import Jikan

jikan = Jikan()
current_season = jikan.seasons(extension='now')

for anime in current_season['data'][:15]:
    title = anime['title']
    score = anime['score']
    print(f"{title} | Оцінка: {score}")