import imageio
import glob

for im_path in glob.glob("../../sample_data/01_task_human/01_iter/CameraTOP_img_01_000.png"):
     im = imageio.imread(im_path)
     print(im.shape)
