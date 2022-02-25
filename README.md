# Surfs_up
Weather data analysis using jupyter notebook, SQLite, SQLalchemy, and Flask to share the analysis.
### Overview of the Analysis
The purpose of the this analysis was to analyze weather data of Oahhu, Hawaii to determine if it is sustainable to open a surf and ice cream  shop year round as requested by an investor. 

### Results
Using SQLite and SQLalchemy to retrieve and store weather data, the following were three key differences found:
1. While the maximum temperature between June (85 F) and December (83 F) are similar, the minimum temperature (June: 64 F; December: 56 F) between the months is worthy to mention. December's minimum temperature is cooler and should be taken into consideration as part of opening up a surf and ice cream shop. Perhaps products to be sold in December should address the cooler temperature pattern.
2. The total count of tempeature data collected for analysis in the month of June was 217 more (1700 total) than the month of December (1517 total). This difference is important to note since it has an impact on the calculation of the averages and the quartile temperature calculations.The smaller temperature count reflected in the December data could cause the average temperature to not reflect a wider range in temperature than the averages calculated for the month of June.
3. There is a larger difference, or wider temperature range for the month of December between the minimum temperature (56 F) and the average temperature in the first quartile (69 F) compared to the month of June where minimum temperature (64 F) is closer to the average temperature in the first quartile (73 F).

### Additional queries to consider
To get a better understanding of the weather patterns between the months of June and December, I recommend running additional queries on data pertaining to rain fall per month and the relative humidity per month. Both weather conditions have significant impact on the success of opening a surf and ice cream shop.
