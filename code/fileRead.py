class data_getter:
    def __init__(self):
        self.path = 'C:\\Users\\rahul.goyal\\Desktop\\Data Science\\Machine Learning\\Projects\\Ecom_project\\Training_Raw_Files\\Good_Raw_Files'
        
    def read_files(self, filename):
        self.all_files = self.path + '/' + filename + '.csv'
        self.data = pd.read_csv(self.all_files)
        return self.data