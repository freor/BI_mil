import imageio

images = []
for f in filenames:
    images.append(imageio.imread(f))
imageio.mimsave('.gif',images)
