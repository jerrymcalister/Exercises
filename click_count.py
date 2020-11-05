import pandas as pd
from pandas import DataFrame

counts = [
    "60, foo.org",
    "50, www.google.com",
    "40, mail.yahoo.com",
    "30, search.yahoo.com",
    "20, dug.digg.net",
    "10, reddit.com"
]


def main():

    df = DataFrame()
    columns = ["count", "domain", "suffix"]

    for line in counts:
        click_count = int(line.split(",")[0])       # get the click count
        url_split = line.split(", ")[1]             # get the url
        url_split = url_split.split(".")            # split the url by '.'
        url_split = url_split[-2:]                  # get the last two times domain and suffix
        url_split.insert(0, click_count)            # add count back to list
        a_series = pd.Series(url_split)             # convert list to a pandas series, then
        df = df.append(a_series, ignore_index=True) # add the series to the dataFrame

    df.columns = columns
    print(df)

    # groupBy and sum
    print(df.groupby(['domain']).sum())
    print(df.groupby(['suffix']).sum())

    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
