import requests
import json
import urllib.parse
import cloudinary.uploader
import cloudinary.api

board_id = 0
bookmark = 0
lowercase_artist = ""
description = ""
image_url = ""
replaced_slash_image_url = ""
dashed_lowercase_artist = ""
pinimg_image_url = ""
pin_id = ""

cloudinary.config(
    cloud_name='dohldvzge',
    api_key='583672847454456',
    api_secret='m9TxiFjyUrnbH6fN_xMGfBs2unM'
)

cloudinary_upload_preset = 'kk4tiben'


def get_board_ids(artist):
    global lowercase_artist
    global dashed_lowercase_artist
    lowercase_artist = artist.lower()
    remove_dot = lowercase_artist.replace(".", "")
    dashed_lowercase_artist = remove_dot.replace(" ", "-")
    payload = {}
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
    board_url = "https://www.pinterest.co.uk/resource/BoardResource/get/?source_url=%2Fwhatguitarshouldibuy%2F" + dashed_lowercase_artist + "%2F&data=%7B%22options%22%3A%7B%22isPrefetch%22%3Afalse%2C%22username%22%3A%22whatguitarshouldibuy%22%2C%22slug%22%3A%22" + dashed_lowercase_artist + "%22%2C%22field_set_key%22%3A%22detailed%22%7D%2C%22context%22%3A%7B%7D%7D&_=1589761481969"
    response = requests.request("GET", board_url, headers=headers, data=payload)
    content = response.content
    parsed = json.loads(content)
    global description
    global board_id
    description = parsed["resource_response"]["data"]["description"]
    board_id = parsed["resource_response"]["data"]["id"]


def post_image_to_cloudinary():
    base_path = "/Users/rhysthomas/Documents/WhatGuitarShouldIBuy/Pinterest/"
    file_name = base_path + dashed_lowercase_artist + "/" + dashed_lowercase_artist + "-3.png"
    response = cloudinary.uploader.upload(file_name)
    global image_url
    image_url = str(response["url"])


def create_new_pin(artist):
    headers = {
        'authority': 'www.pinterest.co.uk',
        'accept': 'application/json, text/javascript, */*, q=0.01',
        'x-pinterest-appstate': 'active',
        'x-app-version': 'fd3c85b',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'x-csrftoken': '34d8c022b199d4258a6f48e00a1a9aa3',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.pinterest.co.uk',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.pinterest.co.uk/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'csrftoken=34d8c022b199d4258a6f48e00a1a9aa3; cm_sub=denied; fba=True; fbm_274266067164=base_domain=.www.pinterest.co.uk; bei=false; logged_out=True; g_state={"i_p":1593165670442,"i_l":4}; _auth=1; _pinterest_sess=TWc9PSZCWEN6N2hyZFczekpKY0xFeHZ5RXJwNWJvaGxCeVhMYWNmU2Z0R1AxbHJTUVMyd1FQQjlkKzZROC9ITW4xNzZFUEEwSDlEWnYxQU1nS1k5b0VhWkxVZStqM3lZZXo4Ym5XZTRpcThaSXhGcGVvSko0YlFROEdQVlF6SFJxaUM1TVo2MXVVTFhMQkVTanJyWHlCK1AzU3N0VFJsMllmOTBvMGN5NzdKSjBLbWZMNUxPbHZqalVHOFJCclJVR1dSM3ZFQk9xMU1ORXl6czMvZG5GeDhDYTJIbEJhT21rdjN1VXpSSTN4K0FvaFJFR0JmUDVWTnowQjUzeVZsZUFEZElQQXRPRmFsUDBRNnhNR2VjNXBuSHFyQ3JuRnVYdVZHNGhwYkQxb0VJTU5GSzYyRXhKcUx2VTNQU3puQmlDeWR5R2oyTURQUWdFanY0UVpOVlFZRThJZm9UT0xDb1JOTi96VEpjRWc4Y1NuR010MzRsczgyU3FNQlBUUjlzdnNzK0lidGNMamZraFVSeUl2bzB4T0FFcW4zdktSVTRoR3R4L3NmQzhSbm9iZEIzdkVJRTFRQTgweDZQL3oyOGZVWnZPZnZ2cDN5TnA0a04wQ3d0MVZ3VmpRYnpFTVZHUTZZSThDSjREeFJ2OGxsYlJJNmUwTkVOYjNQd1M2emVOQ2lsTS9RNXord2hHOEVEUVp5NktlT0d1d1VzSDJaVll6QVZOQ0NKM1hERHJ1MXYyNWRkczAyRkNYSUcvNFdLdDNoeWRKYTI3dWN5cmM4UWlmcFpuRzRZRndWak02M2N2SFFWMXpjazZkZStKY1NlM2dINXpGMzExTjQ2c0J2bk0zVGtUL1RjRWJ2Um9mdHNkZGw4VzBxTFdjY1FsazRWZERCMW1NYUN6MUZ3WW5mSUYrNVFPLzAwQnRndXU5NHZKMU1xK3Y1djlBOG10bFMwcUlKcG9nbVRBVHd5WDErTEF2UU9sTktwTzE1VzlhWTNBOXlPMU1MTWprb2hKVEt0N20yOEtjdHNIa0V6QjcwMHU5Q3Rkbkx5SHFJcmRxbDdTYW0xcHI3dHhGZDV4ZVp2ek85R05YbTBSR0R6R3pDN3lwM0NQbDdUbUFSMXRwOGNHeTFQRFZsbUpLOUtEWEluWENxWThrOHFMV2VLQ2ZUMWlVQVFIUWswR1VnUTBsbTVER1NDYmVHM3hvZTF4eExianJQQS9ocXVpa3hBcXNqeUFOUVZoODFMVFRpRXhSZm1GTENpTGZSYzM0eEI3S2FRZjdwNXJqQURGbmFsZ0VYUU9Rak84ZlA0clhqLzlkcWU1VzFyQzl3UlFsb2dzZHlORGZsMkF3YUY4SkN3OVNhakhqMENGVjVZdFNaZzl5cXpDNERTZXBxTHFjNnJqS04wUGF2enVKeDdsclphalNjQ0dmMkxZQ0hPRmxkaUdRaVhHK2FITnl6dVU5YWJmVkZFd0thN3JDZk5tbGYvQkJzMUZRdjhIVXlGTVBQY2NLdGE2TFpWdkxOSk9NalVOTWM0NUI2T2Ivc3BnS3hDdGc2RVI3NVFaUzB1cm03azZXei9UOWt5L0Y1anB2S3Y0a25MWW9nMGlLb3dMaHZDTTFoY2JBVlFYRXJOL0hacE5udVJsOXhEbDNhS3Y1N0Rib1FIMU94RmtTcFhZQmZxS0ltbm1FNU9UdkdxdlpIdVpud0prU0tZUGZEZUZYYS9UY3g2VjV5RVRQcytxd2JRWEhhVGphZmJqY2NsL0wwMGtLOFExL0Qwd1lXaXBjUmxoOEEza2lvTlorSldIUTloN1VYa2VyUW1uY0lZS0VnSDlZazYzQzQ4dy9CL1JldHhwYzBTQzY2cUJ6YStlYitvL0FiTTNvTkNMRFlycENmVm5UZ3VZWHBLQ2xwRGFHa2R1eHM2UmZDM0MrTEZBS25weFJEZE0zSUhMZE5WSFpHWUtVK3l4anFobi9Rc3hJWVFVWFZDeTJtNjVUd05RZ0E9PSZTd3dsUTduYWQ5UlpKVithQjMyWFBGTXdwRlU9; sessionFunnelEventLogged=1; _routing_id="242e3ec6-83f5-4037-a037-aca6c71f944a"'
    }
    base_url = "https://www.pinterest.co.uk/resource/PinResource/create/"
    source_url = 'source_url=/pin-builder/&data='
    encode_image_url = image_url.replace("https://", "https%3A%//")
    global replaced_slash_image_url
    first_half = '{"options":{"board_id":"' + str(
        board_id) + '","field_set_key":"create_success","skip_pin_create_log":true,"description":"' + description + '","link":"whatguitarshouldibuy.com/' + dashed_lowercase_artist + '","title":"How to sound like ' + artist + '","image_url":"'
    second_half = '","method":"uploaded","upload_metric":{"source":"partner_upload_standalone"}},"context":{}}'
    encoded_first_half = urllib.parse.quote(first_half, safe="")
    encoded_second_half = urllib.parse.quote(second_half, safe="")
    payload = source_url + encoded_first_half + encode_image_url + encoded_second_half
    url = base_url
    response = requests.request("POST", url, headers=headers, data=payload)
    status_code = response.status_code
    if status_code == 200:
        print(artist + " pin creation successful")
    elif status_code == 400:
        print(artist + " pin failed to create")
    elif status_code == 429:
        print("Too many requests")
    content = response.content
    parsed_response = json.loads(content)
    global pin_id
    pin_id = parsed_response["resource_response"]["data"]["id"]
    global pinimg_image_url
    pinimg_image_url = parsed_response["resource_response"]["data"]["images"]["474x"]["url"]


def update_board_cover(artist):
    url = "https://www.pinterest.co.uk/resource/BoardResource/update/"
    headers = {
        'authority': 'www.pinterest.co.uk',
        'accept': 'application/json, text/javascript, */*, q=0.01',
        'x-pinterest-appstate': 'active',
        'x-app-version': 'fd3c85b',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'x-csrftoken': '34d8c022b199d4258a6f48e00a1a9aa3',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.pinterest.co.uk',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.pinterest.co.uk/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'csrftoken=34d8c022b199d4258a6f48e00a1a9aa3; cm_sub=denied; fba=True; fbm_274266067164=base_domain=.www.pinterest.co.uk; bei=false; logged_out=True; g_state={"i_p":1593165670442,"i_l":4}; _auth=1; _pinterest_sess=TWc9PSZCWEN6N2hyZFczekpKY0xFeHZ5RXJwNWJvaGxCeVhMYWNmU2Z0R1AxbHJTUVMyd1FQQjlkKzZROC9ITW4xNzZFUEEwSDlEWnYxQU1nS1k5b0VhWkxVZStqM3lZZXo4Ym5XZTRpcThaSXhGcGVvSko0YlFROEdQVlF6SFJxaUM1TVo2MXVVTFhMQkVTanJyWHlCK1AzU3N0VFJsMllmOTBvMGN5NzdKSjBLbWZMNUxPbHZqalVHOFJCclJVR1dSM3ZFQk9xMU1ORXl6czMvZG5GeDhDYTJIbEJhT21rdjN1VXpSSTN4K0FvaFJFR0JmUDVWTnowQjUzeVZsZUFEZElQQXRPRmFsUDBRNnhNR2VjNXBuSHFyQ3JuRnVYdVZHNGhwYkQxb0VJTU5GSzYyRXhKcUx2VTNQU3puQmlDeWR5R2oyTURQUWdFanY0UVpOVlFZRThJZm9UT0xDb1JOTi96VEpjRWc4Y1NuR010MzRsczgyU3FNQlBUUjlzdnNzK0lidGNMamZraFVSeUl2bzB4T0FFcW4zdktSVTRoR3R4L3NmQzhSbm9iZEIzdkVJRTFRQTgweDZQL3oyOGZVWnZPZnZ2cDN5TnA0a04wQ3d0MVZ3VmpRYnpFTVZHUTZZSThDSjREeFJ2OGxsYlJJNmUwTkVOYjNQd1M2emVOQ2lsTS9RNXord2hHOEVEUVp5NktlT0d1d1VzSDJaVll6QVZOQ0NKM1hERHJ1MXYyNWRkczAyRkNYSUcvNFdLdDNoeWRKYTI3dWN5cmM4UWlmcFpuRzRZRndWak02M2N2SFFWMXpjazZkZStKY1NlM2dINXpGMzExTjQ2c0J2bk0zVGtUL1RjRWJ2Um9mdHNkZGw4VzBxTFdjY1FsazRWZERCMW1NYUN6MUZ3WW5mSUYrNVFPLzAwQnRndXU5NHZKMU1xK3Y1djlBOG10bFMwcUlKcG9nbVRBVHd5WDErTEF2UU9sTktwTzE1VzlhWTNBOXlPMU1MTWprb2hKVEt0N20yOEtjdHNIa0V6QjcwMHU5Q3Rkbkx5SHFJcmRxbDdTYW0xcHI3dHhGZDV4ZVp2ek85R05YbTBSR0R6R3pDN3lwM0NQbDdUbUFSMXRwOGNHeTFQRFZsbUpLOUtEWEluWENxWThrOHFMV2VLQ2ZUMWlVQVFIUWswR1VnUTBsbTVER1NDYmVHM3hvZTF4eExianJQQS9ocXVpa3hBcXNqeUFOUVZoODFMVFRpRXhSZm1GTENpTGZSYzM0eEI3S2FRZjdwNXJqQURGbmFsZ0VYUU9Rak84ZlA0clhqLzlkcWU1VzFyQzl3UlFsb2dzZHlORGZsMkF3YUY4SkN3OVNhakhqMENGVjVZdFNaZzl5cXpDNERTZXBxTHFjNnJqS04wUGF2enVKeDdsclphalNjQ0dmMkxZQ0hPRmxkaUdRaVhHK2FITnl6dVU5YWJmVkZFd0thN3JDZk5tbGYvQkJzMUZRdjhIVXlGTVBQY2NLdGE2TFpWdkxOSk9NalVOTWM0NUI2T2Ivc3BnS3hDdGc2RVI3NVFaUzB1cm03azZXei9UOWt5L0Y1anB2S3Y0a25MWW9nMGlLb3dMaHZDTTFoY2JBVlFYRXJOL0hacE5udVJsOXhEbDNhS3Y1N0Rib1FIMU94RmtTcFhZQmZxS0ltbm1FNU9UdkdxdlpIdVpud0prU0tZUGZEZUZYYS9UY3g2VjV5RVRQcytxd2JRWEhhVGphZmJqY2NsL0wwMGtLOFExL0Qwd1lXaXBjUmxoOEEza2lvTlorSldIUTloN1VYa2VyUW1uY0lZS0VnSDlZazYzQzQ4dy9CL1JldHhwYzBTQzY2cUJ6YStlYitvL0FiTTNvTkNMRFlycENmVm5UZ3VZWHBLQ2xwRGFHa2R1eHM2UmZDM0MrTEZBS25weFJEZE0zSUhMZE5WSFpHWUtVK3l4anFobi9Rc3hJWVFVWFZDeTJtNjVUd05RZ0E9PSZTd3dsUTduYWQ5UlpKVithQjMyWFBGTXdwRlU9; sessionFunnelEventLogged=1; _routing_id="242e3ec6-83f5-4037-a037-aca6c71f944a"'
    }
    source_url = "source_url=/whatguitarshouldibuy/boards/&data="
    first_half = '{"options":{"board_id":"' + str(board_id) + '","url":"'
    encoded_first_half = urllib.parse.quote(first_half, safe="")
    image_link = pinimg_image_url.replace("https://", "https%3A//")
    second_half = '","pin_id":"' + str(pin_id) + '","pin_image_url":"'
    encoded_second_half = urllib.parse.quote(second_half, safe="")
    third_half = '","crop_x":0,"crop_y":52,"height":236,"width":236,"scale":1},"context":{}}'
    encoded_third_half = urllib.parse.quote(third_half, safe="")
    full_payload = source_url + encoded_first_half + image_link + encoded_second_half + image_link + encoded_third_half
    response = requests.request("POST", url, headers=headers, data=full_payload)
    status_code = response.status_code
    if status_code == 200:
        print(artist + " board cover updated")
    elif status_code == 400:
        print(artist + " board cover failed to update")
    elif status_code == 429:
        print("Too many requests")
    cloudinary.api.delete_all_resources()


def full_process(artist):
    get_board_ids(artist)
    post_image_to_cloudinary()
    create_new_pin(artist)
    update_board_cover(artist)


artist_array_1 = [
    "Queen",
    # "Lynyrd Skynyrd",
    # "Foo Fighters",
    # "Dire Straits",
    # "Red Hot Chilli Peppers",
    # "Zakk Wylde",
    # "Slayer",
    # "Taylor Swift"
]
artist_array_2 = [
    "The Rolling Stones",
    "Creedence Clearwater Revival",
    "John Mayer",
    "Guns N Roses",
    "Metallica",
    "Eric Clapton",
    "Greenday"
]
artist_array_3 = [
    "Radiohead",
    "Oasis",
    "Blur",
    "ACDC",
    "Led Zeppelin",
    "Jimi Hendrix",
    "The Doors"
]
artist_array_4 = [
    "Rage Against the Machine",
    "Pink Floyd",
    "Aerosmith",
    "Black Sabbath",
    "ZZ Top",
    "Bob Dylan",
    "Elvis Presley"
]
artist_array_5 = [
    "The White Stripes",
    "Ed Sheeran",
    "Johnny Cash",
    "The Eagles"
    "The Beatles",
    "Chet Atkins",
    "The Lumineers"
]
artist_array_6 = [
    # "Megadeth",
    # "Chuck Berry",
    # "John Lennon",
    "B.B. King",
    # "The Clash",
    # "Fleetwood Mac",
    # "Santana"
]
artist_array_7 = [
    "Iron Maiden",
    "Buddy Holly",
    "Jeff Buckley",
    "Snow Patrol",
    "King Crimson",
    "Bob Marley",
    "Joan Jett"
]


# Monday
def lambda_handler_1(event=None, context=None):
    for n in artist_array_1:
        full_process(n)
    print("New pins added for seven boards!")


# Friday
def lambda_handler_2(event=None, context=None):
    for n in artist_array_2:
        full_process(n)
    print("New pins added for seven boards!")


# Friday
def lambda_handler_3(event=None, context=None):
    for n in artist_array_3:
        full_process(n)
    print("New pins added for seven boards!")


# Friday
def lambda_handler_4(event=None, context=None):
    for n in artist_array_4:
        full_process(n)
    print("New pins added for seven boards!")


# Friday
def lambda_handler_5(event=None, context=None):
    for n in artist_array_5:
        full_process(n)
    print("New pins added for seven boards!")


# Friday
def lambda_handler_6(event=None, context=None):
    for n in artist_array_6:
        full_process(n)
    print("New pins added for seven boards!")


# Friday
def lambda_handler_7(event=None, context=None):
    for n in artist_array_7:
        full_process(n)
    print("New pins added for seven boards!")


# full_process("The White Stripes")
lambda_handler_1()
