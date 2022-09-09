class file_operation:
    def __init__(self):
        self.model_directory = 'C:\\Users\\rahul.goyal\\Desktop\\Data Science\\Machine Learning\\Projects\\Ecom_project'
        self.log_writer = logger.App_logger()
        self.file_object = open("Ecom_logs/LogData.txt", 'a+')
    
    def createmodelfolder(self):
        path = os.path.join(self.model_directory, 'Models/')
        if not os.path.isdir(path):
            os.makedirs(path)
    
    def save_model(self, model, filename):
        try:
            self.createmodelfolder()
            self.dir = 'C:\\Users\\rahul.goyal\\Desktop\\Data Science\\Machine Learning\\Projects\\Ecom_project\\Models'
            path = os.path.join(self.dir, filename)
            if not os.path.isdir(path):
                os.makedirs(path)
                   
            with open(path + '/' + filename + '.pkl', 'wb') as f:
                pickle.dump(model,f)
            self.log_writer.log(self.file_object, 'Model saved.')
            
        except Exception as e:
            self.log_writer.log(self.file_object, 'Error in saving the models. Exception message:' + str(e))
            self.file_object.close()
            raise Exception()
            
    def load_model(self, filename):
        self.dir = 'C:\\Users\\rahul.goyal\\Desktop\\Data Science\\Machine Learning\\Projects\\Ecom_project\\Models'
        with open(self.dir + '/' + filename + '/' + filename + '.pkl', 'rb') as f:
            return pickle.load(f)