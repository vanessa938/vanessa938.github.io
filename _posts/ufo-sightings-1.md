---
layout: post
title: UFO Sightings: Shape and Counts
---

<iframe src="{{ site.baseurl }}/assets/ufo_chart.html"
        width="100%" height="720" frameborder="0"></iframe>

**The Data:** [UFO dataset](https://github.com/UIUC-iSchool-DataViz/is445_data/raw/main/ufo-scrubbed-geocoded-time-standardized-00.csv)
**The Analysis:** [Python notebook](https://github.com/vanessa938/vanessa938.github.io/blob/main/notebooks/ufo.ipynb)

For the first plot, I'm visualizing the number of UFO sightings per year for each shape type. By hovering above a certain year for a certain shape it displays the count or number of sightings for that particular UFO shape for that year. Year is encoded as quantitative, shape is encoded as nominal, and count is encoded as quantitative. For the color scheme I chose tableau10 and it's colored by shape. I chose this specific color scheme because I like the colors and the colors are very distinct so there's no chance of the colors getting mixed up or confused. I added the column names for the dataframe as I read the file in. I extracted the year from the date variable and made a new quantitative variable called year with the year of the UFO sighting. I filtered the dataframe to only include years from 1990 and on. Then I filtered for the 8 most common shapes and kept only those shapes. 

For the second plot, I'm visualizing the total count of the top 8 shapes of UFOs for the selected years. The brush interaction with the first plot chooses what the second plot shows. The brush size can be increased or decreased, and dragged to select the time period you want to look at. When you hover over a bar it displays the shape name and the the number of sightings for that shape. Shape is encoded as nominal and sum(count) is encoded as quantitative. For the color scheme I also chose tableau10 to match with the color scheme of the first plot and it's still colored by shape type. The same data transformations applied to the dataframe used for the first plot are also used for the second plot. From the manipulated dataframe I created another dataframe selecting only year and shape.

For interactivity, the first plot uses interval brush and legend selection. The second plot uses only legend selection. The interval brush helps make my visualization more clear because the box highlights a portion of the plot, and that portion is then shown in shape counts in the second plot. The viewer can see exactly how many total counts of sightings happen for that shape in those selected years. Legend selection also makes the plot more clear as it shows the specified year, shape, and count for the first plot and shows the shape and total count for the second plot.