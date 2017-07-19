# keepasshttplib

![build status](https://travis-ci.org/02TPr1804/keepasshttplib.svg?branch=master)

## What is keepasshttplib?
keepashttplib is a python library that can interact with [keepasshttp](https://github.com/pfn/keepasshttp)

Currently, this library only supports get-login. Other operations will be supported in the future
## Usage

```python
from keepasshttplib import keepasshttplib
k = keepasshttplib.Keepasshttplib()
k.get_credentials("http://dsms.fasthosts.co.uk")
```