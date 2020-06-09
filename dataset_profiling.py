
# Required libraries: Pandas, Numpy
# raw_data is must be a pandas dataframe.

def dataset_profiler(raw_data):
    df_prof=pd.DataFrame(columns=["column name","count","number of unique","number of null value","is binary?","number of 1","data type","fill rate"],index=np.arange(0,len(raw_data.columns)))
    columns = raw_data.columns
    ctr=0
    for column in columns:
        df_prof["column name"][ctr]=column
        df_prof["count"][ctr]=raw_data[column].count()
        df_prof["number of unique"][ctr]=raw_data[column].nunique()
        df_prof["number of null value"][ctr] = raw_data[column].isnull().sum()
        df_prof["is binary?"][ctr]=False
        df_prof["number of 1"][ctr]=0
        df_prof["data type"][ctr] = str(raw_data[column].dtype).split('(')[0]
        df_prof["fill rate"][ctr] = raw_data[column].count()/len(raw_data)
        if raw_data[column].dropna().value_counts().index.isin([0,1]).all()==True and raw_data[column].nunique()==2:
            df_prof["is binary?"][ctr]=True
            df_prof["number of 1"][ctr]=(raw_data[column]==1).sum()
        ctr+=1
    return df_prof

