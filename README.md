# jsonapi

# Description
I extended JSONEncoder and JSONDecoder to support serialize and deserialize complex and range in python.

# How to set up
1. Unzip the .tar.gz file.
2. Change to directory that contains setup.py.
3. Run the following code
    python setup.py build
    python setup.py install

# Example
```Python
import json
import jsonapi
c = complex(1,1)
c_json = json.dumps(c,cls=jsonapi.MyEncoder)
c_dejson = json.loads(c_json,cls=jsonapi.MyDecoder)

r = range(1,10,2)
r_json = json.dumps(r,cls=json.api.MyEncoder)
r_dejson = json.loads(r_json,cls=jsonapi.MyDecoder)
```