# Algorithm Services [![Build Status](https://travis-ci.org/MatheusBarbieri/algorithm-services.svg?branch=master)](https://travis-ci.org/MatheusBarbieri/algorithm-services)

> This is a web server that permits the execution of algorithms.

### Installation
- Requirements: Python 3.6.2

There is a Makefile in the project folder which has set up rules for installing, running and testing this application.

To begin installation, in the root directory of the project call ```make setup```

### Basic usage
After installation, run the application by calling ```make run``` on the project directory, then you will be able to acess the webserver.
- Syntax: <server domain>/<algorithm>/<inputs>
- Example: localhost:8888/fizzbuzz/100


### Avaliable algorithms
| Algorithm | Short Description | Input | Output |
| ----------|:------------|:-----:| :-------:|
| Fizzbuzz  | This algorithm takes an input integer and outputs a list in that range in which every element divisible by 3 is substituted by the word **Fizz**, every element divisable by 5 is substituted by the word **buzz** and elements divisble by both numbers are substituted by **Fizzbuzz**.| Any integer | List of objects(numbers and strings)|

### Tests
Tests can be run by calling ```make tests``` in the root director.
