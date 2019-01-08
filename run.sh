python2 ./mil/main.py --experiment=my_pick_and_place --demo_file=my_pick_and_place --demo_gif_dir=my_pick_and_place/ --gif_prefix=object \
               --T=16 --im_width=100 --im_height=100 --val_set_size=6 --metatrain_iterations=30000 --init=xavier \
               --meta_batch_size=5 --train_update_lr=0.01 --clip=True --clip_min=-10 --clip_max=10 \
               --fp=True --num_filters=16 --filter_size=5 --num_conv_layers=4 --num_strides=4 --all_fc_bt=False --bt_dim=20 \
               --num_fc_layers=3 --layer_size=200 --loss_multiplier=50.0 --two_head=True --log_dir=logs/sim_push
