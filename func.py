def nullity(data):
    df=pd.DataFrame(columns=['dataFeatures','dataType','null','nullPct','unique','uniqueSample'])
    df['dataFeatures']=data.columns
    df['dataType']=[i for i in data.dtypes]
    df['null']=df['dataFeatures'].apply(lambda x: sum(data[x].isna()))
    df['nullPct']=df['null'].apply(lambda x: round((x/len(data))*100,2))
    df['unique']=df['dataFeatures'].apply(lambda x: data[x].nunique())
    df['uniqueSample']=df['dataFeatures'].apply(lambda x: data[x].unique())
    print('data count : {}'.format(len(data)))
    return df