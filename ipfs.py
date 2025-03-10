import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	# convert python dictionary to JSON
	json_data = json.dumps(data)

	# upload JSON data to IPFS
	
	url =   'https://api.pinata.cloud/pinning/pinJSONToIPFS'
	api = '7c9704e12c4f7db849aa'
	sk = '09258d8b4c0a1597a6e67493118b416bf40950f7e451e97a336530e4f80e80e6'
    
	headers = {"Content-Type": "application/json", 
			"pinata_api_key": api,
			"pinata_secret_key": sk}
	# check success
	#if response.status_code == 200:
	result = requests.post(url,headers=headers, data = json_data)
	cid = result.json().get("IpfsHash",None)
	return cid
	#else:
	#	raise Exception(f"Failed to pin data to IPFS: {response.text}")


def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	parms = (
        ('arg',cid),
    )
	url = f"https://gateway.pinata.cloud/ipfs/{cid}"
	
	response = requests.post(
        url,params=parms,
        auth=('7c9704e12c4f7db849aa', '09258d8b4c0a1597a6e67493118b416bf40950f7e451e97a336530e4f80e80e6')
    )

#	if response.status_code == 200:
	data = json.loads(response.text)
	assert isinstance(data, dict), f"Error: get_from_ipfs should return a dictionary"
	return data
#	else:
#		raise Exception(f"Failed to fetch data from IPFS: {response.text}")

# test
