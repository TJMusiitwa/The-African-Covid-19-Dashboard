## The African Covid-19 Dashboard

![Covid19PushFetch](https://github.com/TJMusiitwa/The-African-Covid-19-Dashboard/workflows/Covid19PushFetch/badge.svg)

[![Heroku App Status](http://heroku-shields.herokuapp.com/african-covid19-dashboard)](https://african-covid19-dashboard.herokuapp.com)

### Foreword

Hello and welcome, you might be wondering "oh great" another dashboard and yes you are right it is however, the prime focus of this dashboard is as stated in the title to mainly visualize an overview of the 2019 Novel Coronavirus COVID-19 (2019-nCoV) epidemic as it relates to the African continent.

This dashboard was built with Python using [Dash](https://dash.plot.ly/), with charts made in [Plotly](https://plot.ly/) and the Flatly theme of the app provided by [Bootswatch](https://bootswatch.com/flatly/).

This dashboard is set up to update the data daily from the [Johns Hopkins Center for Systems Science and Engineering](https://github.com/CSSEGISandData/COVID-19) Coronavirus repository.

## To-Do
While a lot has already been done; there still remains a few things in my opinion would add greater functionality to the dashboard in general.
 - [ ] Make the web app phone responsive
 
 - [ ] Make into a PWA (Progressive Web App)
 
 - [ ] Add insight into the data with SIR/SEIR models and timeline predictions on the data

## Home Page
### Graph Indicators
The statistic card indicators showcase the overall number of respective cases on the African continent. The green percentage marks show the delta in terms of increase in the number of cases from the previous day.

### African Maps
The African maps show markers for each region is relative to the square root of the  cases within that country.
The size of the marker is a measure of how many people have caught the virus within that country since the outbreak began and the color is a measure of how active the virus currently is, with darker colors indicating the virus has had a greater impact and lighter shades indicating that it has caused less of an impact.

### Overall Trend
The trend chart displays the totals for `CONFIRMED`, `ACTIVE`, `RECOVERED`, and `DEATHS` for Africa, by date. Hovering the mouse over the chart will reveal the counts for each of these measures on the specific date. Using the mouse, you can zoom in and out or click and drag to select a box to zoom in on.

## Data
The data tab is your look at all the data that is used for this dashboard. With functionalities of filtering through the data per column, you can easily traverse the data to find any particular data you are looking for e.g. the `date` column allows you to filter with symbols such as `>2020-04-13 or <= 2020-02-02 or eq 2020-04-30`
You may download this data from [here](https://github.com/TJMusiitwa/The-African-Covid-19-Dashboard/blob/master/africa_data.csv)

## Regional Trends
The regional trends tab gives you a by region outlook on the effect of the virus within specific regions. The regions were apportioned according to the [United Nations geoscheme that can be found here](https://en.wikipedia.org/wiki/United_Nations_geoscheme). Hence it is bound to be weird to find that the East African region has more countries that known in the official East African Community.
Whilst searching how to properly separate the regions, I decided to go with the United Nations option given that it is a universal body that is worldwide respected.
If you think that I can or should separate this data differently, please reach out and give me a [heads-up](mailto:jonamusiitwa@outlook.com) as to why.
