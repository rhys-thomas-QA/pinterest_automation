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
    'authority': 'www.pinterest.co.uk',
    'accept': 'application/json, text/javascript, */*, q=0.01',
    'x-pinterest-appstate': 'active',
    'x-app-version': 'a2a392a',
    'x-requested-with': 'XMLHttpRequest',
    'x-pinterest-experimenthash': '8ce911ccc491eeaff4cd32514fc52d66c7f980b0d9f5cbff9ec37ab242afc3f527b2c9e0b71af1574b7b6c3ff0710bca87328e0af67802887d9278b546134edc',
    'user-agent': 'Chrome/81.0.4044.138',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.pinterest.co.uk/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': 'csrftoken=34d8c022b199d4258a6f48e00a1a9aa3; bei=false; cm_sub=denied; logged_out=True; fba=True; g_state={"i_p":1588835383497,"i_l":2}; ujr=1; fbm_274266067164=base_domain=.www.pinterest.co.uk; _auth=1; _pinterest_sess=TWc9PSZ1WUxsbE5zaW1qOUltc1ppV2d3UTZ2emdBRGlOdEJ4dlptU2dvMHB2SlIzN01rVDlxcEFna21ocWNoMGZJT2dBZjR4Qk5yTVgwRlVUR2R2enNHRlVWRnBFYWtGYnkwK3VmZTJ3K2JHakZJMXNUeEZHVHFFaFE4ZFpyZy9FRjBGNnB2S0JEZCtsd3ZhL0xyazBWd0I3d3dJRFRORTFUOHJrYUxmTjF2NnMvK1l0UmZlM004NEdaTi9MTDJLalg5RFY4SG5vV05Md2hNdGJJZHFWelVsTTZyUDlRYld1SmUxZkh0eG9RSitoMGh4VGpWcGVkUGprV1pnRVFmL3hlOWQ4L2JueFd4dnZqZzUxd2FxUDVZTVNCd3lDVS9aZ2VkRlRlOU1WSC8zWTIwWkNtNnhGMHk0RUgzV0hIVURWOGNyZ00rcHd3VExtMmZWeFFxNk02bE1WVklJQnZlMVBHZWFkVEhyRHlrU2dXdmtaTzkvQmlGd050RlNZYzFWV1N5bThWdWs1cGNsS0xLQW5CUWoxTHpuQ1VNQWVtaFVtdGROWHEwcHpySmVrb09uTEdKYkFoTnA3cEo0THNMT25nWWYxejliQTY5M2xvbENUNHpVclNLT05rT2gxMlJTYWtjYTRnVGgycTJ6SmdIWWVOV2U1QjZxbEFHUVNrU1FMbk15VlptVHU2VVVFNXZ4ZGdhRXBHcTB6U2pzVU9sV3JYMjJBRnNwWVd2czQ2K1ovOHdtVnBRUThYWkh4WjlzdE5pUjNzUVBKWldNM21SaWp1akJ5YmFkSjFuVnlDV1JtbzRLUzZxVm1pSkNkaVN2RkFDQi9mY3R1bXczRVArZFYxS1JtNHJYaVFqSmZxaHg2TGVkOE9wYjl2SkpYU2JPRnZBYkhteTlFNGptOXBmRjR4dlJTN0VJZWNBUTdhSUV1elowV3ZYU0dDeUVpOWZ0YitoSUdYQWQyWVVvWmNlT3Q1K0pRNnZOcWYwWlJDVm5YSWNtcTQ1a2NjNGRBTG1hdmhSOE40QnZCN1pUR2ZmVVJGcHJLTXN6Y2xKeGN3ZHpwVWlxMkVSY2g4V1Y2cGlYTUMrT1RsNTFSZytOVTVFeE84Q2hVdW9PcUZMM3VpS3JjWGRVeW0yQWhuTklBNDlaTzhPbnF2aDJyOGxBb1FicCtlN1Qvc2l1UHpJWWdHeDhaaXBHNUtIQUpTZ0hsamdKVkpoNkRjb3hOR3Z3a1YrQVFMYzd3SFFmRzZMTTJVdTZBM2IwNUsyRnVzNkJnM3JqNVVvUFhrSnhoQTQ1Wk9sWXJORHcyZ25BMWxyWGFPT2VWUnZsTVJ2S3dOZGE3ZysvbjAyaHdLcHozSUFRbXJrOEl2ODZpNThKdGFRcXB3MUx5VGd2dzBadmsrQ2tQbFE3RytBc2VYd0Z5aTd6RzVnREI3U2NiZVQxTk9jMjh6eXErbHdNZTN4TzdyelVGNCszY3F6TTIrUFRHMUU4aWVTSzZVbStXZ2tLZ21Va0E3VmlTSlFKN0pqRmlURGFnaTlXY3gxaERKSXRYeDA3R25oZDVWUW9OYmhYaFdHZ3dScCtmek1EUzJkcGF3bzIwa29lcHloMGQ2ZW12YjhWZXFlUmdhWTFka0R1WFVOSUdpQlYvYU9jdWdYSDF3elVLd3c2R25UZFMxT3hDSnF3SUFPVzNPc1JaeTJoR1psZlhpdk0yTzNyM0Z6TVpxalE2WUtlcjRjWVdsZ3J0V3JGY1RqN0FtRWF5K0lrTHo0TUk3R3EyUU12eTJFSkVCM1NubDIzQnN6S2VzK0R3OEpOdEwwSXBOTFlwNm1YdS9HYnhhN2ZLMjlUQ0xKTHJRTWx0OWVHaFVEMDhTQmxVQ083WWlpYmYrbVpZJnVhM3BLN0dYL2NYdlFmb1drQXEvM2h2WHNxcz0=; _routing_id="11b53b90-db40-4e10-9b81-b511e4736845"; sessionFunnelEventLogged=1'
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
