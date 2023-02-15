"""Write Color-Scales from plotly-colors module"""

from plotly import colors


for key in colors.PLOTLY_SCALES.keys():
    print(key)
