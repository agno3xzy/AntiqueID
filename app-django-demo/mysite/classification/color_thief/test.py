from colorthief import ColorThief

color_thief = ColorThief('profile.jpg')
# get the dominant color
dominant_color = color_thief.get_color(quality=1)
print(dominant_color)
# build a color palette
palette = color_thief.get_palette(color_count=6)
print(palette)