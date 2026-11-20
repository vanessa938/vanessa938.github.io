import pandas as pd
import streamlit as st
import altair as alt

st.set_page_config(page_title="Bigfoot Sightings", layout="wide")

URL = "https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/bfro_reports_fall2022.csv"

@st.cache_data
def load():
    df = pd.read_csv(URL, usecols=["state", "county", "season", "title", "latitude", "longitude", "date", "number", "classification", "temperature_high", "humidity"])
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    return df

df = load()

st.title("Bigfoot Sightings in North America")
st.caption("Data: Bigfoot Field Researchers Organization (BFRO) Reports via UIUC IS445 DataViz")

st.header("Visualization 1: Map of Bigfoot Sightings Reports in North America")

geo = df.dropna(subset=["latitude", "longitude", "year"])
geo = geo[(geo.longitude < -60) & (geo.latitude > 15)]

c1, c2 = st.columns(2)
yr_min, yr_max = int(geo.year.min()), int(geo.year.max())
years = c1.slider("Year Range", yr_min, yr_max, (1990, yr_max))
classes = c2.multiselect("Report Classification", sorted(geo.classification.unique()), default=["Class A", "Class B"])

sub = geo[geo.year.between(*years) & geo.classification.isin(classes)]

states = alt.topo_feature("https://cdn.jsdelivr.net/npm/vega-datasets@2/data/us-10m.json", "states")
base = alt.Chart(states).mark_geoshape(fill="#f0f0f0", stroke="white").project("albersUsa")

points = alt.Chart(sub).mark_circle(size=25, opacity=0.6).encode(
    longitude="longitude:Q",
    latitude="latitude:Q",
    color=alt.Color(
        "classification:N", title="Class", scale=alt.Scale(
            domain=["Class A", "Class B", "Class C"],
            range=["#d95f02", "#1b9e77", "#7570b3"]
        )
    ),
    tooltip=["title:N", "state:N", "county:N", "date:T", "classification:N"],
).project(
    "albersUsa"
)

st.altair_chart((base + points).properties(width=800, height=450), use_container_width=True)
st.write(f"Showing {len(sub):,} reports.")
st.write("h")
# describes what features you are highlighting with your viz, the design choices you made (choices of scales, marks, colors, etc) to visualize your data appropriately, and what you would like to change if you had more time

st.header("Visualization 2: When Sightings Are Reported")

by_month = (df.dropna(subset=["month"]).query("season != 'Unknown'").groupby(["month", "season"]).size().reset_index(name="reports"))
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
by_month["month_name"] = by_month["month"].astype(int).map(lambda m: month_names[m-1])

sel = alt.selection_point(fields=["season"], bind="legend")
chart2 = alt.Chart(by_month).mark_bar().encode(
    x=alt.X("month_name:N", sort=month_names, title="Month"),
    y=alt.Y("reports:Q", title="Number of reports"),
    color=alt.Color(
        "season:N", 
        title="Season (click to filter)", 
        scale=alt.Scale(
            domain=["Winter", "Spring", "Summer", "Fall"], 
            range=["#4c78a8","#54a24b","#f58518","#b279a2"])),
    opacity=alt.condition(sel, alt.value(1), alt.value(0.15)),
    tooltip=["month_name:N", "season:N", "reports:Q"],
).add_params(sel).properties(height=400)
st.altair_chart(chart2, use_container_width=True)
st.write("a")
# describes what features you are highlighting with your viz, the design choices you made (choices of scales, marks, colors, etc) to visualize your data appropriately, and what you would like to change if you had more time