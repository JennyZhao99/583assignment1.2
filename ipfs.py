import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	# convert python dictionary to JSON
	json_data = json.dumps(data)

	# upload JSON data to IPFS API
	url = "https://ipfs.infura.io:5001/api/v0/add"
	response = requests.post(url, files={"file": json_data})
	
	# check if successful
	if response.status_code == 200:
		result = response.json()
		cid = result["Hash"]
		return cid
	else:
		raise Exception(f"Failed to pin data to IPFS: {response.text}")

	#return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	

	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
