class preprocessing:
    def __init__(self):
        self.path ='C:\\Users\\rahul.goyal\\Desktop\\Data Science\\Machine Learning\\Projects\\Ecom_project\\Training_Raw_Files\\Good_Raw_Files'
    
    def createMregeDataDirectory(self):
        self.dir_path = 'C:\\Users\\rahul.goyal\\Desktop\\Data Science\\Machine Learning\\Projects\\Ecom_project'
        path = os.path.join(self.dir_path, 'Merge_data/')
        if not os.path.isdir(path):
            os.makedirs(path)
    
    def merge_files(self, file1, file2):
        self.createMregeDataDirectory()
        self.filename1 = self.path + '/' + file1 + '.csv'
        self.file1 = pd.read_csv(self.filename1)
        self.filename2 = self.path + '/' + file2 + '.csv'
        self.file2 = pd.read_csv(self.filename2)
        self.common_col = self.file1.columns.intersection(self.file2.columns)
        self.merge_df = self.file1.merge(self.file2, on = self.common_col[0])
        self.save_merge_df = self.merge_df.to_csv(self.path + '/' +'merge_data.csv', index = False)
        shutil.copy(self.path+'/merge_data.csv', self.dir_path+'/Merge_data')
        return self.merge_df
    
        
    def remove_columns(self, final_df, columns):    #### Removes the unwanted columns
        self.data = final_df
        self.columns = columns
        self.df_useful_cols = self.data.drop(labels = self.columns, axis=1)
        return self.df_useful_cols
    
    def is_null_present(self, final_df):    #### checking the null values and saving CSV file for null values
        null_present = False
        cols_with_missing_values = []
        cols = final_df.columns
        null_counts = final_df.isnull().sum()
        for i in range(len(null_counts)):
             if null_counts[i]>0:
                    null_present = True
                    cols_with_missing_values.append(cols[i])
                    
        if (null_present):
            dataframe_with_null = pd.DataFrame()
            dataframe_with_null['columns'] = final_df.columns
            dataframe_with_null['missing values count'] = np.asarray(final_df.isna().sum())
            dataframe_with_null.to_csv('null_values.csv', index=False)
            return dataframe_with_null
        
    def seperate_label_features(self, data, label_column_name):    #### This Method seperates the label and the features columns
        self.data = data
        self.X = self.data.drop(labels= label_column_name, axis=1)
        self.Y = self.data[label_column_name]
        return self.X, self.Y
        
    def handle_imb_dataset(self, x, y):    #### This Method handles the imbalance dataset to make it balanced
        self.rdsample = RandomOverSampler()
        self.x_sampled, self.y_sampled = self.rdsample.fit_resample(x,y)
        return self.x_sampled, self.y_sampled
    
    def createFinalData(self):
        self.dir_path = 'C:\\Users\\rahul.goyal\\Desktop\\Data Science\\Machine Learning\\Projects\\Ecom_project'
        path = os.path.join(self.dir_path, 'Final_Data/')
        if not os.path.isdir(path):
            os.makedirs(path)
        
    def encode_cat_cols(self, data):    #### This Method encodes the categorical columns into numeric values
        self.createFinalData()
        self.data = data
        self.cat_features = [features for features in self.data.columns if self.data[features].dtypes=="O"]
        self.final_file = pd.get_dummies(self.data, columns= self.cat_features, drop_first=True)
        self.path = 'C:\\Users\\rahul.goyal\\Desktop\\Data Science\\Machine Learning\\Projects\\Ecom_project\\Final_Data'
        self.save_final_file = self.final_file.to_csv(self.path + '/' + 'preprocessed_file.csv', index = False)
        return self.final_file
    
    def feature_selection(self, xr,yr):
        self.selectkbest = SelectKBest(chi2, k=10)
        self.x_new = self.selectkbest.fit_transform(xr,yr)
        return self.x_new
    
    def train_test_split(self, x_new, yr):
        self.split = train_test_split(x_new, yr, test_size=0.2)
        self.x_train, self.x_test, self.y_train, self.y_test = self.split
        return self.x_train, self.x_test, self.y_train, self.y_test       