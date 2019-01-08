import pickle
import json
import numpy as np
import os
from os.path import join
import shutil

#pkl_name = "./data/sim_push/demos_9.pkl"
#json_name = "./vec/1_task/1_iter/pos_16.json"

# FILES / JSON_NAME
pkl_dir = "./my_pick_and_place"
pkl_prefix = "demos_"

json_files = "./vec"
json_name = "pos_16.json"


# CONSTANTS
STATE_STRING = ["joint_angles", "end_position", "end_orientation"]
STATE_LEN = [6, 3, 4]
ACTION_STRING = ["end_angular_velocity", "joint_velocities", "end_linear_velocity"]
ACTION_LEN = [3, 6, 3]

TOTAL_STATE_LEN = sum(STATE_LEN)
TOTAL_ACTION_LEN = sum(ACTION_LEN)

FRAME_NUM = 16


def make_demoX_and_demoU(j_file):
    result = {'demoX': [], 'demoU': []}

    demoX = np.zeros((FRAME_NUM, TOTAL_STATE_LEN))
    demoU = np.zeros((FRAME_NUM, TOTAL_ACTION_LEN))

    json_file = open(j_file).read()
    contents = json.loads(json_file)
    for k,v in contents.items():
        if k in STATE_STRING:
            idx = STATE_STRING.index(k)
            start_idx = sum(STATE_LEN[:idx])
            final_idx = start_idx + STATE_LEN[idx]

            demoX[:, start_idx:final_idx] = np.array(v)
        elif k in ACTION_STRING:
            idx = ACTION_STRING.index(k)
            start_idx = sum(ACTION_LEN[:idx])
            final_idx = start_idx + ACTION_LEN[idx]

            demoU[:, start_idx:final_idx] = np.array(v)

    result['demoX'] = demoX
    result['demoU'] = demoU

    return result


if __name__ == "__main__":
    '''
    if os.path.exists(pkl_dir):
        #os.rmdir(pkl_dir)
        shutil.rmtree(pkl_dir, ignore_errors=True)
    '''
    if os.path.exists("my_pick_and_place/*.pkl"):
        os.remove("my_pick_and_place/*.pkl")
    #os.mkdir(pkl_dir)

    # [1_task, 2_task, ... ]
    json_files = [join(json_files, f) for f in sorted(os.listdir(json_files), key=(lambda x: int(x.split("_")[0])))]

    for n, f in enumerate(json_files):
        # [1_iter, ... ]
        # ["...../pos_16.json", ... ]
        jsons = [join(join(f, k), json_name) for k in os.listdir(f)]
        #print(jsons) # ['./vec/1_task/1_iter']
        pkl_demos = pkl_prefix + str(n) + ".pkl"

        demos = { 'demoX' : [], 'demoU' : [] }

        for j in jsons:
            # { 'demoX': [], 'demoU': [] }
            tmp_demos = make_demoX_and_demoU(j)
            demos['demoX'].append(tmp_demos['demoX'])
            demos['demoU'].append(tmp_demos['demoU'])

        demos['demoX'] = np.repeat(np.array(demos['demoX']), 11, axis=0)
        demos['demoU'] = np.repeat(np.array(demos['demoU']), 11, axis=0)

        print(np.array(demos['demoX']).shape)

        with open(join(pkl_dir, pkl_demos), 'wb') as handle:
            pickle.dump(demos, handle, protocol=pickle.HIGHEST_PROTOCOL)



