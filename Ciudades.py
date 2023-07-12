import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
while True:
   orig = input("Ingrese ciudad de origen: ")
   if orig == "quit" or orig == "S":
        break
   dest = input("Ingrese ciudad de destino: ")
   if dest == "quit" or dest == "S":
        break
   key = "9yKDQj9jxyIOLIiW2gNeTqRsKbCOnXUE"
   url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
   json_data = requests.get(url).json()
   print("URL: " + (url))
   json_data = requests.get(url).json()
   json_status = json_data["info"]["statuscode"]
   if json_status == 0:
      print("API Status: " + str(json_status) + " = A successful route call.\n")
      print("=============================================")
      print("Direccion desde " + (orig) + " to " + (dest))
      print("Duracion del viaje:   " + (json_data["route"]["formattedTime"]))
      print("Kilometros:           " + str("{: .1f}".format((json_data["route"]["distance"])*1.61)))
      print("=============================================")
      for each in json_data["route"]["legs"][0]["maneuvers"]:
          print((each["narrative"]) + " (" + str("{:.1f}".format((each["distance"])*1.61) + " km)"))
      print("=============================================\n")