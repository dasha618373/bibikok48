import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd


diabetes = datasets.load_diabetes()
df = pd.DataFrame(data=diabetes.data, columns=diabetes.feature_names)
df['target'] = diabetes.target


def categorize_bmi(bmi):
    if bmi < 100:
        return "меньше 100"
    elif 100 <= bmi <= 200:
        return "от 100 до 200"
    else:
        return "больше 200"


df['bmi_category'] = df['target'].apply(categorize_bmi)

factor_x = 'age'
factor_y = 'bmi'


classes = df['bmi_category'].unique()


fig, ax = plt.subplots()

colors = ['g', 'r', 'b']

for i, cls in enumerate(classes):
    class_data = df[df['bmi_category'] == cls]
    ax.scatter(class_data[factor_x], class_data[factor_y],
               label=cls, c=colors[i])


ax.set_xlabel(factor_x)
ax.set_ylabel(factor_y)
ax.set_title("Диаграмма рассеяния для Diabetes (по BMI)")
ax.legend()

plt.show()