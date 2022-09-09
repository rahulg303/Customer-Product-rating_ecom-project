class model_finder:
    def __init__(self):
        self.dt = DecisionTreeClassifier()
        self.rf = RandomForestClassifier()
        self.log_writer = logger.App_logger()
        self.file_object = open("Ecom_logs/LogData.txt", 'a+')
        
    def dt_model(self, x_train, y_train):
        try:
            self.dt = DecisionTreeClassifier()
            self.dt.fit(x_train, y_train)
            self.log_writer.log(self.file_object, 'Training the model with Decision Tree Classifier.')
            return self.dt
        
        except Exception as e:
            self.log_writer.log(self.file_object, 'Error in training the DT model. Exception message:' + str(e))
            self.file_object.close()
            raise Exception()
    
    def rf_model(self, x_train, y_train):
        try:
            self.rf = RandomForestClassifier()
            self.rf.fit(x_train, y_train)
            self.log_writer.log(self.file_object, 'Training the model with Random Forest Classifier.')
            return self.rf
        
        except Exception as e:
            self.log_writer.log(self.file_object, 'Error in training the RF model. Exception message:' + str(e))
            self.file_object.close()
            raise Exception()        
        
    
    def get_best_model(self, x_train, x_test, y_train, y_test):
        try:
            self.decision_tree = self.dt_model(x_train, y_train)
            self.random_forest = self.rf_model(x_train, y_train)
            self.dt_score = self.decision_tree.score(x_test, y_test)
            self.rf_score = self.random_forest.score(x_test, y_test)
            if self.dt_score > self.rf_score:
                return ('Decision_Tree_model',self.dt_score.round(decimals=3)*100)
            else:
                self.log_writer.log(self.file_object, 'Selected the best model.')
                return ('Random_Forest_model',self.rf_score.round(decimals=3)*100)
            
        except Exception as e:
            self.log_writer.log(self.file_object, 'Error in selecting the best model. Exception message:' + str(e))
            self.file_object.close()
            raise Exception()