import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Data/percentages.csv")
data = data.drop(["neighborhood", "most_recent_year", "building_class_category", "sale_price_increase"], axis=1)
print(data)
plt.scatter(data.drop(["gentrifying"], axis=1), data.drop(["duration"], axis=1))
plt.show()