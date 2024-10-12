import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar
from osmnx import features_from_place
from geopandas import GeoSeries
from shapely import Point

fig, ax = plt.subplots()
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_facecolor("ivory")
ax.set_xlim(58.12, 58.20)
ax.set_ylim(54.90, 54.95)

place = "Ust-Katav"
water_gdf = features_from_place(place, tags={"natural": "water"})
forest_gdf = features_from_place(place, {"natural": ["wood", "tree", "tree_row"]})
landuse_gdf = features_from_place(place, tags={"landuse": True})
highway_gdf = features_from_place(place, tags={"highway": ["secondary", "tertiary"]})

forest_gdf.plot(ax=ax, facecolor="palegreen")
landuse_gdf.plot(ax=ax, facecolor="lightgray", edgecolor="gray")
water_gdf.plot(ax=ax, facecolor="lightskyblue", edgecolor="deepskyblue")
highway_gdf.plot(ax=ax, color="palegoldenrod", linewidth=3)

points = GeoSeries([Point(58.12, 54.90), Point(59.12, 54.90)], crs=4326).to_crs(32619)

scalebar = ScaleBar(
    dx=points[0].distance(points[1]),
    bar_style="geography",
    length_fraction=1,
    width_fraction=0.03,
)
ax.add_artist(scalebar)
fig.savefig("bar_style_geography.png", dpi=60, bbox_inches="tight")
