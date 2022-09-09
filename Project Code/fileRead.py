class data_getter:
    def __init__(self):
        self.path = 'C:\\Users\\rahul.goyal\\Desktop\\Data Science\\Machine Learning\\Projects\\Ecom_project\\Training_Raw_Files\\Good_Raw_Files' 
        self.log_writer = logger.App_logger()
        self.file_object = open("Ecom_logs/LogData.txt", 'a+')
        
    def read_files(self, filename):
        self.log_writer.log(self.file_object, "Start reading file")
        try:
            self.all_files = self.path + '/' + filename + '.csv'
            self.data = pd.read_csv(self.all_files)
            self.log_writer.log(self.file_object, 'Data load successful. Exited the data_getter class.')
            return self.data
        
        except Exception as e:
            self.log_writer.log(self.file_object, 'Exception occurred in read_files method of data_getter class. Exception message:' + str(e))
            self.log_writer.log(self.file_object, 'Data load unsuccessful. Exited the data_getter class.')
            self.file_object.close()
            raise Exception() 