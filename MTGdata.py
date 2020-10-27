import requests
import json
import pyspark as ps
import pandas as pd

url = "https://api.tcgplayer.com/pricing/group/2648"

headers = {"Authorization":"bearer HCQV6QHDJtoSNRwb_NyrsQXjcA4SLIxw0c-dnk6wmv4R8HWjJiqxAADaeQemGRzLdgs6k9AW4FQ0gLA8hu7LWlQP5ggOVTKPTUwf-qxJiQJMj9G7dgqE0vhkrjIJlZVN5atLv_2IjHwVr1k90hRInE-NqXb8_hZJDIWCf2iiUm7ZdyBvFntTWrWgFGgTL113Da6dC3_1D38xulQtvbCKdlCaag2orwT3Hb3WnSYnaIhyA0EzB5LtkLNQpEoR4t1RyE-dQ-WIfksapyfaoKFXBkXnB9NnliPzDs7Hxk-xx1Jnznn3wr5EyXuZcyInuzq_cl846Q","Accept": "application/json"}

response = requests.request("GET", url, headers=headers)
data = response.json()
data = data['results']
df = pd.DataFrame.from_dict(data)
print(df)
# file = open("zendikar_rising.txt", "w")
# file.write(response.text)
# file.close()