class handling_missing_values:
    def __init__(self):
        self.path ='C:\\Users\\rahul.goyal\\Desktop\\Data Science\\Machine Learning\\Projects\\Ecom_project\\Training_Raw_Files\\Good_Raw_Files'
        self.data = data
        self.log_writer = logger.App_logger()
        self.file_object = open("Ecom_logs/LogData.txt", 'a+')
        
    def createCleanDataFolder(self):
        self.dir_path = 'C:\\Users\\rahul.goyal\\Desktop\\Data Science\\Machine Learning\\Projects\\Ecom_project'
        path = os.path.join(self.dir_path, 'Clean_Data/')
        if not os.path.isdir(path):
            os.makedirs(path)
        
    def impute_missing_data(self, data, feature_name):    #### impute the missing value in the all merged dataset and save the CSV file with new data
        try:
            self.createCleanDataFolder()
            self.feature_name = feature_name
            self.mean_feature = self.data[self.feature_name].mean()
            self.data[self.feature_name] = self.data[self.feature_name].fillna(self.mean_feature)
            self.data = self.data.to_csv(self.dir_path + '/' + 'Clean_Data'+'/'+'clean.csv', index = False)
            self.log_writer.log(self.file_object, 'Imputed the missing values in the merged dataset and saving it into CSV file.')
            return self.data
        
        except Exception as e:
            self.log_writer.log(self.file_object, 'Error in imputing the missing values. Exception message:'+str(e))
            self.file_object.close()
            raise Exception()
        
    def impute_missing_values(self, file, feature_name):    #### Impute the missing values of numerical features and saving it in clean CSV file 
        self.dir_path = 'C:\\Users\\rahul.goyal\\Desktop\\Data Science\\Machine Learning\\Projects\\Ecom_project\\Clean_Data'
        self.filename = self.dir_path + '/' + file + '.csv'
        self.file = pd.read_csv(self.filename)
        self.feature_name = feature_name
        self.mean_value = self.file[self.feature_name].mean()
        self.file[self.feature_name] = self.file[self.feature_name].fillna(self.mean_value)
        self.file = self.file.to_csv(self.dir_path + '/' + 'clean.csv', index = False)
        return self.file
    
    def impute_cat_missing_data(self, file, cat_feature):    #### Imputing the missing categorical features and saving the data in clean CSV file
        try:
            self.dir_path = 'C:\\Users\\rahul.goyal\\Desktop\\Data Science\\Machine Learning\\Projects\\Ecom_project\\Clean_Data'
            self.filename = self.dir_path + '/' + file + '.csv'
            self.file = pd.read_csv(self.filename)
            self.cat_feature = cat_feature
            self.file[self.cat_feature] = self.file[self.cat_feature].fillna('other')
            self.file = self.file.to_csv(self.dir_path + '/' + 'clean.csv', index=False)
            self.log_writer.log(self.file_object, 'Imputed the categorical missing values and saving the data into Clean CSV file.')
            return self.file
        
        except Exception as e:
            self.log_writer.log(self.file_object, 'Error in imputing the categorical missing values. Exception message:' + str(e))
            self.file_object.close()
            raise Exception()