# Random Walks
1. [ ] Write Project outline
1. [ ] Learn about random walks and how to detect them
1. [ ] Apply new project structure
1. [ ] Use sphinx to document the project
1. [ ] Learn about XGBoost since 
    
    ``` python
     
        from xgboost import XGBRegressor 
    
        xgb = XGBRegressor()
        xgb.fit(X_train_scaled, y_train)
        
        plotModelResults(xgb, 
                         X_train=X_train_scaled, 
                         X_test=X_test_scaled, 
        plot_intervals=True, plot_anomalies=True)
    ```
    yielded the best baseline for the time series analysed in in https://medium.com/open-machine-learning-course/open-machine-learning-course-topic-9-time-series-analysis-in-python-a270cb05e0b3

### Resources
* https://machinelearningmastery.com/gentle-introduction-random-walk-times-series-forecasting-python/
* https://ai.stanford.edu/%7Eang/papers/icml04-apprentice.pdf
* http://sameersingh.org/files/papers/anchors-aaai18.pdf
* https://arxiv.org/pdf/1602.04938.pdf