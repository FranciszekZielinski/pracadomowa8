import pandas as pd
import seaborn

iris = seaborn.load_dataset("iris")

writer = pd.ExcelWriter('iris.xlsx')

iris.to_excel(writer)

writer.save()
