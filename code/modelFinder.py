class model_finder:
    def __init__(self):
        self.dt = DecisionTreeClassifier()
        self.rf = RandomForestClassifier()
        
    def dt_model(self, x_train, y_train):
        self.dt = DecisionTreeClassifier()
        self.dt.fit(x_train, y_train)
        return self.dt
    
    def rf_model(self, x_train, y_train):
        self.rf = RandomForestClassifier()
        self.rf.fit(x_train, y_train)
        return self.rf
    
    def get_best_model(self, x_train, x_test, y_train, y_test):
        self.decision_tree = self.dt_model(x_train, y_train)
        self.random_forest = self.rf_model(x_train, y_train)
        self.dt_score = self.decision_tree.score(x_test, y_test)
        self.rf_score = self.random_forest.score(x_test, y_test)
        if self.dt_score > self.rf_score:
            return ('Decision_Tree_model',self.dt_score.round(decimals=3)*100)
        else:
             return ('Random_Forest_model',self.rf_score.round(decimals=3)*100)