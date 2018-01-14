# Simple python script to screenshot a website
This script will screenshot a website using python / selenium
You'll need google chrome headless for this to work
All python requirements are in `requirements.txt`

You also need the googlewebdriver from here https://chromedriver.storage.googleapis.com/index.html?path=2.35/ 
Place it somewhere in $PATH so python can access it
also you need chrome

```
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - 
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
sudo apt-get update
sudo apt-get install google-chrome-stable
```

`pip install -r requirements.txt`

just run the script with 
`python main.py`

