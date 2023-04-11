import numpy as np
import pandas as pd
import altair as alt

Low = 100

High = 100000

# Compute x^2 + y^2 across a 2D grid
x, y = np.meshgrid(range(Low, High, 5000), range(100, 0, -10))
z = x * y

# Convert this grid to columnar data expected by Altair
model = pd.DataFrame({'x': x.ravel(),
                     'y': y.ravel(),
                     'z': z.ravel()})

alt.Chart(model).mark_rect().encode(
    x='x:O',
    y='y:O',
    color='z:Q',
    tooltip='z:Q'
)
