import pickle
import json
import numpy as np

pkl_name = "./data/sim_push/demos_9.pkl"
json_name = "./vec/1_task/1_iter/pos_16.json"

with open(pkl_name, 'rb') as f:
    data = pickle.load(f)
    for k,v in data.items():
        print(k)
        try:
            print(v.shape)
        except:
            print(v)

json_file = open(json_name).read()
contents = json.loads(json_file)
for k,v in contents.items():
    print(k)
    try:
        print(np.array(v).shape)
    except:
        print(v)
