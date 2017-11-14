import json

city = {"中国": {"上海": "123"},"美国": {"纽约": "456"},}

with open('a.txt', 'w') as f:
    f.write(json.dumps(city,ensure_ascii=False))
