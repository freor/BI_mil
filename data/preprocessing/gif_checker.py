from PIL import Image
#im = Image.open("../sim_push/object_0/cond0.samp0.gif")
im = Image.open("../../my_pick_and_place/object_0/cond0.samp0.gif")

# To iterate through the entire gif
try:
    n = 0
    while 1:
        im.seek(im.tell()+1)
        n = n+ 1
        print(im.height)
        print(im.width)
        print(n)
        # do something to im
except EOFError:
    pass # end of sequence
