def overview(dataframe):
    #docstring
    '''
    Read a csv file into a DataFrame.
    Print first 5 rows of data.
    Print datatype for each column.
    Print number of NULL/NaN values for each column.
    Print summary data.
    
    Return:
    data, rtype: DataFrame
    '''
    print("The first 5 rows of data are:\n", df.head())
    print("\n")
    print("The (Row,Column) is:\n", df.shape)
    print("\n")
    print("Data type of each column:\n", df.dtypes)
    print("\n")
    print("The number of null values in each column are:\n", df.isnull().sum())
    print("\n")
    print("Summary of data:\n", df.describe())
    return 

overview(df)
