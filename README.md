
# Python version: 3.8.8

## Table of Contents
1. [ Project Description. ](#desc)
2. [ Development Setup ](#setup)
3. [ Installation Setup ](#installation)

<a name="desc"></a>
# Fiverr Gigs Promotion Twitter Bot

The project explored the capabilities of the Twitter API to automate my business promotion process. The bot is scheduled to post gig links with twitter trending topics . Particularly consumed the API to  periodically search and tweet top trending topics in the USA and the UK, alongside the link to my services and order page. The bot helps to generate traffic to my fiverr profile and in turn converts more sales.
Here is a link to the twiter bot account: https://twitter.com/HelenGraph Also below is the image of a sample tweet made by the bot:
![Fiverr Gig Promotion Twitter Bot, Data Analysis, Data Scraping, Web Scraping, Machine Learning, Data Science](https://user-images.githubusercontent.com/58152694/179152062-be45103b-df98-4ed7-9a42-bcfdfc4789d4.png)



This project should serve as a case study for other freelancers wanting to automate their business promotion. 


<a name="setup"></a>

# Development Setup
To run this system, you must have python installed on your computer.
The dependencies and third party libraries of this program are written in the `requirement.txt` file available in the source folder and the third party libraries include:
* `tweepy==4.10.0`

Other dependencies include:
* `time`
* `configParser`

which are readily available with python.

The program file initially included the `myPromoter.py` script and other necesaary files needed for deployment.

To install the required dependencies once, follow the following procedures:

1. On the cmd/terminal, enter the following command to navigate to the application folder:
```bash
$/> cd <your_path>/<application_folder>
```


2. Then, install dependencies

OS X & Linux:
```bash
$ pip3 install -r requirements.txt
```
Windows:
```bash
> pip install -r requirements.txt
```

<a name="installation"></a>
# Installation
Do the following to run the program:

1. Open terminal and ensure the working directory is set to the application folder

OS X & Linux:

```bash
$ <your_path>/<application_folder>
```

Windows:

```bash
> <your_path>/<application_folder>
```
2. Then run the module "myPromoter.py" to enjoy this program.
```bash
$/> python myPromoter.py
```
