import requests
import urllib.request
import urllib.parse

#
# def getData(url, src="r"):
# 	if src=="r":
# 		r = requests.get(url)   #, verify =False
# 		return r.content
# 	if src== "u":
# 		with urllib.request.urlopen(url) as doc:
# 			return doc.read()
#
# def getGreeting(fname, lname):
# 	url = "https://cs.coe.edu/~shughes/DS230/greetingG.php"
# 	url += "?fname="+fname
# 	url += "&lname="+lname
# 	print(getData(url))
#
# def getGreetingPost(fname, lname):
# 	url = "https://cs.coe.edu/~shughes/DS230/greetingP.php"
# 	postVals = {"lname":lname, "fname":fname}
# 	r = requests.post(url,postVals)
#
# 	data = urllib.parse.urlencode(postVals).encode()
# 	with urllib.request.urlopen(url, data= data) as doc:
# 		return doc.read()
#
# 	#return r.content
# print(getGreetingPost("Ralph","Smith"))
#
#
# #url = "https://cs.coe.edu/~shughes/DS230/Kittens.html"
# url = "https://cs.coe.edu/~shughes/DS230/greetingG.php?fname=Jenny&lname=Hughes"
# #print(getData(url))
# #print(getData(url, src= "u"))
#
# #getGreeting("Steve", "Hughes")


# def getJson(url, query = {}):
# 	r = requests.get(url, params= query)
# 	print(r.text)
# 	return json.loads(r.text)
#
# url = "https://cs.coe.edu/~shughes/DS236/Parts/partName.php"
# q = {"pName": "whozit"}
#
# url = "https://cs.coe.edu/~shughes/DS230/Parts/parts.php"
# d = getJson(url)
#
#
# parts = d["parts"][0]
# print(parts, type(parts))
# for part in parts:
# 	for k,v in part.items():
# 		print(k,v)


# def getJson(url, query = {}):
# 	r = requests.get(url, params= query)
# 	print(r.text)
# 	return json.loads(r.text)
#
# url = "https://api.zippopotam.us/"
# q = {
#    "post code": "90210",
#    "country": "United States",
#    "country abbreviation": "US",
#    "places": [
#        {
#            "place name": "Beverly Hills",
#            "longitude": "-118.4065",
#            "state": "California",
#            "state abbreviation": "CA",
#            "latitude": "34.0901"
#        }
#    ]
# }
#
# url = "https://api.zippopotam.us/country/state/city"
# d = getJson(url)
#
#
# parts = d["Zip"][0]
# print(parts, type(parts))
# for part in parts:
# 	for k,v in part.items():
# 		print(k,v)


import requests

#Two part joke program

def get_programming_joke():
	try:
		url = "https://v2.jokeapi.dev/joke/Programming?type=twopart"
		response = requests.get(url)  #get method from the requests module

		#if fails raise error
		response.raise_for_status()

		#parsing the response json into a dictionary
		joke_data = response.json()

		#if the 'error' key is present and true it returns an error message
		if joke_data.get("error"):
			return "An error occurred fetching the joke."

		#extract the two parts of joke setup and delivery
		setup = joke_data["setup"]
		delivery = joke_data["delivery"]

		#displaying the joke
		return f"{setup}\n...\n{delivery}"
	except requests.exceptions.RequestException as e:  #matcheing the exception in the requests module
		return f"An error occurred: {e}"


if __name__ == "__main__":
	print(get_programming_joke())
