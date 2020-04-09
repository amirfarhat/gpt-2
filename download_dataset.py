import os
import requests

file_name = "shakespeare.txt"
if not os.path.isfile(file_name):
    url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
    data = requests.get(url)		
    with open(file_name, 'w') as f:
        f.write(data.text)
