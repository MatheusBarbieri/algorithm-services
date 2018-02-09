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
| Threads | Connections | 50%(ms)  | 75%(ms)  | 90%(ms)  | 99.99%(ms) | Avg(ms)   | Req/s | Timeouts | Date |
| :---:   | :---:       | :-----:  | :-----:  | :------: | :-------:  | :------:  | :---: | :------: | :--: |
| 1 | 1 | 1.24 | 1.34 | 1.58 | 276.79 | 2285.22 | 246.83 | 0 | 2018-02-09_16:00:24 |
| 1 | 25 | 79.75 | 104.48 | 128.84 | 667.34 | 96515.42 | 239.66 | 24 | 2018-02-09_16:01:24 |
| 1 | 50 | 167.99 | 218.32 | 332.12 | 1726.87 | 216729.22 | 224.98 | 49 | 2018-02-09_16:02:24 |
| 20 | 400 | 500.07 | 681.80 | 820.38 | 1988.12 | 569543.22 | 209.62 | 7 | 2018-02-09_16:03:24 |

#### Clock Angle
| Threads | Connections | 50%(ms)  | 75%(ms)  | 90%(ms)  | 99%(ms)   | Avg(ms)  | Req/s  | Timeouts |
| :---:   | :---------: | :-----:  | :-----:  | :------: | :-------: | :------: | :----: | :------: |
| 1 | 1 | 1.25 | 1.36 | 1.96 | 286.50 | 8308.49 | 222.76 | 0 | 2018-02-09_16:04:24 |
| 1 | 25 | 84.76 | 91.22 | 254.77 | 636.45 | 116556.43 | 224.67 | 24 | 2018-02-09_16:05:24 |
| 1 | 50 | 176.68 | 204.00 | 429.11 | 1993.28 | 230246.71 | 221.95 | 27 | 2018-02-09_16:06:24 |
| 20 | 400 | 501.86 | 621.89 | 735.65 | 1287.45 | 529368.65 | 208.15 | 235 | 2018-02-09_16:07:24 |
