import tests.add_pins as add_pins
artist_array_1 = [
    # "Queen",
    # "Lynyrd Skynyrd",
    # "Foo Fighters",
    # "Dire Straits",
    # "Red Hot Chilli Peppers",
    # "Zakk Wylde",
    # "Slayer",
    "Taylor Swift"
]


# Monday
def lambda_handler_1(event=None, context=None):
    for n in artist_array_1:
        add_pins.full_process(n)
    print("New pins added for eight boards!")
