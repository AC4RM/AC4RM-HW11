from homework import *
from pytest import approx
from pathlib import Path
import urllib.request
import sqlite3
import pandas as pd
import re



def test_python():
    @time_it
    def make_list(n):
        result = []
        for i in range(n):
            result.append(i)

        return result

    output = make_list(1000)
    assert ' '.join(output.split()[:-2]) + ' ' + output.split()[-1] == "The function make_list takes seconds"


def test_sql():
    urllib.request.urlretrieve('https://github.com/AC4RM/AC4RM-dataset/blob/main/sql/data.db?raw=true', 'data.db')

    con = sqlite3.connect('data.db')

    customer_df = pd.read_sql_query(sql_query_1, con)
    invoice_df = pd.read_sql_query(sql_query_2, con)

    assert customer_df.iloc[5, 1] == '8498'
    assert customer_df.shape == (10, 2)
    assert invoice_df.iloc[3, 1] == 469.83
    assert invoice_df.shape == (7, 2)

    Path('data.db').unlink(missing_ok=True)


def test_model():
    result = train_model()
    assert all([a == approx(b, abs=1e-6) for a, b in zip(result['consequent support'].values, [0.25551601, 0.25551601, 0.25551601, 0.19349263, 0.18393493, 0.13950178])])
    Path('groceries.csv').unlink(missing_ok=True)


def test_regex():
    assert re.search(regex_pattern, 'ASDF_123') is not None
    assert re.search(regex_pattern, 'ASDF123_') is None
    assert re.search(regex_pattern, 'A-S3') is None
