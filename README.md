# Alarmous

**A website to satisfy all your alarm related needs**

[![Website](/screenshots/website.gif)](http://devl.xfstzsazrv.us-east-1.elasticbeanstalk.com/)
**Project for learning Django framework**
**Project Duration - August 2019**
***
Alarmous is a simple website where users can create alarms, and have it ring on the website when the alarm time is up.

## Page Flows
![Architecture Diagram](/screenshots/FlowChart.png)
A high-level overview of the entire website

[AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) was used to deploy the website

## Requirements
* [Python 3.5+](https://www.python.org/downloads/)
* An amazon AWS account - If deploying on BeanStalk (optional)

## Installation
1. Clone the repo by using the following command
``` bash
$ git clone https://github.com/hussu97/alarmous.git
$ cd alarmous
```
2. Install all the packages from requirements.txt
``` bash
$ pip install -r requirements.txt
```
3a. Create a file called secretkey.txt in the main directory, and add a string of characters inside it (Keep it secure)
3b. Alternatively, you can add your key to the environment variables (key = 'secret')
4. Collect all the static files using
``` bash
$ python manage.py collectstatic
``` 
5. Make sure your static files are being hosted on static/, and media files on media/, through your nginx or apache2 configuration (production mode only)
6. Start the django server using
``` bash
$ python manage.py runserver
$ python3 manage.py runserver #Linux
```
7. Go to http://127.0.0.1:8000/ to view the mainpage of the website, if running on localhost


> Note: If using the website with DEBUG = False, you may need to add your host IP Address to the variable ALLOWED_HOSTS in alarms/settings.py, or add it to your environment variables (key = 'host_domain')

## Functions
* Register and Login as an alarmous User
* Add an alarm, giving the alarm a name, time, and choosing a sound from a preset list
* Be greeted with a popup message and an alarm sound of your choice, when your alarm is ready
* Edit the alarm time, or delete it

## Additional Screenshots
###Web Screens
![Landing](/screenshots/landing.jpg)
![Home](/screenshots/home.jpg)
![Popup](/screenshots/popup.jpg)
***
### Mobile Screens
![Home](/screenshots/home_mobile.png)
![Popup](/screenshots/popup_mobile.png)
***
## License
[Apache License 2.0](https://github.com/hussu97/mediCords/blob/master/LICENSE)