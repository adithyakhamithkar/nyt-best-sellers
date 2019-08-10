### Install virtualenv
```
pip install virtualenv
```
### Initilise
```
virtualenv -p /usr/bin/python2.7 apienv
```
### Active
```
source apienv/bin/activate
```
### Install
```
pip install -r req.txt
```

### Start app
```
export NY_API_KEY=xxxxxx
python api/app.py
```

### Deactivate
```
deactivate
```
