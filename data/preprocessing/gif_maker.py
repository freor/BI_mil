import imageio
import natsort
from os import listdir
from os.path import isfile, join

TOTAL_SAMPLE = 220
EACH_NUM_PNG = 21

# list sample paths
dataset_path = "../../sample_data/"
dir_paths = [join(dataset_path, d) for d in listdir(dataset_path)] # [01_task_human, 02_task_human, ...]
iter_paths = [[join(d, i) for i in listdir(d)] for d in dir_paths] # [[01_iter, 02_iter, ...], [01_iter, ...]]

# assert the number of data
len_samples = 0
for i in iter_paths:
    len_samples += len(i)
assert len_samples == TOTAL_SAMPLE
print(len_samples)

# making 'png's to gif
for task in iter_paths:
    for iters in task:
        image_data = [join(iters, f) for f in listdir(iters) if f.endswith("png")]
        image_data = natsort.natsorted(image_data)
        assert len(image_data) == EACH_NUM_PNG or len(image_data) == 16
        with imageio.get_writer(join(iters, "task.gif"), mode="I") as writer:
            for f in image_data:
                image = imageio.imread(f)
                writer.append_data(image)

