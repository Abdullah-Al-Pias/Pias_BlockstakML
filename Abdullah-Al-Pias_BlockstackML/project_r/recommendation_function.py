import pandas as pd
import joblib


def get_recommendation(data, model_path):
    sample_dataset = pd.DataFrame(data, index=[0])
    columns_to_encode = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome']
    sample_dataset_encoded = pd.get_dummies(sample_dataset, columns=columns_to_encode)
    new_dataset = pd.read_csv("column_names.csv")
    for col, val in new_dataset.items():
        if col in sample_dataset_encoded.columns.tolist():
            new_dataset[col] = sample_dataset_encoded[col]

    
    model = joblib.load(model_path)
    target = model.predict(new_dataset.drop('y_yes', axis=1))
    # if target=="True"
    target = "no" if target[0] == 'True' else "yes"  ## one hot encoded in this way
    return target


# # Sample data with string values
# data = {
#     'age': 30,
#     'job': 'blue-collar',
#     'marital': 'married',
#     'education': 'basic.9y',
#     'default': 'no',
#     'balance': 1000,
#     'housing': 'no',
#     'loan': 'no',
#     'contact': 'cellular',
#     'day': 5,
#     'month': 'mar',
#     'duration': 200,
#     'campaign': 1,
#     'pdays': -1,
#     'previous': 0,
#     'poutcome': 'nonexistent'
# }

# output = get_recommendation(data, "decision_tree.pkl") 
# print(output)       