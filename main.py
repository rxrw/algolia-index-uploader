from algoliasearch.search_client import SearchClient
import os
import json

client = SearchClient.create(os.environ.get("ALGOLIA_INDEX_ID"), os.environ.get("ALGOLIA_INDEX_ADMIN_KEY"))
index = client.init_index(os.environ.get("ALGOLIA_INDEX_NAME"))
path = "{}/{}".format(os.environ.get("GITHUB_WORKSPACE"), os.environ.get("INDEX_PATH"))

fp = open(path, 'r')

content = fp.readlines()

result = json.loads(content)

index.save_objects(result)

print("上传{}成功".format(os.environ.get("INDEX_PATH")))