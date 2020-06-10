import tests.add_pins as add_pins

artist_array_5 = [
    "The White Stripes",
    "Ed Sheeran",
    "Johnny Cash",
    "The Eagles",
    "The Beatles",
    "Chet Atkins",
    "The Lumineers"
]


# Friday
def lambda_handler_5(event=None, context=None):
    for n in artist_array_5:
        add_pins.full_process(n)
    print("New pins added for eight boards!")
