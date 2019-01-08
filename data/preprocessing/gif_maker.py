import imageio
import natsort
from os import listdir
from os.path import isfile, join
import shutil
import os

TOTAL_SAMPLE = 220
EACH_NUM_PNG = 21

# list sample paths
dataset_path = "../../sample_data/"
save_path = "../../my_pick_and_place/"
gif_dir_prefix = "object_"

shutil.rmtree(join(save_path, gif_dir_prefix) + "*", ignore_errors=True)


tasks = sorted(listdir(dataset_path), key=(lambda x: x.split("_")[2]))
tasks = sorted(tasks, key=(lambda x: int(x.split("_")[0])))
#tasks = sorted(tasks, key=(lambda x: x.split("_")[2]))

print(tasks)

dir_paths = [join(dataset_path, d) for d in tasks] # [01_task_human, 02_task_human, ...]
iter_paths = [[join(d, i) for i in listdir(d)] for d in dir_paths] # [[01_iter, 02_iter, ...], [01_iter, ...]]

final_paths = []
tmp = []
print("iter paths", len(iter_paths))
for i in range(len(iter_paths)):
    tmp += iter_paths[i]
    if i % 2 == 1:
        final_paths.append(tmp)
        tmp = []


print(final_paths)

# assert the number of data
len_samples = 0
for i in iter_paths:
    len_samples += len(i)
assert len_samples == TOTAL_SAMPLE
print(len_samples)

print("length",len(final_paths))
# making 'png's to gif
for n, task in enumerate(final_paths): # iter_paths
    #robot_human = n % 2
    save_num = n# / 2
    save_file_name = save_path + gif_dir_prefix + str(save_num)
    if not os.path.exists(save_file_name):
        os.mkdir(save_file_name)

    for p, iters in enumerate(task):
        save_name = "cond%d.samp0.gif" % p

        image_data = [join(iters, f) for f in listdir(iters) if f.endswith("png")]
        image_data = natsort.natsorted(image_data)
        assert len(image_data) == EACH_NUM_PNG or len(image_data) == 16
        with imageio.get_writer(join(save_file_name, save_name), mode="I") as writer:
            for f in image_data:
                image = imageio.imread(f)
                writer.append_data(image)
