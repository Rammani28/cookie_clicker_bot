# Cookie Clicker bot

This bot can play "Cookie clicker" game  all night for you.
It will buy the upgrades on the way and backups your progress on each purchase.

## Requirements
- Your system must have python 3.x installed
- Chrome browser
- Chrome web driver of same version as your Chrome browser [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
- Selenium package installed

## Installation
1. Open terminal and run the following command:
```
$git clone https://github.com/Rammani28/cookie_clicker_bot.git
```
2. change directory 
```
$cd cookie_clicker_bot
```
3. It is recommended to use virtual environment to setup selenium
```
$python -m venv venv  #creates virtual environment named 'venv'
$source venv/bin/activate  #activate current virtual environment named 'venv'
```
4. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install selenium.
```
$ pip install selenium 
```

## Usage
#### Enter the following in the terminal to start the bot.
```
$python3 main.py
```
It should be running now. If not make sure the variable 'PATH' in the main.py is set to your chromedrivr's location.


## Contributing

Pull requests and any suggestions are welcome.



## License

[MIT](https://choosealicense.com/licenses/mit/)

