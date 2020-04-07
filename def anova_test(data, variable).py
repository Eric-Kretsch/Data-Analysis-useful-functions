def anova_test(data, variable):
    '''
    Args: 
        data = (DataFrame)
        variable = Categorical column used for 1-way ANOVA test
    Returns: Nothing
    '''
    x = ['numerical_data']
    for i,k in enumerate(x):
        lm = ols('{} ~ {}'.format(x[i],variable), data=data).fit()
        table = sm.stats.anova_lm(lm)
        print("P-value for 1-way ANOVA test between {} and {} is ".format(x[i],variable),table.loc[variable,'PR(>F)'])
