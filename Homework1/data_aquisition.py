import urllib.request
import json

enigma_api= "6336800936fe4cd1fd565f4865f4e792"

url = 'https://api.enigma.io/v2/data/' + enigma_api

final_url = url + '/us.gov.dot.rita.trans-stats.on-time-performance.2009?conjunction=and'

json_obj = urllib.request.urlopen(final_url)

str_response = json_obj.readall().decode('utf-8')
data = json.loads(str_response) 

data2 = data['result'] 

final_data = []

wanted_keys = ['flightdate','flightnum','airlineid','carrier','originairportid','origincityname','originstatename','destairportid','destcityname','deststate','deptime','arrtime','lateaircraftdelay','arrdelay','divarrdelay','depdelay','weatherdelay','securitydelay','depdelayminutes','nasdelay','carrierdelay'] # specify needed keys
for dic_item in data2:
    newdict = {k: dic_item[k] for k in set(wanted_keys) & set(dic_item.keys())}
    final_data.append(newdict)

errflag = 0
try:
    #Open a json file for writing
    file = open("C:/Users/Poonam/Desktop/FlightData.json","w")
    
    #write data to file
    json.dump(final_data,file,indent=4)
    
    #close a file
    file.close()
    
except IOError as e:
    errflag = 1
    print("Exception caught: ({})".format(e))

if(errflag == 0):
    print("Data is saved to FlightData.json file!")
else:
    print("Error in file!")





