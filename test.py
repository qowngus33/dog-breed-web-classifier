import requests

image = open('puppy.jpg', 'rb')

files = {
    'image': image,
}

res = requests.post('http://127.0.0.1:5000/predict', files=files)

print(res.content)
