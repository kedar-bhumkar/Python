import pandas as pd

def generateFile(filename, df_test):
    print(filename)
    df_test.to_csv(filename, sep=',', index=False)


def readFile(filename):
    print(filename)
    return pd.read_csv(filename, sep=',')
