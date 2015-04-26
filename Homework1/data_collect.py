
__author__ = 'Poonam'

import urllib.request
import json

enigma_api= "6336800936fe4cd1fd565f4865f4e792"
url = 'https://api.enigma.io/v2/data/' + enigma_api
url2 = url + '/us.gov.dot.rita.trans-stats.on-time-performance.2009?page='

n=11
for i in range(1,n):
    final_url = url2 + str(i)
    json_obj = urllib.request.urlopen(final_url)
    final_url = ""
    str_response = json_obj.readall().decode('utf-8')
    data = json.loads(str_response)
   
    required_data = data['result'] 

    final_data = []

    wanted_keys = ['flightdate','flightnum','airlineid','carrier','originairportid','origincityname','originstatename','destairportid','destcityname','deststate','deptime','arrtime','lateaircraftdelay','arrdelay','divarrdelay','depdelay','weatherdelay','securitydelay','depdelayminutes','nasdelay','carrierdelay'] # specify needed keys
    
    for dic_item in required_data:
        newdict = {k: dic_item[k] for k in set(wanted_keys) & set(dic_item.keys())}
        final_data.append(newdict)

    errflag = 0
    
    try:
        #Open a json file for appending
        file = open("C:/Users/Poonam/Desktop/FlightData.json","a")
    
        #write data to file
        json.dump(final_data,file,indent=4)
    
        #close a file
        file.close()
    
    except IOError as e:
        errflag = 1
        print("Exception caught: ({})".format(e))
        
    if(errflag == 0):
        print("Data collected for page " + str(i))

print("Data is saved to FlightData.json file!")
