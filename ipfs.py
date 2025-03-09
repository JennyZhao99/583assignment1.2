import requests
import json

INFURA_API_KEY = "03016c3bbdb5494f962fcd2d8ac441f1"

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	# convert python dictionary to JSON
	json_data = json.dumps(data)

    # Infura 的 IPFS API 端点
	url = "https://ipfs.infura.io:5001/api/v0/add"

    # 请求头中添加 Authorization
	headers = {
        "Authorization": f"Bearer {INFURA_API_KEY}"
    }

    # 使用 requests 库将 JSON 数据上传到 IPFS
	response = requests.post(
        url,
        files={"file": json_data},  # 将 JSON 数据作为文件上传
        headers=headers  # 添加 Authorization 头
    )

    # 检查请求是否成功
	if response.status_code == 200:
        # 解析返回的 JSON，获取 CID
		result = response.json()
		cid = result["Hash"]
		return cid
	else:
		raise Exception(f"Failed to pin data to IPFS: {response.text}")


def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	

	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
