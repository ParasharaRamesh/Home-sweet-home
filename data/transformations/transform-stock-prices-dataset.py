import pandas as pd

def transform_stock_prices(inp_path, out_path):
    '''
    Take the original sg-stock-prices.csv and transform it to create a new transformed sg-stock-prices.csv which has the following columns

    date, stock_price_indicator

    Where date is of format "year-month" and stock_price_indicator is a number

    :param inp_path: input csv path
    :param out_path: output csv path for storing the new dataframe
    :return: transformed dataframe
    '''
    pass


if __name__ == '__main__':
    inp_path = "../../datasets/auxiliary-data/sg-stock-prices.csv"
    out_path = "../../datasets/transformed/sg-stock-prices.csv"
    print(transform_stock_prices(inp_path, out_path))
