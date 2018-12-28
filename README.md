# existing data

demoX, demoU: (the number of demos in a task, time horizon, state/action)

- demoX: (24, 100, 20)
- demoU: (24, 100, 7)
- xml: string

## specification

- demoX: state
- demoU: action


# our data

## state data
- joint_angles: (16, 6)
- end_position: (16, 3)
- end_orientation: (16, 4)

## action data
- end_angluar_velocity: (16, 3)
- joint_velocities: (16, 6)
- end_linear_velocity: (16, 3)

## data shape

- gif: (24, )
- demoX: (16, 13)
- demoU: (16, 12)
