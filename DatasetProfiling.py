class DatasetProfiling:
    
    def __init__(self,dataset):
        self.df=pd.read_csv(dataset, sep='|',encoding='iso8859_9', error_bad_lines=False,low_memory=False)
    
    def dataset_abstract(self):
        raw_data=self.df
        df_prof=pd.DataFrame(columns=["column name","count","number of unique","number of null value","is binary?","number of 1","data type","fill rate","range","most_freq","variance", "modele_girer_mi ","comments"],index=np.arange(0,len(raw_data.columns)))
        columns = raw_data.columns
        ctr=0
        var_values=raw_data.var()
        max_values=raw_data.max(axis=0)
        min_values=raw_data.min(axis=0)
        for column in columns:
            df_prof["column name"][ctr]=column
            df_prof["count"][ctr]=raw_data[column].count()
            df_prof["number of unique"][ctr]=raw_data[column].nunique()
            df_prof["number of null value"][ctr] = raw_data[column].isnull().sum()
            df_prof["is binary?"][ctr]=False
            df_prof["number of 1"][ctr]=0
            df_prof["data type"][ctr] = str(raw_data[column].dtype).split('(')[0]
            df_prof["fill rate"][ctr] = raw_data[column].count()/len(raw_data)
            ####
            if column in var_values.index :
                df_prof['variance'][ctr]= var_values[column]
            if column in min_values.index:
                df_prof['range'][ctr]= "[{} - {}]".format( min_values[column] , max_values[column] )
            try:
                df_prof['most_freq'][ctr]=raw_data[column].value_counts().index[0] #column'un mode'unu kaydeder
            except Exception as e:
                pass
            ###
            if raw_data[column].dropna().value_counts().index.isin([0,1]).all()==True and raw_data[column].nunique()==2:
                df_prof["is binary?"][ctr]=True
                df_prof["number of 1"][ctr]=(raw_data[column]==1).sum()
            ctr+=1
        return df_prof
    
    def important_features(self):
        raw_data=self.df
        df_impt=pd.DataFrame(columns=["column name","count","number of unique","number of null value","is binary?","number of 1","data type","fill rate","range","most_freq","variance", "modele_girer_mi ","comments"],index=np.arange(0,len(raw_data.columns)))
        columns = raw_data.columns
        ctr=0
        var_values=raw_data.var()
        max_values=raw_data.max(axis=0)
        min_values=raw_data.min(axis=0)
        for column in columns:
            if (raw_data[column].nunique() not in [0,1]):
                df_impt["column name"][ctr]=column
                df_impt["count"][ctr]=raw_data[column].count()
                df_impt["number of unique"][ctr]=raw_data[column].nunique()
                df_impt["number of null value"][ctr] = raw_data[column].isnull().sum()
                df_impt["is binary?"][ctr]=False
                df_impt["number of 1"][ctr]=0
                df_impt["data type"][ctr] = str(raw_data[column].dtype).split('(')[0]
                df_impt["fill rate"][ctr] = raw_data[column].count()/len(raw_data)
              ####
                if column in var_values.index :
                    df_impt['variance'][ctr]= var_values[column]
                if column in min_values.index:
                    df_impt['range'][ctr]= "[{} - {}]".format( min_values[column] , max_values[column] )
                try:
                    df_impt['most_freq'][ctr]=raw_data[column].value_counts().index[0] #column'un mode'unu kaydeder
                except Exception as e:
                    pass
              ###
                if raw_data[column].dropna().value_counts().index.isin([0,1]).all()==True and raw_data[column].nunique()==2:
                    df_impt["is binary?"][ctr]=True
                    df_impt["number of 1"][ctr]=(raw_data[column]==1).sum()
                else:
                    pass
            ctr+=1
        return df_impt.dropna(how="all",axis=0).reset_index(drop=True)
    
