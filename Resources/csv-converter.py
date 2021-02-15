import pandas as pd
import os

path = os.path.join("Resources","cities.csv")
csv = pd.read_csv(path)

csv.to_html(buf=os.path.join("Resources", "assets", "cities-data.html"))