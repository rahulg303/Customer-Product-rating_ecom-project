class preprocessing:
    def __init__(self):
        self.path ='C:\\Users\\rahul.goyal\\Desktop\\Data Science\\Machine Learning\\Projects\\Ecom_project\\Training_Raw_Files\\Good_Raw_Files'
        self.log_writer = logger.App_logger()
        self.file_object = open("Ecom_logs/LogData.txt", 'a+')
    
    def createMregeDataDirectory(self):
        try:
            self.dir_path = 'C:\\Users\\rahul.goyal\\Desktop\\Data Science\\Machine Learning\\Projects\\Ecom_project'
            path = os.path.join(self.dir_path, 'Merge_data/')
            if not os.path.isdir(path):
                os.makedirs(path)
            self.log_writer.log(self.file_object, 'Creating Merge Data Directory.')
            
        except Exception as e:
            self.log_writer.log(self.file_object, 'Error occured in making merge data directory. Exception message:'+str(e))
            self.file_object.close()
            raise Exception()
    
    def merge_files(self, file1, file2):
        try:
            self.createMregeDataDirectory()
            self.filename1 = self.path + '/' + file1 + '.csv'
            self.file1 = pd.read_csv(self.filename1)
            self.filename2 = self.path + '/' + file2 + '.csv'
            self.file2 = pd.read_csv(self.filename2)
            self.common_col = self.file1.columns.intersection(self.file2.columns)
            self.merge_df = self.file1.merge(self.file2, on = self.common_col[0])
            self.save_merge_df = self.merge_df.to_csv(self.path + '/' +'merge_data.csv', index = False)
            shutil.copy(self.path+'/merge_data.csv', self.dir_path+'/Merge_data')
            self.log_writer.log(self.file_object, 'Data Merged successfully.')
            return self.merge_df
        
        except Exception as e:
            self.log_writer.log(self.file_object, 'Error occured while merging the data. Exception message:'+ str(e))
            self.log_writer.close()
            raise Exception()
    
        
    def remove_columns(self, final_df, columns):    #### Removes the unwanted columns
        try:
            self.data = final_df
            self.columns = columns
            self.df_useful_cols = self.data.drop(labels = self.columns, axis=1)
            self.log_writer.log(self.file_object, 'Columns removed. Exited the Preprocessing class')
            return self.df_useful_cols
        
        except Exception as e:
            self.log_writer.log(self.file_object, 'Error occured while removing the columns. Exception message:'+str(e))
            self.file_object.close()
            raise Exception()
    
    def is_null_present(self, final_df):    #### checking the null values and saving CSV file for null values
        try:
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
            self.log_writer.log(self.file_object, 'Checking Missing/Null values present.')
            return dataframe_with_null
        
        except Exception as e:
            self.log_writer.log(self.file_object, 'Error while checking null values. Exception message:'+str(e))
            self.file_object.close()
            raise Exception()
        
    def seperate_label_features(self, data, label_column_name):    #### This Method seperates the label and the features columns
        try:
            self.data = data
            self.X = self.data.drop(labels= label_column_name, axis=1)
            self.Y = self.data[label_column_name]
            self.log_writer.log(self.file_object, 'Seperated feature columns and Target feature.')
            return self.X, self.Y
        
        except Exception as e:
            self.log_writer.log(self.file_object, 'Error while seperating target and feature columns. Exception message:'+str(e))
            self.file_object.close()
            raise Exception()
            
        
    def handle_imb_dataset(self, x, y):    #### This Method handles the imbalance dataset to make it balanced
        try:
            self.rdsample = RandomOverSampler()
            self.x_sampled, self.y_sampled = self.rdsample.fit_resample(x,y)
            self.log_writer.log(self.file_object, 'Imbalanced dataset converted into balanced dataset.')
            return self.x_sampled, self.y_sampled
        
        except Exception as e:
            self.log_writer.log(self.file_object, 'Error in making balanced dataset. Exception message:'+str(e))
            self.file_object.close()
            raise Exception()
    
    def createFinalData(self):
        self.dir_path = 'C:\\Users\\rahul.goyal\\Desktop\\Data Science\\Machine Learning\\Projects\\Ecom_project'
        path = os.path.join(self.dir_path, 'Final_Data/')
        if not os.path.isdir(path):
            os.makedirs(path)
        
    def encode_cat_cols(self, data):    #### This Method encodes the categorical columns into numeric values
        try:
            self.createFinalData()
            self.data = data
            self.cat_features = [features for features in self.data.columns if self.data[features].dtypes=="O"]
            self.final_file = pd.get_dummies(self.data, columns= self.cat_features, drop_first=True)
            self.path = 'C:\\Users\\rahul.goyal\\Desktop\\Data Science\\Machine Learning\\Projects\\Ecom_project\\Final_Data'
            self.save_final_file = self.final_file.to_csv(self.path + '/' + 'preprocessed_file.csv', index = False)
            self.log_writer.log(self.file_object, 'Encoded the categorical column into numeric values.')
            return self.final_file
        
        except Exception as e:
            self.log_writer.log(self.file_object, 'Error in encoding categorical features. Exception message'+str(e))
            self.file_object.close()
            raise Exception()
    
    def feature_selection(self, xr,yr):
        try:
            self.selectkbest = SelectKBest(chi2, k=10)
            self.x_new = self.selectkbest.fit_transform(xr,yr)
            self.log_writer.log(self.file_object, 'Top 10 features selected using SelectKbest.')
            return self.x_new
        
        except Exception as e:
            self.log_writer.log(self.file_object, 'Error occured while selecting the best features. Exception message:'+str(e))
            self.file_object.close()
            raise Exception()
    
    def train_test_split(self, x_new, yr):
        try:
            self.split = train_test_split(x_new, yr, test_size=0.2)
            self.x_train, self.x_test, self.y_train, self.y_test = self.split
            self.log_writer.log(self.file_object, 'Splited the data into train test in 80:20.')
            return self.x_train, self.x_test, self.y_train, self.y_test
        
        except Exception as e:
            self.log_writer.log(self.file_object, 'Error in splitting the data. Exception message:'+str(e))
            self.file_object.close()
            raise Exception()