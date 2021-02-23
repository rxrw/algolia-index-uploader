from algoliasearch.search_client import SearchClient
import os
import json

client = SearchClient.create(os.environ.get("ALGOLIA_INDEX_ID"), os.environ.get("ALGOLIA_INDEX_ADMIN_KEY"))
index = client.init_index(os.environ.get("ALGOLIA_INDEX_NAME"))
path = "{}/{}".format(os.environ.get("GITHUB_WORKSPACE"), os.environ.get("INDEX_PATH"))

with open(path, 'r') as f:
  content = f.read()

data = json.loads(content)

index.save_objects(data)

print("上传{}成功".format(os.environ.get("INDEX_PATH")))