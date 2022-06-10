import requests


for _ in range(100):
    x = requests.get("http://211.58.102.6:8000/api/inference/2")
    with open("2_{}.jpg".format(_), "wb") as f:
        f.write(x.content)

    x = requests.get("http://211.58.102.6:8000/api/inference/1")
    with open("1_{}.jpg".format(_), "wb") as f:
        f.write(x.content)