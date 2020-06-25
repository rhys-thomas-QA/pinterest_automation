import requests
import json
import urllib.parse
import time

board_id = 0
pin_id_array = []
description_array = []
link_array = []
title_array = []
results_array = []
dashed_lowercase_artist = ""
headers = {
#removed for security purposes
}
payload = {}
base_url = "https://www.pinterest.co.uk/resource/"


def get_board_ids(artist):
    global dashed_lowercase_artist
    lowercase_artist = artist.lower()
    remove_dot = lowercase_artist.replace(".", "")
    dashed_lowercase_artist = remove_dot.replace(" ", "-")
    board_url = base_url + "BoardResource/get/?source_url=%2Fwhatguitarshouldibuy%2F" + dashed_lowercase_artist + "%2F&data=%7B%22options%22%3A%7B%22isPrefetch%22%3Afalse%2C%22username%22%3A%22whatguitarshouldibuy%22%2C%22slug%22%3A%22" + dashed_lowercase_artist + "%22%2C%22field_set_key%22%3A%22detailed%22%7D%2C%22context%22%3A%7B%7D%7D&_=1589761481969"
    response = requests.request("GET", board_url, headers=headers, data=payload)
    parsed = json.loads(response.content)
    global board_id
    board_id = parsed["resource_response"]["data"]["id"]


def more_ideas():
    epoch_time = str(int(time.time()))
    url = base_url + "BoardContentRecommendationResource/get/?source_url=%2Fwhatguitarshouldibuy%2F" + dashed_lowercase_artist + "%2Fmore_ideas%2F%3Fideas_referrer%3D1&data=%7B%22options%22%3A%7B%22isPrefetch%22%3Afalse%2C%22type%22%3A%22board%22%2C%22id%22%3A%22" + str(
        board_id) + "%22%2C%22__track__referrer%22%3A%221%22%7D%2C%22context%22%3A%7B%7D%7D&_=" + epoch_time
    response = requests.request("GET", url, headers=headers, data=payload)
    parsed = json.loads(response.text)
    results = parsed["resource_response"]["data"]
    for n in results:
        is_promoted = n["is_promoted"]
        if is_promoted is False:
            pin_id = n["id"]
            pin_id_array.append(pin_id)
            description = n["description"]
            description_array.append(description)
            link = n["link"]
            if link is not None:
                link_array.append(link)
            elif link is None:
                link_array.append("None")
            title = n["title"]
            title_array.append(title)


def save_pins(artist):
    url = base_url + "/create/"
    number_of_successes = []
    i = 0
    while i <= 4:
        link_payload = link_array[i]
        split_link_payload = link_payload.replace(":", "%3A")
        encoded_title = urllib.parse.quote(title_array[i], safe="")
        quotes = description_array[i].replace('"', '\"')
        encoded_description = urllib.parse.quote(quotes, safe="")
        full_payload = "source_url=/whatguitarshouldibuy/" + dashed_lowercase_artist + "/more_ideas/%3Fideas_referrer%3D1&data=%7B%22options%22%3A%7B%22board_id%22%3A%22" + str(
            board_id) + "%22%2C%22clientTrackingParams%22%3A%22CwABAAAAEDgyODIwNDg2NjI4NTU3MjYGAAMAGwA%22%2C%22description%22%3A%22" + \
                       encoded_description + "%22%2C%22link%22%3A%22" + split_link_payload + "%22%2C%22image_url%22%3A%22%22%2C%22is_buyable_pin%22%3Afalse%2C%22is_removable%22%3Afalse%2C%22pin_id%22%3A%22" + \
                       pin_id_array[
                           i] + "%22%2C%22title%22%3A%22" + encoded_title + "%22%2C%22eventContext%22%3A%7B%22viewType%22%3A5%2C%22viewParameter%22%3A3173%2C%22element%22%3A10599%7D%7D%2C%22context%22%3A%7B%7D%7D"
        body = full_payload.encode("utf-8")
        pin_response = requests.request("POST", url, headers=headers, data=body)
        status_code = pin_response.status_code
        if status_code == 200:
            number_of_successes.append(i)
            print(artist + " pin has been added successfully")
        elif status_code == 400:
            print(artist + " pin failed to save")
        elif status_code == 429:
            print("Too many requests")
        i += 1
    print(str(len(number_of_successes)) + " pins saved for " + artist)
    assert len(number_of_successes) != 0


def cleanup():
    del pin_id_array[:]
    del description_array[:]
    del link_array[:]
    del title_array[:]
    del results_array[:]


def full_process(artist):
    get_board_ids(artist)
    more_ideas()
    save_pins(artist)
    cleanup()
