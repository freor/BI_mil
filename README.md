# existing data

demoX, demoU: (the number of demos in a task, time horizon, state/action)

- demoX: (24, 100, 20)
- demoU: (24, 100, 7)
- xml: string

## specification

- demoX: state
- demoU: action


# our data

- We have 10 demos in each task and the time horizon is 16

## state data
- joint_angles: (16, 6)
- end_position: (16, 3)
- end_orientation: (16, 4)

## action data
- end_angluar_velocity: (16, 3)
- joint_velocities: (16, 6)
- end_linear_velocity: (16, 3)

## data shape

- human_gif: (10, 16, )
- robot_gif: (1, 16, )
- demoX: (1, 16, 13)
- demoU: (1, 16, 12)

# about DATA

- my_pick_and_place (DIR) (#: 1~24)

  - object_{#} (DIR): GIFs

  - demos_{#} (PKL): { 'demoX': np.array, 'demoU': np.array }



