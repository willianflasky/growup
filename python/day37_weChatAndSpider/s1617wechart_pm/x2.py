data = {
    'name':'alex',
    'msg':'a阿斯蒂芬'
}

import json

print(json.dumps(data))
print(json.dumps(data,ensure_ascii=False))