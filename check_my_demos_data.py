import pickle
from os.path import join

pkl_dir = "./my_pick_and_place"
demos_file = "demos_0.pkl"

with open(join(pkl_dir, demos_file), 'rb') as f:
    data = pickle.load(f)
    print("data", data)
    for k,v in data.items():
        print(k)
        try:
            print(v.shape)
        except:
            print(k)
