from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
from storage import save_model
from registry import register_model

def train_model(name,csv_path,target):
    df=pd.read_csv(csv_path)
    X,y=df.drop(columns=[target]),df[target]
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
    model=RandomForestClassifier()
    model.fit(X_train,y_train)
    acc=accuracy_score(y_test,model.predict(X_test))
    path=save_model(model,name)
    register_model(name,"v1",path)
    return {"model_name":name,"accuracy":acc}
