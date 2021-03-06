#!/bin/sh

for var in `seq 100 10 300`
do

   lower_bound=$var
   upper_bound=`expr $var + 10`

   # Fixed Variables
   CITY="Berlin"
   CONJUNCTION="to"
   FORMAT=".json"
   DATA_LOCATION="berlin_data"

   filename="$lower_bound$CONJUNCTION$upper_bound$FORMAT"

   # Run scraper on specific range
   scrapy crawl airbnb -o $filename -a city=$CITY -a price_lb=$lower_bound -a price_ub=$upper_bound
   mv $filename $DATA_LOCATION

done

