import requests
import pandas as pd
from bs4 import BeautifulSoup

print("Your Movie list is on it's way")
print('What Would you like to save it with?')
file_name = input('>')

latest_movies = []
for no in range(1,4):
    url = f"https://www.rottentomatoes.com/browse/movies_in_theaters/sort:newest?page={no}"
    response = requests.get(url)
    response = response.content
    soup = BeautifulSoup(response, 'html.parser')
    container = soup.find_all('div', class_ = 'flex-container')

    for movie in container:
        Title = movie.find('span', class_ ='p--small').text.strip()
        release = movie.find('span', class_ ='smaller').text.strip()
        latest_movies.append([Title, release])
data = pd.DataFrame(latest_movies, columns=['MOVIE NAME', 'DATE RELEASE'])

data.to_csv(f'{file_name}.csv')
print('Movie List Saved')
print("""Thanks, 
and Expect more from THE KINGS WORLD""")
