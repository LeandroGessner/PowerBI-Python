'''
Don't forget to use and activate the virtual enviroment

First create the enviroment.
    - Open VS Code, open a new terminal tab,
    type 'cmd' to change to CMD terminal
    
    - Type 'python -m venv powerbi-python' and
    wait a little bit untill the enviroment is created

    - Then navigate to the folder by typing 'cd powerbi-python\Scripts'.
    Tip: type a few letters and use the tab key to complete the word

    - Once you're in the Scripts folder, type 'activate'
    
    - After that you should see the name of the parent folder
    between brackets at the beggining of cmd line, something like this:
    (powerbi-python) C:Users\YourUser
'''

# Part 1

# First of all, import the needed libraries and the data
import sqlite3
import pandas as pd


# the path to the local of your file
path = r"C:\<YOUR_PATH_TO_DB>\car_sales.db"

with sqlite3.connect(path) as connection:
    df = pd.read_sql_query("SELECT * FROM sales", connection)


# Here we're breaking the big sales dataframe into 3 smaller dataframes, for better analysis
cars = df[
    [
        "vin",
        "car",
        "mileage",
        "license",
        "color",
        "purchase_date",
        "purchase_price",
        "investment",
    ]
]

customers = df[["vin", "customer"]]
sales = df[["vin", "sale_price", "sale_date"]]


# Part 2

# dataset is the name of the object created by Power BI
# here we're splitting the column 'customer' into two new columns,
# 'full_name' and 'email', using regex in pandas based on '<>'
# PS: this script must be executed in Power BI
dataset = dataset.assign(
    full_name = dataset["customer"].str.extract(r"([^<]+)"),
    email = dataset["customer"].str.extract(r"<([^>]+)>"),
).drop(columns=["customer"])


# Part 3

dataset[["first_name", "last_name"]] = dataset["full_name"].str.split(
    n=1, expand=True
)
dataset.drop(columns=["full_name"], inplace=True)


# Part 4

# dataset = pandas.DataFrame(color, vin)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import matplotlib.pyplot as plt

plt.style.use("seaborn")

series = dataset[dataset["color"] != ""]["color"].value_counts()
series.plot(kind="bar", color=series.index, edgecolor="black")

plt.show()
