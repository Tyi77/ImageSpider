import requests
from bs4 import BeautifulSoup
import os

# inputSize = int(input("Please enter how many keywords you want: "))
# inputImage = input("Please enter the keywords of the photos (e.g. apple: 2, car sign: 12, banana: 7): ")

# print(list(map(str.strip, inputImage.split(','))))


def spider(item):
    keyword = item[0]
    count = item[1]

    response = requests.get(f'https://unsplash.com/s/photos/{keyword}')

    soup = BeautifulSoup(response.text, 'lxml')

    results = soup.select('a.rEAWd .MorZF img.YVj9w', limit=count)

    imageLinks = [result.get('src') for result in results]

    for index, link in enumerate(imageLinks):
        if not os.path.exists('./images'):
            os.mkdir('./images')
        
        img = requests.get(link)
        with open('./images/' + keyword + str(index+1) + '.jpg', 'wb') as file:
            file.write(img.content)

spider(['car', 5])