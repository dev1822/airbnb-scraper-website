lower_bound=300
upper_bound=400
CITY="London"
filename="final.json"
scrapy crawl airbnb -o $filename -a city=$CITY -a price_lb=$lower_bound -a price_ub=$upper_bound