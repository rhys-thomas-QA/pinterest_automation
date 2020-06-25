import requests
import json
import urllib.parse
import time
import re
import cloudinary
import cloudinary.uploader
import cloudinary.api
from artist_array import artist_array
import PySimpleGUI as sg


artistSearchUrl = 0
urlencodedartist = 0
guides = 0
guides_array = 0
artistBoardUrl = 0
boardId = 0
description = 0
image_url = 0
replaced_slash_image_url = 0
pin_id = 0
pinimg_image_url = 0

emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
cloudinary.config(
    cloud_name='dohldvzge',
    api_key='583672847454456',
    api_secret='m9TxiFjyUrnbH6fN_xMGfBs2unM'
)

cloudinary_upload_preset = 'kk4tiben'


def search_url(artist):
    global urlencodedartist
    urlencodedartist = urllib.parse.quote(artist, safe="")
    decodedUrl = "/search/pins/?q=" + urlencodedartist + "&rs=typed"
    encodedUrl = urllib.parse.quote(decodedUrl, safe="")
    splitArtist = artist.split(" ")

    # splitArtist is an array of the names of the artist
    array = []
    for n in splitArtist:
        output = ("&term_meta[]=" + n + "%7Ctyped")
        array.append(output)

    artistString = ''.join(array)
    encodedArtistString = urllib.parse.quote(artistString, safe="")

    json_data = '{"options":{"isPrefetch":false,"article":null,"auto_correction_disabled":false,"corpus":null,"customized_rerank_type":null,"filters":null,"page_size":null,"query":' + "\"" + artist + "\"" + ',"query_pin_sigs":null,"redux_normalize_feed":true,"rs":"typed","scope":"pins","source_id":null},"context":{}}'
    encodedJson = urllib.parse.quote(json_data, safe="")
    # print(encodedJson)
    epoch_time = int(time.time())
    stringTime = str(epoch_time)
    fullUrl = encodedUrl + encodedArtistString + "&data=" + encodedJson + "&_=" + stringTime
    global artistSearchUrl
    artistSearchUrl = "https://www.pinterest.co.uk/resource/BaseSearchResource/get/?source_url=" + fullUrl


def get_search_results(artist):
    search_url(artist)
    headers = {
    #removed for security purposes
    }
    payload = {}
    response = requests.request("GET", artistSearchUrl, headers=headers, data=payload)
    response_body = response.content
    parsed = json.loads(response_body)
    # print(parsed)
    global guides
    guides = parsed["resource_response"]["data"]["guides"]


def saving_guides():
    global guides_array
    guides_array = []
    trimmed_guides = guides[:15]
    for n in trimmed_guides:
        guide = n["display"]
        guides_array.append(guide)


def create_board(artist):
    urlencodedartist = urllib.parse.quote(artist, safe="")
    payload = 'source_url=/whatguitarshouldibuy/boards/&data=%7B%22options%22%3A%7B%22name%22%3A%22' + urlencodedartist + '%22%2C%22description%22%3A%22%22%2C%22category%22%3A%22other%22%2C%22privacy%22%3A%22public%22%2C%22collab_board_email%22%3Atrue%2C%22collaborator_invites_enabled%22%3Afalse%7D%2C%22context%22%3A%7B%7D%7D'
    headers = {
        'authority': 'www.pinterest.co.uk',
        'x-pinterest-appstate': 'active',
        'x-app-version': 'fd3c85b',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': 'application/json, text/javascript, */*, q=0.01',
        'x-pinterest-experimenthash': '34879610e323f52518c71f6af2b94994d1a5ff53db42df4021881df51763093129a043acc2fa9cdc15bccb886e022a7b52145c13f6ca18d95296717a802d2e28',
        'x-csrftoken': '34d8c022b199d4258a6f48e00a1a9aa3',
        'origin': 'https://www.pinterest.co.uk',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.pinterest.co.uk/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'csrftoken=34d8c022b199d4258a6f48e00a1a9aa3; cm_sub=denied; fba=True; fbm_274266067164=base_domain=.www.pinterest.co.uk; bei=false; logged_out=True; g_state={"i_p":1593165670442,"i_l":4}; _auth=1; _pinterest_sess=TWc9PSZOcHg4SndXZGtnbzV0ZWNFcGhEcW0raEpFR3BFdGlsQ29PYU1OdFZlN29WUDVhZ1I0WFk1anhNS0gyeWlKZWdpeXIzdjd3aDZnc1NReExTZDVCdHNUWjU5SVJ3MkVCYmcwQ0poSFVlNzQwb0pyOGN5cTFwQ1RIcHp5L0czYVlUazBWZ01CWGkxditveGRlL0oxK2cwWVQxZkNwc09KMkpIRjlueFdwTXk2UU1lOGR3eUc0MEdRVFNSZy94bFU3UHhxOGRhQmRkNVZLQzAxZkN3RmtEZ2t0S1U5Vm81Mytzc21QVTlqTGJpSVArZTNSa2tRRlVpNUlQRDJUK0E5Vm9tY20wYU51ek1XdFp0eXRNQkxqRTN3RXFZUFludjVaaDhkZlJCdDYvckNzR1dIZ3drSzBmSUgvb2ZvT1BoTVlGQWpuZnNUVHBpajFkc2RTandqS3lGanNFUEVSakFwdUIzN2Y1SWUyYjJ5TzZTd2dsWlBvS2VkQVlaSUg3T2JWc3o0WUh0NEgzL3hmRlRRb0pQaHllc1ZDUDR3ZUdxaGxFY2lMY0cwdnAzVS9jQ0tacElBVit2MldDNGs1RzNtaGttMnpEK3JNb0xJdVd6R29zdlV3bncxT2hFMnJRZGxGZnhWbjN4dGdwQ3Q1RG5SZUhhUWRMcmkvY3N1d1hZdERuMHYvdDdrbFJYRjIvbVpRdDgxK2lVME8rdmdmS3g4dDhqNUVaWGU5RkdDRk5vZ205Ty9Lb3FGTWlXVm9UYTlBdWFUZHl4RUtZa01FM0NXSkVCSnZQTEVzdlgxcFpzQmxqV2l3TDFENHA3VloxM2I0cld2L3FpL20zbmUxVVZxemkvM1ZZanNkMW1hQW1yMk9xZTVhVjdsZVdyYTVEZ0YyTWRYS09lOU50T2FiV0tNRUFQQVdtWURocXAyanMwQ2NXUjdzMUcvOTI2QmFpREJsMUYrWG9ySzVxell6WXk0bzF1MHJrNnJHalNkb2lxTWFGbnh5bFh0WmtZQlNFbWJRVW1ta2dXdlovZlhmaThjakJmcnhHU25CZGNmUlZGTkFTblhSRTA4bkVldWh1ZFdJeXo3RkZkUW5mV00zZHNyV3Q5VFMraHpGbndvckJtVlh0RW1qTEpMbThVQS9QZmo5eHFRU2tURE5RQjZVejd2QnpBby9DTzI0UjFZdDdUUlo4dVhDd1JRQ3J6OUJQU2lPZ09VcW9ocnB2S0sxV3JlR1FnVDREWHFLdVF5UWRsV3N4RytPZmgwcWg5cFpOUG9pc3FIc0U1VWRlZkI4VWtLdDBlVDYvWThVeGNzd1pJSXRaU1hab2ExaU5QQisyZVh2OHVDVnJRMmNpdkVNZzVBUFAxWVllV0FVamJxdFEvZGVMbHpNbnF5NEptZXNMRXI5MUVkUjZDU3pjSWdJd1VqMHMwbCt3MWNEVjVKcWZyemcwcjJBR2NpQ0JzTk1qSHYzYkhPVmJCVGVaQXpHUFJlQmdYalhCWTJKQWRCVWU5VjVySFowVjhqV2QvWE8vRGN5VSsvWTljejJaK1BUOTNKeGE1SGlGSE9zVGtuU3krZjVrbm45SFgxMnF2MjVkcXVlWGNFK3ppTjJKWTJ5d1Uyb1RzYW16RUZKN0F4NVhDODhPS2pDYTc3czRHRm1aSjhOSEdnRmJrNUdFazJlQnNzanVMVHNyTnFkeXk4ZVZXTDk5RkxFd2F3R3pMN2N2YUFCaUh1enpyWDNNdXc1YjNoYVk4NDRyNkxmeHJxRTNJdEpiR29YSXh5RURLU1hFSmlPS1VPMWpIR2lPMjUxMzVxaUFqRGIyRzdPSEM4VEovenhoQ3BLSkNGcmttSWZ5RmpUUElmRlY1WXU1Y3dRTEJhTlRlZWZRRTk1WFcrUW9wZ2lyVTVMeDUybFUzK2dkK05qQVd1NWdVY253RmtLbjFlUStPUU5rMVB3YW5Wd1ZxZmFTaFVHaUpsTmRHYXdXa1NsZGx1M1VwOEE9PSZEcEoxS1JKd3NKeEtWS25rN1JucG5kdWtDYjQ9; _routing_id="322ee1aa-07c3-458f-bbf5-0d025b6c0ef2"; sessionFunnelEventLogged=1'
    }
    global artistBoardUrl
    artistBoardUrl = "https://www.pinterest.co.uk/resource/BoardResource/create/"

    response = requests.request("POST", artistBoardUrl, headers=headers, data=payload)
    status_code = response.status_code

    if status_code == 200:
        print(artist + " board creation successful")
    elif status_code == 400:
        print(artist + " board failed to create")
    elif status_code == 429:
        print("Too many requests")
    content = response.content
    parsedResponse = json.loads(content)
    global boardId
    boardId = parsedResponse["resource_response"]["data"]["id"]


def update_board(artist):
    string_guides_array = ", ".join(guides_array)
    stringify_list = str(string_guides_array)
    url = "https://www.pinterest.co.uk/resource/BoardResource/update/"
    source_url = "/whatguitarshouldibuy/boards/&data="
    global description
    description = ',"description":"' + artist + '. How to sound like ' + artist + '. My site can show you what guitar to buy to sound like ' + artist + '.' + stringify_list
    data = '{"options":{"board_id":"' + str(
        boardId) + '","name":"' + artist + '"' + description + '","privacy":"public","allow_homefeed_recommendations":true},"context":{}}'
    encoded_data = urllib.parse.quote(data, safe="")
    payload = source_url + encoded_data
    headers = {
        'authority': 'www.pinterest.co.uk',
        'x-pinterest-appstate': 'active',
        'x-app-version': 'fd3c85b',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': 'application/json, text/javascript, */*, q=0.01',
        'x-pinterest-experimenthash': '34879610e323f52518c71f6af2b94994d1a5ff53db42df4021881df51763093129a043acc2fa9cdc15bccb886e022a7b52145c13f6ca18d95296717a802d2e28',
        'x-csrftoken': '34d8c022b199d4258a6f48e00a1a9aa3',
        'origin': 'https://www.pinterest.co.uk',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.pinterest.co.uk/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'csrftoken=34d8c022b199d4258a6f48e00a1a9aa3; cm_sub=denied; fba=True; fbm_274266067164=base_domain=.www.pinterest.co.uk; bei=false; logged_out=True; g_state={"i_p":1593165670442,"i_l":4}; _auth=1; _pinterest_sess=TWc9PSZOcHg4SndXZGtnbzV0ZWNFcGhEcW0raEpFR3BFdGlsQ29PYU1OdFZlN29WUDVhZ1I0WFk1anhNS0gyeWlKZWdpeXIzdjd3aDZnc1NReExTZDVCdHNUWjU5SVJ3MkVCYmcwQ0poSFVlNzQwb0pyOGN5cTFwQ1RIcHp5L0czYVlUazBWZ01CWGkxditveGRlL0oxK2cwWVQxZkNwc09KMkpIRjlueFdwTXk2UU1lOGR3eUc0MEdRVFNSZy94bFU3UHhxOGRhQmRkNVZLQzAxZkN3RmtEZ2t0S1U5Vm81Mytzc21QVTlqTGJpSVArZTNSa2tRRlVpNUlQRDJUK0E5Vm9tY20wYU51ek1XdFp0eXRNQkxqRTN3RXFZUFludjVaaDhkZlJCdDYvckNzR1dIZ3drSzBmSUgvb2ZvT1BoTVlGQWpuZnNUVHBpajFkc2RTandqS3lGanNFUEVSakFwdUIzN2Y1SWUyYjJ5TzZTd2dsWlBvS2VkQVlaSUg3T2JWc3o0WUh0NEgzL3hmRlRRb0pQaHllc1ZDUDR3ZUdxaGxFY2lMY0cwdnAzVS9jQ0tacElBVit2MldDNGs1RzNtaGttMnpEK3JNb0xJdVd6R29zdlV3bncxT2hFMnJRZGxGZnhWbjN4dGdwQ3Q1RG5SZUhhUWRMcmkvY3N1d1hZdERuMHYvdDdrbFJYRjIvbVpRdDgxK2lVME8rdmdmS3g4dDhqNUVaWGU5RkdDRk5vZ205Ty9Lb3FGTWlXVm9UYTlBdWFUZHl4RUtZa01FM0NXSkVCSnZQTEVzdlgxcFpzQmxqV2l3TDFENHA3VloxM2I0cld2L3FpL20zbmUxVVZxemkvM1ZZanNkMW1hQW1yMk9xZTVhVjdsZVdyYTVEZ0YyTWRYS09lOU50T2FiV0tNRUFQQVdtWURocXAyanMwQ2NXUjdzMUcvOTI2QmFpREJsMUYrWG9ySzVxell6WXk0bzF1MHJrNnJHalNkb2lxTWFGbnh5bFh0WmtZQlNFbWJRVW1ta2dXdlovZlhmaThjakJmcnhHU25CZGNmUlZGTkFTblhSRTA4bkVldWh1ZFdJeXo3RkZkUW5mV00zZHNyV3Q5VFMraHpGbndvckJtVlh0RW1qTEpMbThVQS9QZmo5eHFRU2tURE5RQjZVejd2QnpBby9DTzI0UjFZdDdUUlo4dVhDd1JRQ3J6OUJQU2lPZ09VcW9ocnB2S0sxV3JlR1FnVDREWHFLdVF5UWRsV3N4RytPZmgwcWg5cFpOUG9pc3FIc0U1VWRlZkI4VWtLdDBlVDYvWThVeGNzd1pJSXRaU1hab2ExaU5QQisyZVh2OHVDVnJRMmNpdkVNZzVBUFAxWVllV0FVamJxdFEvZGVMbHpNbnF5NEptZXNMRXI5MUVkUjZDU3pjSWdJd1VqMHMwbCt3MWNEVjVKcWZyemcwcjJBR2NpQ0JzTk1qSHYzYkhPVmJCVGVaQXpHUFJlQmdYalhCWTJKQWRCVWU5VjVySFowVjhqV2QvWE8vRGN5VSsvWTljejJaK1BUOTNKeGE1SGlGSE9zVGtuU3krZjVrbm45SFgxMnF2MjVkcXVlWGNFK3ppTjJKWTJ5d1Uyb1RzYW16RUZKN0F4NVhDODhPS2pDYTc3czRHRm1aSjhOSEdnRmJrNUdFazJlQnNzanVMVHNyTnFkeXk4ZVZXTDk5RkxFd2F3R3pMN2N2YUFCaUh1enpyWDNNdXc1YjNoYVk4NDRyNkxmeHJxRTNJdEpiR29YSXh5RURLU1hFSmlPS1VPMWpIR2lPMjUxMzVxaUFqRGIyRzdPSEM4VEovenhoQ3BLSkNGcmttSWZ5RmpUUElmRlY1WXU1Y3dRTEJhTlRlZWZRRTk1WFcrUW9wZ2lyVTVMeDUybFUzK2dkK05qQVd1NWdVY253RmtLbjFlUStPUU5rMVB3YW5Wd1ZxZmFTaFVHaUpsTmRHYXdXa1NsZGx1M1VwOEE9PSZEcEoxS1JKd3NKeEtWS25rN1JucG5kdWtDYjQ9; _routing_id="322ee1aa-07c3-458f-bbf5-0d025b6c0ef2"; sessionFunnelEventLogged=1'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    status_code = response.status_code
    if status_code == 200:
        print(artist + " board update successful")
    elif status_code == 400:
        print("Board failed to update description")
    elif status_code == 429:
        print("Too many requests")


def search_for_pins(artist):
    search_url(artist)
    headers = {
        'authority': 'www.pinterest.co.uk',
        'accept': 'application/json, text/javascript, */*, q=0.01',
        'x-pinterest-appstate': 'active',
        'x-app-version': 'b4982f8',
        'x-requested-with': 'XMLHttpRequest',
        'x-pinterest-experimenthash': 'ee4a0545694b2b10cbd40923f509b0ba04c149fca39c75638ab25ec000ee9b482a28d4b2849ce2ef29d2caa0048e08ece68241c227753cb9580be666c6dbb8f7',
        'user-agent': 'Chrome/81.0.4044.138',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.pinterest.co.uk/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'csrftoken=34d8c022b199d4258a6f48e00a1a9aa3; bei=false; cm_sub=denied; logged_out=True; fba=True; g_state={"i_p":1588835383497,"i_l":2}; ujr=1; fbm_274266067164=base_domain=.www.pinterest.co.uk; _auth=1; _pinterest_sess=TWc9PSZ1WUxsbE5zaW1qOUltc1ppV2d3UTZ2emdBRGlOdEJ4dlptU2dvMHB2SlIzN01rVDlxcEFna21ocWNoMGZJT2dBZjR4Qk5yTVgwRlVUR2R2enNHRlVWRnBFYWtGYnkwK3VmZTJ3K2JHakZJMXNUeEZHVHFFaFE4ZFpyZy9FRjBGNnB2S0JEZCtsd3ZhL0xyazBWd0I3d3dJRFRORTFUOHJrYUxmTjF2NnMvK1l0UmZlM004NEdaTi9MTDJLalg5RFY4SG5vV05Md2hNdGJJZHFWelVsTTZyUDlRYld1SmUxZkh0eG9RSitoMGh4VGpWcGVkUGprV1pnRVFmL3hlOWQ4L2JueFd4dnZqZzUxd2FxUDVZTVNCd3lDVS9aZ2VkRlRlOU1WSC8zWTIwWkNtNnhGMHk0RUgzV0hIVURWOGNyZ00rcHd3VExtMmZWeFFxNk02bE1WVklJQnZlMVBHZWFkVEhyRHlrU2dXdmtaTzkvQmlGd050RlNZYzFWV1N5bThWdWs1cGNsS0xLQW5CUWoxTHpuQ1VNQWVtaFVtdGROWHEwcHpySmVrb09uTEdKYkFoTnA3cEo0THNMT25nWWYxejliQTY5M2xvbENUNHpVclNLT05rT2gxMlJTYWtjYTRnVGgycTJ6SmdIWWVOV2U1QjZxbEFHUVNrU1FMbk15VlptVHU2VVVFNXZ4ZGdhRXBHcTB6U2pzVU9sV3JYMjJBRnNwWVd2czQ2K1ovOHdtVnBRUThYWkh4WjlzdE5pUjNzUVBKWldNM21SaWp1akJ5YmFkSjFuVnlDV1JtbzRLUzZxVm1pSkNkaVN2RkFDQi9mY3R1bXczRVArZFYxS1JtNHJYaVFqSmZxaHg2TGVkOE9wYjl2SkpYU2JPRnZBYkhteTlFNGptOXBmRjR4dlJTN0VJZWNBUTdhSUV1elowV3ZYU0dDeUVpOWZ0YitoSUdYQWQyWVVvWmNlT3Q1K0pRNnZOcWYwWlJDVm5YSWNtcTQ1a2NjNGRBTG1hdmhSOE40QnZCN1pUR2ZmVVJGcHJLTXN6Y2xKeGN3ZHpwVWlxMkVSY2g4V1Y2cGlYTUMrT1RsNTFSZytOVTVFeE84Q2hVdW9PcUZMM3VpS3JjWGRVeW0yQWhuTklBNDlaTzhPbnF2aDJyOGxBb1FicCtlN1Qvc2l1UHpJWWdHeDhaaXBHNUtIQUpTZ0hsamdKVkpoNkRjb3hOR3Z3a1YrQVFMYzd3SFFmRzZMTTJVdTZBM2IwNUsyRnVzNkJnM3JqNVVvUFhrSnhoQTQ1Wk9sWXJORHcyZ25BMWxyWGFPT2VWUnZsTVJ2S3dOZGE3ZysvbjAyaHdLcHozSUFRbXJrOEl2ODZpNThKdGFRcXB3MUx5VGd2dzBadmsrQ2tQbFE3RytBc2VYd0Z5aTd6RzVnREI3U2NiZVQxTk9jMjh6eXErbHdNZTN4TzdyelVGNCszY3F6TTIrUFRHMUU4aWVTSzZVbStXZ2tLZ21Va0E3VmlTSlFKN0pqRmlURGFnaTlXY3gxaERKSXRYeDA3R25oZDVWUW9OYmhYaFdHZ3dScCtmek1EUzJkcGF3bzIwa29lcHloMGQ2ZW12YjhWZXFlUmdhWTFka0R1WFVOSUdpQlYvYU9jdWdYSDF3elVLd3c2R25UZFMxT3hDSnF3SUFPVzNPc1JaeTJoR1psZlhpdk0yTzNyM0Z6TVpxalE2WUtlcjRjWVdsZ3J0V3JGY1RqN0FtRWF5K0lrTHo0TUk3R3EyUU12eTJFSkVCM1NubDIzQnN6S2VzK0R3OEpOdEwwSXBOTFlwNm1YdS9HYnhhN2ZLMjlUQ0xKTHJRTWx0OWVHaFVEMDhTQmxVQ083WWlpYmYrbVpZJnVhM3BLN0dYL2NYdlFmb1drQXEvM2h2WHNxcz0=; sessionFunnelEventLogged=1; _routing_id="9490e57c-60cd-4399-a1df-8686ee5f3793"'
    }
    payload = {}
    search_response = requests.request("GET", artistSearchUrl, headers=headers, data=payload)
    response_body = search_response.text
    parsed = json.loads(response_body)
    results_array = parsed["resource_response"]["data"]["results"]
    description_array = []
    for n in results_array:
        description = n["description"]
        no_emoji_description = emoji_pattern.sub(r'', description)
        description_array.append(no_emoji_description)
    link_array = []
    for m in results_array:
        link = m["link"]
        string_link = str(link)
        new_string_link = string_link.replace("https:", "https%3A")
        # slash_replace = new_string_link.replace("/", "%2F")
        if link is not None:
            link_array.append(new_string_link)
        elif link is None:
            link_array.append("None")
    title_array = []
    for o in results_array:
        title = o["title"]
        title_array.append(title)
    pin_id_array = []
    for r in results_array:
        pin_id = r["id"]
        pin_id_array.append(pin_id)

    splitArtist = artist.split(" ")

    # splitArtist is an array of the names of the artist
    array = []
    for n in splitArtist:
        output = ("&term_meta[]=" + n + "%7Crecentsearch%7C0")
        array.append(output)
    artistString = ''.join(array)
    source_url = "?q=" + urlencodedartist + "&rs=rs&eq=&etslf=311" + artistString
    encoded_source_url = urllib.parse.quote(source_url, safe="")
    data = "&data="
    # create the pin payloads from the results response
    i = 0
    while i <= 20:
        payload_array = []
        first_half_payload = '{"options":{"description":"' + description_array[i] + '"' + ',"link":"'
        encoded_first_half_payload = urllib.parse.quote(first_half_payload, safe="")
        # slash_link = link_payload.replace()
        link_payload = link_array[i]
        second_half_payload = '","title":"' + title_array[
            i] + '","clientTrackingParams":"CwABAAAAEDgxMDY4NjgwMTM2NDk1NTUGAAMACAA'
        third_half_payload = '","board_id":"' + str(
            boardId) + '","pin_id":"' + pin_id_array[
                                  i] + '","is_buyable_pin":false,"is_removable":false,"carousel_slot_index":0},"context":{}}'
        encoded_second_half_payload = urllib.parse.quote(second_half_payload, safe="")
        encoded_third_half_payload = urllib.parse.quote(third_half_payload, safe="")
        payload = encoded_first_half_payload + link_payload + encoded_second_half_payload + '%7E0' + encoded_third_half_payload
        payload_array.append(payload)
        url = "https://www.pinterest.co.uk/resource/RepinResource/create/"
        full_payload = 'source_url=/search/pins' + encoded_source_url + data + payload
        headers = {
            'authority': 'www.pinterest.co.uk',
            'x-pinterest-appstate': 'active',
            'x-app-version': 'fd3c85b',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': 'application/json, text/javascript, */*, q=0.01',
            'x-pinterest-experimenthash': '34879610e323f52518c71f6af2b94994d1a5ff53db42df4021881df51763093129a043acc2fa9cdc15bccb886e022a7b52145c13f6ca18d95296717a802d2e28',
            'x-csrftoken': '34d8c022b199d4258a6f48e00a1a9aa3',
            'origin': 'https://www.pinterest.co.uk',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.pinterest.co.uk/',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cookie': 'csrftoken=34d8c022b199d4258a6f48e00a1a9aa3; cm_sub=denied; fba=True; fbm_274266067164=base_domain=.www.pinterest.co.uk; bei=false; logged_out=True; g_state={"i_p":1593165670442,"i_l":4}; _auth=1; _pinterest_sess=TWc9PSZOcHg4SndXZGtnbzV0ZWNFcGhEcW0raEpFR3BFdGlsQ29PYU1OdFZlN29WUDVhZ1I0WFk1anhNS0gyeWlKZWdpeXIzdjd3aDZnc1NReExTZDVCdHNUWjU5SVJ3MkVCYmcwQ0poSFVlNzQwb0pyOGN5cTFwQ1RIcHp5L0czYVlUazBWZ01CWGkxditveGRlL0oxK2cwWVQxZkNwc09KMkpIRjlueFdwTXk2UU1lOGR3eUc0MEdRVFNSZy94bFU3UHhxOGRhQmRkNVZLQzAxZkN3RmtEZ2t0S1U5Vm81Mytzc21QVTlqTGJpSVArZTNSa2tRRlVpNUlQRDJUK0E5Vm9tY20wYU51ek1XdFp0eXRNQkxqRTN3RXFZUFludjVaaDhkZlJCdDYvckNzR1dIZ3drSzBmSUgvb2ZvT1BoTVlGQWpuZnNUVHBpajFkc2RTandqS3lGanNFUEVSakFwdUIzN2Y1SWUyYjJ5TzZTd2dsWlBvS2VkQVlaSUg3T2JWc3o0WUh0NEgzL3hmRlRRb0pQaHllc1ZDUDR3ZUdxaGxFY2lMY0cwdnAzVS9jQ0tacElBVit2MldDNGs1RzNtaGttMnpEK3JNb0xJdVd6R29zdlV3bncxT2hFMnJRZGxGZnhWbjN4dGdwQ3Q1RG5SZUhhUWRMcmkvY3N1d1hZdERuMHYvdDdrbFJYRjIvbVpRdDgxK2lVME8rdmdmS3g4dDhqNUVaWGU5RkdDRk5vZ205Ty9Lb3FGTWlXVm9UYTlBdWFUZHl4RUtZa01FM0NXSkVCSnZQTEVzdlgxcFpzQmxqV2l3TDFENHA3VloxM2I0cld2L3FpL20zbmUxVVZxemkvM1ZZanNkMW1hQW1yMk9xZTVhVjdsZVdyYTVEZ0YyTWRYS09lOU50T2FiV0tNRUFQQVdtWURocXAyanMwQ2NXUjdzMUcvOTI2QmFpREJsMUYrWG9ySzVxell6WXk0bzF1MHJrNnJHalNkb2lxTWFGbnh5bFh0WmtZQlNFbWJRVW1ta2dXdlovZlhmaThjakJmcnhHU25CZGNmUlZGTkFTblhSRTA4bkVldWh1ZFdJeXo3RkZkUW5mV00zZHNyV3Q5VFMraHpGbndvckJtVlh0RW1qTEpMbThVQS9QZmo5eHFRU2tURE5RQjZVejd2QnpBby9DTzI0UjFZdDdUUlo4dVhDd1JRQ3J6OUJQU2lPZ09VcW9ocnB2S0sxV3JlR1FnVDREWHFLdVF5UWRsV3N4RytPZmgwcWg5cFpOUG9pc3FIc0U1VWRlZkI4VWtLdDBlVDYvWThVeGNzd1pJSXRaU1hab2ExaU5QQisyZVh2OHVDVnJRMmNpdkVNZzVBUFAxWVllV0FVamJxdFEvZGVMbHpNbnF5NEptZXNMRXI5MUVkUjZDU3pjSWdJd1VqMHMwbCt3MWNEVjVKcWZyemcwcjJBR2NpQ0JzTk1qSHYzYkhPVmJCVGVaQXpHUFJlQmdYalhCWTJKQWRCVWU5VjVySFowVjhqV2QvWE8vRGN5VSsvWTljejJaK1BUOTNKeGE1SGlGSE9zVGtuU3krZjVrbm45SFgxMnF2MjVkcXVlWGNFK3ppTjJKWTJ5d1Uyb1RzYW16RUZKN0F4NVhDODhPS2pDYTc3czRHRm1aSjhOSEdnRmJrNUdFazJlQnNzanVMVHNyTnFkeXk4ZVZXTDk5RkxFd2F3R3pMN2N2YUFCaUh1enpyWDNNdXc1YjNoYVk4NDRyNkxmeHJxRTNJdEpiR29YSXh5RURLU1hFSmlPS1VPMWpIR2lPMjUxMzVxaUFqRGIyRzdPSEM4VEovenhoQ3BLSkNGcmttSWZ5RmpUUElmRlY1WXU1Y3dRTEJhTlRlZWZRRTk1WFcrUW9wZ2lyVTVMeDUybFUzK2dkK05qQVd1NWdVY253RmtLbjFlUStPUU5rMVB3YW5Wd1ZxZmFTaFVHaUpsTmRHYXdXa1NsZGx1M1VwOEE9PSZEcEoxS1JKd3NKeEtWS25rN1JucG5kdWtDYjQ9; _routing_id="322ee1aa-07c3-458f-bbf5-0d025b6c0ef2"; sessionFunnelEventLogged=1'
        }
        pin_response = requests.request("POST", url, headers=headers, data=full_payload)
        status_code = pin_response.status_code
        if status_code == 200:
            print(artist + " pin has been added successfully")
        elif status_code == 400:
            print(artist + " pin failed to save")
        elif status_code == 429:
            print("Too many requests")
        i += 1


def post_image_to_cloudinary(artist):
    lowercase_artist = artist.lower()
    dashed_lowercase_artist = lowercase_artist.replace(" ", "-")
    base_path = "/Users/rhysthomas/Documents/WhatGuitarShouldIBuy/Pinterest/"
    file_name = base_path + dashed_lowercase_artist + "/" + dashed_lowercase_artist + "-1.png"
    response = cloudinary.uploader.upload(file_name)
    global image_url
    image_url = str(response["url"])


def create_new_pin(artist):
    headers = {
        'authority': 'www.pinterest.co.uk',
        'x-pinterest-appstate': 'active',
        'x-app-version': 'a59ed29',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Chrome/81.0.4044.138 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': 'application/json, text/javascript, */*, q=0.01',
        'x-pinterest-experimenthash': '1877a9b978cc56aa918cfaaca60245cb86f370d795d0df6a787cc9de22aab6c548dee6f6fcceb591bc69204f832b9d0cdf06126fb2045e23a2113ae040a90d7d',
        'x-csrftoken': '34d8c022b199d4258a6f48e00a1a9aa3',
        'origin': 'https://www.pinterest.co.uk',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.pinterest.co.uk/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'csrftoken=34d8c022b199d4258a6f48e00a1a9aa3; bei=false; cm_sub=denied; logged_out=True; fba=True; ujr=1; fbm_274266067164=base_domain=.www.pinterest.co.uk; g_state={"i_p":1589952156306,"i_l":3}; _auth=1; _pinterest_sess=TWc9PSZTWmh6dmVZc3RwUmNiMTJCYXg3TnBvRnBWQnQ1QTFWU3lTM0NBTThPOHRzY0dDbkxsaWhxRmwxQWc3cGJyc2hCcTFFM3ZQOVJUbUc1S0lmWFNEc0ljM24wY1NTZ1lWcW9FRENUc0ZuUURxTFFKbzJuQ0hTZi9ma3VtN1dZWUtlaGZuaUs3b1ppT0lnRXp4YWt4OHhIRWlScWpMZE55UHQycXlrMnR3c0Z2Y1FLdWZkeHpqM2Y3RUkzd2RKWTFPWVdpbG9rWVQ5UzZLM2k5MDBUNGptVk1aUXl6UTIyYmp2ZmVJRUgwVU44MFJCR254RDFudTV0VjUzR2lzQnhxcmF6aWR4ZHBmdXhCTTVndEQ2MkI3ejRTY200ZnJScWs5dU9mZEN6OUx0cWs1bURNbllqTFQ2WWZnSmNjdXc1Q2pzMHAyaVFHQzFNZDlyS0tzY1BSMWpyaHRrVTY2SnBrZHhxLzl1ZExpbVd1c2gybnNsZHRzSDZJN3RzZnBRZ01JaG4zcnNVRnNXMGZRb1Y0djJ2Mld2VnF5V1NIendmZDZVUEd2eEJvVmJvUmc1NXduMDlaODk4VTlWSFRKSkVtVStIT3UzWnlWSm1SRllEQnZhM3U1bEZRT25OQmRyMWpyZzRheEUveklUc2V3aE0rZ3prb3psZ25uL0JvUjFkTGJLNmtLMSswWGc0dG5SQzA3MmE2dGpwUzJsSU81bmdxZ1FpWjVSL1piSjhVdXZTWE9xY09jUmVHZWxTaU5sVjcvRkdZd25tZXFDWWZTUjd0MVNWakJtUS9DTXNNbDRWbXhlb09wQWtQTVZDbllJVjFiaGRRSUx6eGxDWUViSEw4QmpKeGNVcGFDNDd1QkJzd1VqTFcycW95Wldkcnpsbm96U3BpSlNtVUR1MnJ2L0JpYlFKTE0zUy9ORU9VVURQK0p6NW81RFZ0c2llRGlQamNaRjZoamw5QWFJRlEza0QrdG8zTDJSM3Y0Y0JzZFd6a050Vk1KR0JHSlhlZmdDRUtiRXJtMHJhN3RYakFCNTJ6d3dCUHhnM1NmQWI3aDAyRUhzS0NhbDJLS2VsNHllc1d4YzVWejlYbWhjK3hhaHIvOG1IS2loL3M4anREbnhJMldEdVZja1Jpb0crWE1HVnd2clNRREs3cGlxa21mUEtZWG5PblU3UGVOWVF0VGp6c2hUUE5EeExDOHZoaUIxZXByeXhFeXdFblVyYmxaclhkQTRzM3BjTG5Oc3lxRWhuc04ramhsQ1AwS0xCcVJ0N2gvSmZMKzAvVXdnVnhrSzBpYkRtRmUwampHRjB1Y3BNbE5YbjdSc0V5Q2NHNzBlRkhUUm5Lc3pkYW5mZUxMazBTazBuKy95KzhmL1RFV1M1TXA3a1RxSHllWjBxK2tJeDZWTG9kOHp4ZnZ5Rnp5Umkyc3BNVzJEMDI0dk1TVko3UHo0S21Kd29rVlpVYnVhVEh3QUV2bTdtZ2hEQ1kyOFloSU9LU05oVExOMWhhbElhSkgvMGtXbEM5VkVOSHR0a3RtblpWTHlFOFZDN3lEQzhQUGxnWERMTUZhZEhOalU5dmhMWU00MTF5T1NQZVE2RUJmUi96aC8wb2dIazJHeVlIMVJHQzIrZWR4ZjI5UUYySkhaTms5eXV1TS9NTngxYUlzTXI1cVNseGFBTGY1L0dmeTFIeGFGVy9oY0hCVXVqdDBtdUxhKzZia0dEdzczK1NLamVVS0ppbWgzTmFJdEtXVzZwK0JSaVQrNzdlME41YWRaeU5QVXBQd25HdlV3dUxZTnRGV1JCZnREZnRHVTM5cWswUXBTN3p1c3R3UmFTMkgySnorUWdRZVVFWnNGSDhySThyN25EaG83QjAvOHB2ckJsSm52cHVhTGk5Wk5oekNRSkZCMGVLM0YvR25ySGJvVWRsQk95T0RNTVYyQXR4VVNJSGJLQjNrWDN4dTJlT3J5YThveVY5R2hQUG4vZzlacER6YjdKMGc9PSY2S3JNUW9JeUMrRXYvTjZsY1hWR0dPQi9zZE09; sessionFunnelEventLogged=1; _routing_id="cd08e9c5-a15c-4f33-824d-d748ea3e2404"',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    lowercase_artist = artist.lower()
    dashed_lowercase_artist = lowercase_artist.replace(" ", "-")
    base_url = "https://www.pinterest.co.uk/resource/PinResource/create/"
    encoded_pin_builder = urllib.parse.quote("/pin-builder/", safe="")
    source_url = 'source_url=' + encoded_pin_builder + '&data='
    encode_image_url = image_url.replace("https://", "https%3A%2F%2F")
    global replaced_slash_image_url
    replaced_slash_image_url = encode_image_url.replace("/", "%2F")
    first_half = '{"options":{"board_id":"' + str(
        boardId) + '","field_set_key":"create_success","skip_pin_create_log":true' + description + '","link":"whatguitarshouldibuy.com/' + dashed_lowercase_artist + '","title":"How to sound like ' + artist + '","image_url":"'
    second_half = '","method":"uploaded","upload_metric":{"source":"partner_upload_standalone"}},"context":{}}'
    encoded_first_half = urllib.parse.quote(first_half, safe="")
    encoded_second_half = urllib.parse.quote(second_half, safe="")
    payload = source_url + encoded_first_half + replaced_slash_image_url + encoded_second_half
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
        'x-pinterest-appstate': 'active',
        'x-app-version': 'a59ed29',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Chrome/81.0.4044.138 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': 'application/json, text/javascript, */*, q=0.01',
        'x-pinterest-experimenthash': '1877a9b978cc56aa918cfaaca60245cb86f370d795d0df6a787cc9de22aab6c548dee6f6fcceb591bc69204f832b9d0cdf06126fb2045e23a2113ae040a90d7d',
        'x-csrftoken': '34d8c022b199d4258a6f48e00a1a9aa3',
        'origin': 'https://www.pinterest.co.uk',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.pinterest.co.uk/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'csrftoken=34d8c022b199d4258a6f48e00a1a9aa3; bei=false; cm_sub=denied; logged_out=True; fba=True; ujr=1; fbm_274266067164=base_domain=.www.pinterest.co.uk; g_state={"i_p":1589952156306,"i_l":3}; _auth=1; _pinterest_sess=TWc9PSZTWmh6dmVZc3RwUmNiMTJCYXg3TnBvRnBWQnQ1QTFWU3lTM0NBTThPOHRzY0dDbkxsaWhxRmwxQWc3cGJyc2hCcTFFM3ZQOVJUbUc1S0lmWFNEc0ljM24wY1NTZ1lWcW9FRENUc0ZuUURxTFFKbzJuQ0hTZi9ma3VtN1dZWUtlaGZuaUs3b1ppT0lnRXp4YWt4OHhIRWlScWpMZE55UHQycXlrMnR3c0Z2Y1FLdWZkeHpqM2Y3RUkzd2RKWTFPWVdpbG9rWVQ5UzZLM2k5MDBUNGptVk1aUXl6UTIyYmp2ZmVJRUgwVU44MFJCR254RDFudTV0VjUzR2lzQnhxcmF6aWR4ZHBmdXhCTTVndEQ2MkI3ejRTY200ZnJScWs5dU9mZEN6OUx0cWs1bURNbllqTFQ2WWZnSmNjdXc1Q2pzMHAyaVFHQzFNZDlyS0tzY1BSMWpyaHRrVTY2SnBrZHhxLzl1ZExpbVd1c2gybnNsZHRzSDZJN3RzZnBRZ01JaG4zcnNVRnNXMGZRb1Y0djJ2Mld2VnF5V1NIendmZDZVUEd2eEJvVmJvUmc1NXduMDlaODk4VTlWSFRKSkVtVStIT3UzWnlWSm1SRllEQnZhM3U1bEZRT25OQmRyMWpyZzRheEUveklUc2V3aE0rZ3prb3psZ25uL0JvUjFkTGJLNmtLMSswWGc0dG5SQzA3MmE2dGpwUzJsSU81bmdxZ1FpWjVSL1piSjhVdXZTWE9xY09jUmVHZWxTaU5sVjcvRkdZd25tZXFDWWZTUjd0MVNWakJtUS9DTXNNbDRWbXhlb09wQWtQTVZDbllJVjFiaGRRSUx6eGxDWUViSEw4QmpKeGNVcGFDNDd1QkJzd1VqTFcycW95Wldkcnpsbm96U3BpSlNtVUR1MnJ2L0JpYlFKTE0zUy9ORU9VVURQK0p6NW81RFZ0c2llRGlQamNaRjZoamw5QWFJRlEza0QrdG8zTDJSM3Y0Y0JzZFd6a050Vk1KR0JHSlhlZmdDRUtiRXJtMHJhN3RYakFCNTJ6d3dCUHhnM1NmQWI3aDAyRUhzS0NhbDJLS2VsNHllc1d4YzVWejlYbWhjK3hhaHIvOG1IS2loL3M4anREbnhJMldEdVZja1Jpb0crWE1HVnd2clNRREs3cGlxa21mUEtZWG5PblU3UGVOWVF0VGp6c2hUUE5EeExDOHZoaUIxZXByeXhFeXdFblVyYmxaclhkQTRzM3BjTG5Oc3lxRWhuc04ramhsQ1AwS0xCcVJ0N2gvSmZMKzAvVXdnVnhrSzBpYkRtRmUwampHRjB1Y3BNbE5YbjdSc0V5Q2NHNzBlRkhUUm5Lc3pkYW5mZUxMazBTazBuKy95KzhmL1RFV1M1TXA3a1RxSHllWjBxK2tJeDZWTG9kOHp4ZnZ5Rnp5Umkyc3BNVzJEMDI0dk1TVko3UHo0S21Kd29rVlpVYnVhVEh3QUV2bTdtZ2hEQ1kyOFloSU9LU05oVExOMWhhbElhSkgvMGtXbEM5VkVOSHR0a3RtblpWTHlFOFZDN3lEQzhQUGxnWERMTUZhZEhOalU5dmhMWU00MTF5T1NQZVE2RUJmUi96aC8wb2dIazJHeVlIMVJHQzIrZWR4ZjI5UUYySkhaTms5eXV1TS9NTngxYUlzTXI1cVNseGFBTGY1L0dmeTFIeGFGVy9oY0hCVXVqdDBtdUxhKzZia0dEdzczK1NLamVVS0ppbWgzTmFJdEtXVzZwK0JSaVQrNzdlME41YWRaeU5QVXBQd25HdlV3dUxZTnRGV1JCZnREZnRHVTM5cWswUXBTN3p1c3R3UmFTMkgySnorUWdRZVVFWnNGSDhySThyN25EaG83QjAvOHB2ckJsSm52cHVhTGk5Wk5oekNRSkZCMGVLM0YvR25ySGJvVWRsQk95T0RNTVYyQXR4VVNJSGJLQjNrWDN4dTJlT3J5YThveVY5R2hQUG4vZzlacER6YjdKMGc9PSY2S3JNUW9JeUMrRXYvTjZsY1hWR0dPQi9zZE09; sessionFunnelEventLogged=1; _routing_id="cd08e9c5-a15c-4f33-824d-d748ea3e2404"',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    source_url = "source_url=/whatguitarshouldibuy/boards/&data="
    first_half = '{"options":{"board_id":"' + boardId + '","url":"'
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
    get_search_results(artist)
    saving_guides()
    create_board(artist)
    update_board(artist)
    search_for_pins(artist)
    # post_image_to_cloudinary(artist)
    # create_new_pin(artist)
    # update_board_cover(artist)


full_process("Rock Music")
