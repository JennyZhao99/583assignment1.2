import requests
import json

INFURA_PROJECT_SECRET = "03016c3bbdb5494f962fcd2d8ac441f1"
INFURA_PROJECT_ID = "m4p+cbnlUMLYT4ah/MzfUj0V79ImrMKAezPKNWBewy1RjjerfgQZfQ"

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	# convert python dictionary to JSON
	json_data = json.dumps(data)

	# upload JSON data to IPFS
	response = requests.post(
        'https://ipfs.infura.io:5001/api/v0/add',
        files={"file": json_data},
        auth=(INFURA_PROJECT_ID, INFURA_PROJECT_SECRET)
    )
		
	# check success
	#if response.status_code == 200:
	result = response.json()
	cid = result["Hash"]
	return cid
	#else:
	#	raise Exception(f"Failed to pin data to IPFS: {response.text}")


def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	parms = (
        ('arg',cid),
    )
	url = f"https://ipfs.infura.io:5001/api/v0/cat"
	
	response = requests.post(
        url,params=parms,
        auth=(INFURA_PROJECT_ID, INFURA_PROJECT_SECRET)
    )

#	if response.status_code == 200:
	data = json.loads(response.text)
	assert isinstance(data, dict), f"Error: get_from_ipfs should return a dictionary"
	return data
#	else:
#		raise Exception(f"Failed to fetch data from IPFS: {response.text}")

# test
