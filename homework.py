import urllib.request
import pandas as pd


def time_it(func):
    # Your code here
    pass


sql_query_1 = '''

              '''

sql_query_2 = '''

              '''


def train_model():

    urllib.request.urlretrieve("https://raw.githubusercontent.com/AC4RM/AC4RM-dataset/main/homework/groceries.csv", "groceries.csv")
    df = pd.DataFrame(columns=['order_id', 'item'])

    with open("groceries.csv") as f:
        # Your code here
        pass


regex_pattern = ""
