class file_operation:
    def __init__(self):
        self.model_directory = 'C:\\Users\\rahul.goyal\\Desktop\\Data Science\\Machine Learning\\Projects\\Ecom_project'
    
    def createmodelfolder(self):
        path = os.path.join(self.model_directory, 'Models/')
        if not os.path.isdir(path):
            os.makedirs(path)
    
    def save_model(self, model, filename):
        self.createmodelfolder()
        self.dir = 'C:\\Users\\rahul.goyal\\Desktop\\Data Science\\Machine Learning\\Projects\\Ecom_project\\Models'
        path = os.path.join(self.dir, filename)
        if not os.path.isdir(path):
            os.makedirs(path)
            
        with open(path + '/' + filename + '.pkl', 'wb') as f:
            pickle.dump(model,f)
            
    def load_model(self, filename):
        self.dir = 'C:\\Users\\rahul.goyal\\Desktop\\Data Science\\Machine Learning\\Projects\\Ecom_project\\Models'
        with open(self.dir + '/' + filename + '/' + filename + '.pkl', 'rb') as f:
            return pickle.load(f)