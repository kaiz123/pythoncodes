

# import numpy as np # linear algebra
# import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# import csv as csv

# from sklearn.model_selection import cross_val_score
# from sklearn.linear_model import LogisticRegression
# from sklearn.svm import SVC, LinearSVC
# from sklearn.ensemble import RandomForestClassifier

# # Input data files are available in the "../input/" directory.
# # For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

# def main():
#     train_dataset = pd.read_csv('train.csv')
#     test_dataset = pd.read_csv('test.csv')
#     #train_dataset.fillna(train_dataset.mean())
#     #test_dataset.fillna(test_dataset.mean())
   
#     print('----train dataset information-------')
#     train_dataset.info()
#     print('----test dataset information--------')
#     test_dataset.info()
#     print("------------------------------------")
#     print(train_dataset.corr()["Survived"])
#     # Filter the columns to remove ones we don't want.
#     columns = train_dataset.columns.tolist()
#     p=np.float32(train_dataset["Pclass"])
#     columns = [c for c in columns if c in ["Pclass"]]
#     #columns=columns.dropna().astype(np.float32)


# # Store the variable we'll be predicting on.
#     target = "Survived"
#     model = RandomForestClassifier(criterion='gini', 
#                              n_estimators=1000,
#                              min_samples_split=10,
#                              min_samples_leaf=1,
#                              max_features='auto',
#                              oob_score=True,
#                              random_state=1,
#                              n_jobs=-1)
#     model.fit(train_dataset[columns], train_dataset[target])
#     Y_pred = model.predict(test_dataset[columns])
    
    
#     submission = pd.DataFrame({
#         "PassengerId": test_dataset["PassengerId"],
#         "Survived": Y_pred
#     })
#     submission.to_csv('kaiztitanic.csv', index=False)

# # Any results you write to the current directory are saved as output.
#     return submission
# main()
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import csv as csv

from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

def main():
    train_dataset = pd.read_csv('train.csv')
    test_dataset = pd.read_csv('test.csv')
    #train_dataset.fillna(train_dataset.mean())
    #test_dataset.fillna(test_dataset.mean())
   
    print('----train dataset information-------')
    train_dataset.info()
    print('----test dataset information--------')
    test_dataset.info()
    print("------------------------------------")
    print(train_dataset.corr()["Survived"])
    # Filter the columns to remove ones we don't want.
    columns = train_dataset.columns.tolist()
    #p=np.float32(train_dataset["Pclass"])
    #train_dataset['Age']=train_dataset['Age'].astype(int)
    #columns = [c for c in columns if c in ["Pclass","Age"]]
    df1=train_dataset.reindex(columns=["Pclass","Age"])
    
    df1.fillna(value=0, inplace=True)

    df1=df1.astype(int,errors='ignore')
    df2=test_dataset.reindex(columns=["Pclass","Age"])
    
    df2.fillna(value=0, inplace=True)

    df2=df2.astype(int,errors='ignore')


# Store the variable we'll be predicting on.
    target = "Survived"
    model = RandomForestClassifier(criterion='gini', 
                             n_estimators=1000,
                             min_samples_split=10,
                             min_samples_leaf=1,
                             max_features='auto',
                             oob_score=True,
                             random_state=1,
                             n_jobs=-1)
    model.fit(df1, train_dataset[target])
    Y_pred = model.predict(df2)
    
    
    submission = pd.DataFrame({
        "PassengerId": test_dataset["PassengerId"],
        "Survived": Y_pred
    })
    submission.to_csv('kaiztitanic1.csv', index=False)

# Any results you write to the current directory are saved as output.
    return submission
main()