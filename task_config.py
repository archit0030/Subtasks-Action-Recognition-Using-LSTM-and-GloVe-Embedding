# 1. Data Preparation
tasks = [
    # Pick and Place actions
    "Pick up the book from the table.",
    "Place the cup on the shelf.",
    "Pick the bottle and place it on the table.",
    "Pick the book and put it on the table.",
    "Pick the book and place it on the table.",
    "Grasp the bottle and place it on the table.",
    "Hey Kinova, can you please pick the bottle and place it on the table?",
    "Perform pick and place task.",
    "Can you pick up the pen and place it on the desk?",
    "Lift the phone and put it on the table.",
    "Please move the book to the shelf.",
    "Pick the remote and place it on the couch.",
    "Get the bottle from the floor and put it on the counter.",
    "Could you grab the magazine and put it on the table?",
    "Take the cup and set it on the desk.",
    "Retrieve the keys and place them on the table.",
    "Hold the notebook and put it on the chair.",
    "Lift the vase and place it on the table.",
    "Pick the water bottle and put it on the table.",
    "Grab the bottle from the shelf and place it on the counter.",
    "Lift the water bottle and set it on the desk.",
    "Pick up the bottle from the floor and put it on the table.",
    "Place the bottle from the chair to the table.",
    "Can you move the bottle from the desk to the shelf?",
    "Take the bottle from the counter and put it on the table.",
    "Could you lift the bottle and place it on the chair?",
    "Move the bottle from the shelf and put it on the table.",
    "Get the bottle from the desk and place it on the counter.",

    # Pick and Pour actions
    "Grab the glass and pour it in the bowl.",
    "Pick the bottle and pour the water in the bowl.",
    "Hey! Please pick the bottle and pour the water in the glass or cup.",
    "Perform pick and pour task.",
    "Pour water from the jug into the glass.",
    "Pick up the bottle and pour juice into the cup.",
    "Fill the bowl with water from the pitcher.",
    "Pour the milk into the cereal bowl.",
    "Can you pour the tea into the cup?",
    "Pick the container and pour the liquid into the bottle.",
    "Could you grab the jug and pour it into the bowl?",
    "Take the glass and pour the water into the pot.",
    "Pick up the cup and pour the coffee into the mug.",
    "Grab the bottle and pour its contents into the glass.",
    "Pick up the bottle and pour it into the bowl.",
    "Take the bottle and pour its contents into the cup.",
    "Pour the water from the bottle into the glass.",
    "Fill the cup with water from the bottle.",
    "Can you pour the bottle's water into the bowl?",
    "Pour the liquid from the bottle into the pot.",
    "Pick the bottle and pour its contents into the pitcher.",
    "Could you take the bottle and pour the water into the cup?",
    "Grab the bottle and pour the liquid into the glass.",
    "Pick up the bottle and pour the water into the bowl.",

    # Other actions
    "Turn the knob clockwise.",
    "Open the door slowly."
]


# Possible sub-actions
sub_actions = [
    "Reach",  # 0
    "Grasp",  # 1
    "Lift",   # 2
    "Move",   # 3
    "Place",  # 4
    "Release",# 5
    "Retract",# 6
    "Rotate", # 7
    "Tilt"    # 8
]

# Map each task to a sequence of sub-action labels
sub_action_sequences = [
    # Pick and Place action sequences
    [0, 1, 2, 3, 4, 5, 6],     # "Pick up the book from the table."
    [0, 1, 2, 3, 4, 5, 6],     # "Place the cup on the shelf."
    [0, 1, 2, 3, 4, 5, 6],     # "Pick the bottle and place it on the table."
    [0, 1, 2, 3, 4, 5, 6],     # "Pick the book and put it on the table."
    [0, 1, 2, 3, 4, 5, 6],     # "Pick the book and place it on the table."
    [0, 1, 2, 3, 4, 5, 6],     # "Grasp the bottle and place it on the table."
    [0, 1, 2, 3, 4, 5, 6],     # "Hey Kinova, can you please pick the bottle and place it on the table?"
    [0, 1, 2, 3, 4, 5, 6],     # "Perform pick and place task."
    [0, 1, 2, 3, 4, 5, 6],     # "Can you pick up the pen and place it on the desk?"
    [0, 1, 2, 3, 4, 5, 6],     # "Lift the phone and put it on the table."
    [0, 1, 2, 3, 4, 5, 6],     # "Please move the book to the shelf."
    [0, 1, 2, 3, 4, 5, 6],     # "Pick the remote and place it on the couch."
    [0, 1, 2, 3, 4, 5, 6],     # "Get the bottle from the floor and put it on the counter."
    [0, 1, 2, 3, 4, 5, 6],     # "Could you grab the magazine and put it on the table?"
    [0, 1, 2, 3, 4, 5, 6],     # "Take the cup and set it on the desk."
    [0, 1, 2, 3, 4, 5, 6],     # "Retrieve the keys and place them on the table."
    [0, 1, 2, 3, 4, 5, 6],     # "Hold the notebook and put it on the chair."
    [0, 1, 2, 3, 4, 5, 6],     # "Lift the vase and place it on the table."
    [0, 1, 2, 3, 4, 5, 6],     # "Pick the water bottle and put it on the table."
    [0, 1, 2, 3, 4, 5, 6],     # "Grab the bottle from the shelf and place it on the counter."
    [0, 1, 2, 3, 4, 5, 6],     # "Lift the water bottle and set it on the desk."
    [0, 1, 2, 3, 4, 5, 6],     # "Pick up the bottle from the floor and put it on the table."
    [0, 1, 2, 3, 4, 5, 6],     # "Place the bottle from the chair to the table."
    [0, 1, 2, 3, 4, 5, 6],     # "Can you move the bottle from the desk to the shelf?"
    [0, 1, 2, 3, 4, 5, 6],     # "Take the bottle from the counter and put it on the table."
    [0, 1, 2, 3, 4, 5, 6],     # "Could you lift the bottle and place it on the chair?"
    [0, 1, 2, 3, 4, 5, 6],     # "Move the bottle from the shelf and put it on the table."
    [0, 1, 2, 3, 4, 5, 6],     # "Get the bottle from the desk and place it on the counter."

    # Pick and Pour action sequences
    [0, 1, 2, 3, 8, 0, 5, 6],  # "Grab the glass and pour it in the bowl."
    [0, 1, 2, 3, 8, 0, 5, 6],  # "Pick the bottle and pour the water in the bowl."
    [0, 1, 2, 3, 8, 0, 5, 6],  # "Hey! Please pick the bottle and pour the water in the glass or cup."
    [0, 1, 2, 3, 8, 0, 5, 6],  # "Perform pick and pour task."
    [0, 1, 2, 3, 8, 0, 5, 6],  # "Pour water from the jug into the glass."
    [0, 1, 2, 3, 8, 0, 5, 6],  # "Pick up the bottle and pour juice into the cup."
    [0, 1, 2, 3, 8, 0, 5, 6],  # "Fill the bowl with water from the pitcher."
    [0, 1, 2, 3, 8, 0, 5, 6],  # "Pour the milk into the cereal bowl."
    [0, 1, 2, 3, 8, 0, 5, 6],  # "Can you pour the tea into the cup?"
    [0, 1, 2, 3, 8, 0, 5, 6],  # "Pick the container and pour the liquid into the bottle."
    [0, 1, 2, 3, 8, 0, 5, 6],  # "Could you grab the jug and pour it into the bowl?"
    [0, 1, 2, 3, 8, 0, 5, 6],  # "Take the glass and pour the water into the pot."
    [0, 1, 2, 3, 8, 0, 5, 6],  # "Pick up the cup and pour the coffee into the mug."
    [0, 1, 2, 3, 8, 0, 5, 6],  # "Grab the bottle and pour its contents into the glass."
    [0, 1, 2, 3, 8, 0, 5, 6],  # "Pick up the bottle and pour it into the bowl."
    [0, 1, 2, 3, 8, 0, 5, 6],  # "Take the bottle and pour its contents into the cup."
    [0, 1, 2, 3, 8, 0, 5, 6],  # "Pour the water from the bottle into the glass."
    [0, 1, 2, 3, 8, 0, 5, 6],  # "Fill the cup with water from the bottle."
    [0, 1, 2, 3, 8, 0, 5, 6],  # "Can you pour the bottle's water into the bowl?"
    [0, 1, 2, 3, 8, 0, 5, 6],  # "Pour the liquid from the bottle into the pot."
    [0, 1, 2, 3, 8, 0, 5, 6],  # "Pick the bottle and pour its contents into the pitcher."
    [0, 1, 2, 3, 8, 0, 5, 6],  # "Could you take the bottle and pour the water into the cup?"
    [0, 1, 2, 3, 8, 0, 5, 6],  # "Grab the bottle and pour the liquid into the glass."
    [0, 1, 2, 3, 8, 0, 5, 6],  # "Pick up the bottle and pour the water into the bowl."

    # Other action sequences
    [0, 1, 8, 7],  # "Turn the knob clockwise."
    [0, 1, 3, 4]   # "Open the door slowly."
]
