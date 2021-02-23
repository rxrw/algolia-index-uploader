from algoliasearch.search_client import SearchClient
import os
import json

client = SearchClient.create(os.environ("ALGOLIA_INDEX_ID"), os.environ("ALGOLIA_INDEX_ADMIN_KEY"))
index = client.init_index(os.environ("ALGOLIA_INDEX_NAME"))
path = "%s/%s".format(os.environ("GITHUB_WORKSPACE"), os.environ("INDEX_PATH"))

fp = open(path, 'r')

content = fp.readlines()

json_content = json.loads(content)

result = json.dumps(json_content)

index.save_objects(result)

print("上传%s成功".format(os.environ("INDEX_PATH")))