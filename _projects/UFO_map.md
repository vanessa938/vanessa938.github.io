---
layout: post
title: "UFO Reportings"
name: ""
tools: [Python, Altair, vega-lite]
custom_js:
  - vega.min
  - vega-lite.min
  - vega-embed.min
  - justcharts
---

<vegachart schema-url="{{ site.baseurl }}/assets/json/ufo_chart_2.json" style="width: 100%"></vegachart>

For the first plot, I'm visualizing sightings across the US for each state. By hovering above a point it displays the city, state, year, and shape of the UFO sighting. There's a interactive slider that lets you choose the year you want to display on the map. Longitude is encoded as quantitative, latitude is also encoded as quantitative, city is encoded as nominal, state is also encoded as nominal, year is encoded as quantitative, and shape is encoded as nominal. For the color scheme I chose tableau10 and it's colored by shape. I chose this specific color scheme because it's good for unordered categories and the colors are very distinct so there's no chance of the colors getting mixed up or confused. I added the column names for the dataframe as I read the file in. I changed the latitude and longitude variable to numeric variables. I extracted the year from the date variable and made a new quantitative variable called year with the year of the UFO sighting. I filtered country to only include sightings that occured in the US and had a value for the state variable. I filtered for the 6 most common shapes and kept only those shapes; if there was an NA value it was filled with "other". Then I grouped by states and selected the top 15 states with UFO sightings.

For the second plot, I'm visualizing . The brush interaction with the first plot chooses what the second plot shows. The brush size can be increased or decreased, and dragged to select the time period you want to look at. When you hover over a bar it displays the shape name and the the number of sightings for that shape. Sightings is encoded as quantitative and state is encoded as nominal. For the color scheme I chose #d95f02a for the selected state and #7a7a7a for the unselected states so the audience can easily visually differentiate between what state is filtered and what states are not. The same data transformations applied to the dataframe used for the first plot are also used for the second plot.

For interactivity, the first plot uses interval brush and shape selection. The second plot only uses interval brush. The interval brush helps make my visualization more clear because the box highlights a portion of the plot, and that portion is then shown in shape counts in the second plot. The viewer can see exactly how many total counts of sightings happen for that shape in those selected years. Shape selection also makes the plot more clear as it shows the specified year, shape, and count for the first plot and shows the shape and total count for the second plot.

<div class="left">
{% include elements/button.html link="https://github.com/UIUC-iSchool-DataViz/is445_data/raw/main/ufo-scrubbed-geocoded-time-standardized-00.csv" text="The Data" %}
</div>

<div class="right">
{% include elements/button.html link="https://github.com/vanessa938/vanessa938.github.io/blob/main/python_notebooks/ufo_sightings_2.ipynb" text="The Analysis" %}
</div>