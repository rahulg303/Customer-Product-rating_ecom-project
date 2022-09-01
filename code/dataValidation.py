class Raw_data_validation:
    def __init__(self):
        self.Batch_directory = 'C:\\Users\\rahul.goyal\\Desktop\\Data Science\\Machine Learning\\Projects/'
                
    def manualRegexCreation(self):
        regex = 'olist'
        return regex
    
    def createdirectoryforGoodBadData(self):
        path = os.path.join(self.Batch_directory, 'Ecom_project/', 'Training_Raw_files/','Good_Raw_files')
        if not os.path.isdir(path):
            os.makedirs(path)
            
        path = os.path.join(self.Batch_directory, 'Ecom_project/', 'Training_Raw_files/','Bad_Raw_files')
        if not os.path.isdir(path):
            os.makedirs(path)
        
    def validationFileName(self, regex):
        self.createdirectoryforGoodBadData()
        self.directory = 'C:\\Users\\rahul.goyal\\Desktop\\Data Science\\Machine Learning\\Projects\\dataset_files/'
        onlyfiles = [f for f in listdir(self.directory)]
        for filename in onlyfiles:
            if (re.match(regex, filename)):
                shutil.copy(self.directory+filename, self.Batch_directory+'Ecom_project'+'/Training_Raw_Files'+'/Good_Raw_Files'+'/'+filename)