import pickle
import json
import numpy as np

pkl_name = "./data/sim_push/demos_9.pkl"
json_name = "./vec/1_task/1_iter/pos_16.json"
#json_files = "./vec"

STATE_STRING = [("joint_angles", 6), ("end_position", 3), ("end_orientation", 4)]
ACTION_STRING = [("end_angular_velocity", 3), ("joint_velocities", 6), ("end_linear_velocity", 3)]


'''
def make_demoX_and_demoU(json_name):
    result = {'demoX': [], 'demoU': []}

    demoX = np.zeros((16, 1))
    demoU = np.zeros((16, 1))

    json_file = open(json_name).read()
    contents = json.loads(json_file)
    for k,v in contents.items():
        if k in STATE_STRING:
            demoX = np.concatenate((demoX, np.array(v)), axis=1)
        elif k in ACTION_STRING:
            demoU = np.concatenate((demoU, np.array(v)), axis=1)

    result['demoX'] = demoX
    result['demoU'] = demoU

    return result
'''


with open(pkl_name, 'rb') as f:
    data = pickle.load(f)
    print("data", data)
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


