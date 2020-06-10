import tests.add_pins as add_pins

artist_array_3 = [
    "Radiohead",
    "Oasis",
    "Blur",
    "ACDC",
    "Led Zeppelin",
    "Jimi Hendrix",
    "The Doors"
]


# Wednesday
def lambda_handler_3(event=None, context=None):
    for n in artist_array_3:
        add_pins.full_process(n)
    print("New pins added for eight boards!")
