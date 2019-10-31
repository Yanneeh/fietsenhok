import http.client, urllib.parse, json
print('Stationsafkortingen: (Ddr) Dordrecht \n'
      '                     (Gr)  Gorinchem \n'
      '                     (Ut)  Utrecht \n'
      '                     (Asd) Amsterdam \n'
      '                     (Rtd) Rotterdam \n'
      '                     (Nm)  Nijmegen \n')

key = {'Ocp-Apim-Subscription-Key': 'd5a7b838aba24fc0945c38492211bb55'}
X = input('Voer stationsafkorting in:  ')

params = urllib.parse.urlencode({
    'maxJourneys': '25',
    'station': X
})

try:
    conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
    conn.request("GET", "/public-reisinformatie/api/v2/departures?" + params, headers=key)

    response = conn.getresponse()
    responsetext = response.read()
    data = json.loads(responsetext)

    payloadObject = data['payload']
    departuresList = payloadObject['departures']

    for departure in departuresList:
        Datum = departure['actualDateTime']
        Time = Datum[11:16]
        Direction = departure['direction']
        Spoornummer = departure['plannedTrack']
        product = departure['product']
        Typetrein = product['shortCategoryName']
        print('Richting: {:23},{:20}Tijd: {}    Spoornummer: {}'.format(Direction,Typetrein,Time,Spoornummer))

    conn.close()
except Exception as e:
    print("Fout: {} {}".format(e.errno, e.strerror))