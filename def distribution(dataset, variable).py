def distribution(dataset, variable):
    '''
    Args:
        dataset: Include the DataFrame here
        variable: Include the column from dataframe used for color encoding
    Returns:
        sns pairplot with color encoding
    '''
    g = sns.pairplot(data = dataset, hue = variable)
    g.fig.suptitle('Graph showing distribution between scores and {}'.format(variable), fontsize=20)
    g.fig.subplots_adjust(top=0.9)
    return g
