---
layout: post
title: "UFO Sightings: Shape and Counts"
name: "UFO Sightings"
tools: [Python, Altair, vega-lite]
custom_js:
  - vega.min
  - vega-lite.min
  - vega-embed.min
  - justcharts
---

<vegachart schema-url="{{ site.baseurl }}/assets/json/ufo_chart.json" style="width: 100%"></vegachart>

For the first plot, I'm visualizing the number of UFO sightings per year for each shape type. It's a stacked area chart, in alphabetical order, where the band thickness of each shape shows its count and the total height of all the bands shows the overall number of sightings. The thinner the band the less sightings there are for that shape, and vice versa. By hovering above a certain year for a certain shape it displays the count or number of sightings for that particular UFO shape for that year. Year is encoded as quantitative, shape is encoded as nominal, and count is encoded as quantitative. For the color scheme I chose tableau10 and it's colored by shape. I chose this specific color scheme because it's good for unordered categories and the colors are very distinct so there's no chance of the colors getting mixed up or confused. I added the column names for the dataframe as I read the file in. I extracted the year from the date variable and made a new quantitative variable called year with the year of the UFO sighting. I filtered the dataframe to only include years from 1990 and on. Then I filtered for the 8 most common shapes and kept only those shapes. 

For the second plot, I'm visualizing the total count of the top 8 shapes of UFOs for the selected years. The brush interaction with the first plot chooses what the second plot shows. The brush size can be increased or decreased, and dragged to select the time period you want to look at. When you hover over a bar it displays the shape name and the the total number of sightings for that shape in that time period. Shape is encoded as nominal and sum(count) is encoded as quantitative. For the color scheme I also chose tableau10 to match with the color scheme of the first plot and it's still colored by shape type. The same data transformations applied to the dataframe used for the first plot are also used for the second plot. Using the manipulated dataframe I aggregated it by grouping by year and shape.

For interactivity, the first plot uses brush selection (interval selection) and shape selection (point selection). The second plot only uses brush selection. The brush selection helps make my visualization more clear because the brush highlights a portion of the plot, and that portion is then shown in total shape counts in the second plot. The viewer can see exactly how many total counts of sightings happen for that shape in those selected years. Shape selection also makes the plot more clear as it shows the specified year, shape, and count for the first plot and shows the shape and total count for the second plot.

<div class="left">
{% include elements/button.html link="https://github.com/UIUC-iSchool-DataViz/is445_data/raw/main/ufo-scrubbed-geocoded-time-standardized-00.csv" text="The Data" %}
</div>

<div class="right">
{% include elements/button.html link="https://github.com/vanessa938/vanessa938.github.io/blob/main/python_notebooks/ufo_sightings.ipynb" text="The Analysis" %}
</div>