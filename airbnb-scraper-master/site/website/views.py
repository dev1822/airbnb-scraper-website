from flask import render_template, Blueprint, request
import subprocess
import json

views = Blueprint('views', __name__)

PATH_TO_DATES_TXT = '/Users/kinshuk/Downloads/airbnb-scraper-master/airbnb_scraper/spiders/dates.txt'
PATH_TO_SCRIPT = '/Users/kinshuk/Downloads/airbnb-scraper-master/site/script.sh'
PATH_TO_JSON = '/Users/kinshuk/Downloads/airbnb-scraper-master/site/final.json'

@views.route('/',  methods=['GET', 'POST'])
def home():

    if request.method == "POST":
        city = request.form.get('city')
        minprice = request.form.get('minprice')
        maxprice = request.form.get('maxprice')
        checkin = request.form.get('checkin')
        checkout = request.form.get('checkout')

        file = open('script.sh', 'w+')
        # file.write('do')
        # file.write('\n')
        file.write(f'lower_bound={minprice}')
        file.write('\n')
        file.write(f'upper_bound={maxprice}')
        file.write('\n')
        file.write(f'CITY="{city}"')
        file.write('\n')
        file.write(f'filename="final.json"')
        file.write('\n')
        file.write(f'scrapy crawl airbnb -o $filename -a city=$CITY -a price_lb=$lower_bound -a price_ub=$upper_bound')
        # file.write('\n')
        # file.write('done')
        file.close()

        file2 = open(PATH_TO_DATES_TXT, 'w+')
        file2.write(checkin)
        file2.write('\n')
        file2.write(checkout)
        file2.close()

        # subprocess.call(['sh', PATH_TO_SCRIPT])

        with open(PATH_TO_JSON, 'r') as f:
            data = json.load(f)
        print(type(data))
        
        print(data)
        titles = []
        for item in data:
            for key, value in item.items():
                if key in titles:
                    break
                titles.append(key)

        print(titles)
        return render_template('home.html', data=data, titles = titles)

        print(city, minprice, maxprice, checkin, checkout)
    return render_template('home.html', data={}, titles={})