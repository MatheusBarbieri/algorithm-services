# Algorithm Services [![Build Status](https://travis-ci.org/MatheusBarbieri/algorithm-services.svg?branch=master)](https://travis-ci.org/MatheusBarbieri/algorithm-services)

> This is a web server that permits the execution of algorithms.

### Installation
- Requirements: Python 3.6.2

There is a Makefile in the project folder which has set up rules for installing, running and testing this application.

To begin installation, in the root directory of the project call ```make setup```

### Basic usage
After installation, run the application by calling ```make run``` on the project directory, then you will be able to acess the webserver.
- Syntax: `<server domain>/<algorithm (lower case)>/<inputs>`
- Example: `localhost:8888/fizzbuzz/100`


### Available algorithms
| Algorithm | Short Description | Input | Output |
| ----------|:------------|:-----:| :-------:|
| Fizzbuzz  | This algorithm takes an input integer and outputs a list in that range in which every element divisible by 3 is substituted by the word **Fizz**, every element divisable by 5 is substituted by the word **buzz** and elements divisble by both numbers are substituted by **Fizzbuzz**.| Any integer | List of objects(numbers and strings)|
| Clock_Angle | Clock Angle calculates the smaller angle between the hands (hour and minutes) of a clock on a given time | Integers: hours; minutes; seconds (optional) | Float: Angle |

### Tests
Tests can be run by calling ```make test``` in the root director.

### Benchmark
The results bellow were received with MacBook Pro 2011, CPU: 2.3 GHz i5, MEM 16GB, OSX 10.13.3 using WRK utility. Each test ran for 60 seconds.

#### Fizzbuzz
| 1 | 1 | 1.22 | 1.30 | 1.59 | 133.87 | 1.66 | 212.12 | 0 | 2018-02-15_16:06:38 |
| 1 | 25 | 86.32 | 98.16 | 258.07 | 1861.16 | 140.23 | 223.47 | 24 | 2018-02-15_16:07:38 |
| 1 | 50 | 184.38 | 215.10 | 309.44 | 1044.51 | 215.13 | 210.09 | 99 | 2018-02-15_16:08:38 |
| 20 | 400 | 492.29 | 643.92 | 743.56 | 1119.57 | 539.02 | 221.21 | 128 | 2018-02-15_16:09:40 |

#### Clock Angle
| 1       | 1           | 1.25 | 1.34 | 1.69 | 297.37 | 5.75 | 195.84 | 0 | 2018-02-15_16:10:40 |
| 1       | 25          | 83.66 | 101.44 | 273.02 | 1857.92 | 135.58 | 237.06 | 0 | 2018-02-15_16:11:40 |
| 1       | 50          | 179.15 | 205.07 | 464.49 | 1108.65 | 226.73 | 214.00 | 33 | 2018-02-15_16:12:40 |
| 20      | 400         | 501.11 | 653.40 | 763.46 | 1985.94 | 554.31 | 220.39 | 38 | 2018-02-15_16:13:40 |
