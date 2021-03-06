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

The following results were obtained on 2018-02-09, the application had no cache:

#### Fizzbuzz
| Threads | Connections | 50%(ms)  | 75%(ms)  | 90%(ms)  | 99.99%(ms) | Avg(ms)  | Req/s | Timeouts | Date |
| :---:   | :---:       | :-----:  | :-----:  | :------: | :-------:  | :------: | :---: | :------: | :--: |
| 1 | 1 | 1.24 | 1.34 | 1.58 | 276.79 | 2.28 | 246.83 | 0 | 2018-02-09_16:00:24  |
| 1 | 25 | 79.75 | 104.48 | 128.84 | 667.34 | 96.51 | 239.66 | 24 | 2018-02-09_16:01:24 |
| 1 | 50 | 167.99 | 218.32 | 332.12 | 1726.87 | 216.72 | 224.98 | 49 | 2018-02-09_16:02:24 |
| 20 | 400 | 500.07 | 681.80 | 820.38 | 1988.12 | 569.54 | 209.62 | 7 | 2018-02-09_16:03:24 |

#### Clock Angle
| Threads | Connections | 50%(ms)  | 75%(ms)  | 90%(ms)  | 99.99%(ms) | Avg(ms)  | Req/s | Timeouts | Date |
| :---:   | :---:       | :-----:  | :-----:  | :------: | :-------:  | :------: | :---: | :------: | :--: |
| 1  | 1 | 1.25     | 1.36     | 1.96     | 286.50    | 8.30     | 222.76 | 0        | 2018-02-09_16:04:24 |
| 1  | 25 | 84.76    | 91.22    | 254.77   | 636.45    | 116.55   | 224.67 | 24       | 2018-02-09_16:05:24 |
| 1  | 50 | 176.68   | 204.00   | 429.11   | 1993.28   | 230.24   | 221.95 | 27       | 2018-02-09_16:06:24 |
| 20 | 400 | 501.86 | 621.89   | 735.65   | 1287.45   | 529.36   | 208.15 | 235      | 2018-02-09_16:07:24 |

The following results were obtained on 2018-02-15, the application had application level cache:

#### Fizzbuzz
| Threads | Connections | 50%(ms)  | 75%(ms)  | 90%(ms)  | 99.99%(ms) | Avg(ms)  | Req/s | Timeouts | Date |
| :---:   | :---:       | :-----:  | :-----:  | :------: | :-------:  | :------: | :---: | :------: | :--: |
| 1 | 1 | 1.22 | 1.30 | 1.59 | 133.87 | 1.66 | 212.12 | 0 | 2018-02-15_16:06:38 |
| 1 | 25 | 86.32 | 98.16 | 258.07 | 1861.16 | 140.23 | 223.47 | 24 | 2018-02-15_16:07:38 |
| 1 | 50 | 184.38 | 215.10 | 309.44 | 1044.51 | 215.13 | 210.09 | 99 | 2018-02-15_16:08:38 |
| 20 | 400 | 492.29 | 643.92 | 743.56 | 1119.57 | 539.02 | 221.21 | 128 | 2018-02-15_16:09:40 |

#### Clock Angle
| Threads | Connections | 50%(ms)  | 75%(ms)  | 90%(ms)  | 99.99%(ms) | Avg(ms)  | Req/s | Timeouts | Date |
| :---:   | :---:       | :-----:  | :-----:  | :------: | :-------:  | :------: | :---: | :------: | :--: |
| 1       | 1           | 1.25 | 1.34 | 1.69 | 297.37 | 5.75 | 195.84 | 0 | 2018-02-15_16:10:40 |
| 1       | 25          | 83.66 | 101.44 | 273.02 | 1857.92 | 135.58 | 237.06 | 0 | 2018-02-15_16:11:40 |
| 1       | 50          | 179.15 | 205.07 | 464.49 | 1108.65 | 226.73 | 214.00 | 33 | 2018-02-15_16:12:40 |
| 20      | 400         | 501.11 | 653.40 | 763.46 | 1985.94 | 554.31 | 220.39 | 38 | 2018-02-15_16:13:40 |

The following results were obtained on 2018-03-16, the application had web-server level proxy (Nginx with 1024 workers):

#### Fizzbuzz
| Threads | Connections | 50%(ms)  | 75%(ms)  | 90%(ms)  | 99.99%(ms) | Avg(ms)  | Req/s | Timeouts | Date |
| :---:   | :---:       | :-----:  | :-----:  | :------: | :-------:  | :------: | :---: | :------: | :--: |
| 1 | 1 | 0.12 | 0.12 | 0.13 | 26.88 | 0.28 | 7523.15 | 0 | 2018-03-16_18:40:05 |
| 1 | 25 | 2.79 | 3.01 | 3.54 | 38.44 | 3.38 | 8189.21 | 0 | 2018-03-16_18:41:05 |
| 1 | 50 | 5.74 | 5.97 | 6.79 | 80.15 | 6.39 | 8240.62 | 0 | 2018-03-16_18:42:05 |
| 20 | 400 | 28.12 | 28.83 | 30.79 | 604.41 | 30.47 | 8132.00 | 0 | 2018-03-16_18:43:05 |


#### Clock Angle
| Threads | Connections | 50%(ms)  | 75%(ms)  | 90%(ms)  | 99.99%(ms) | Avg(ms)  | Req/s | Timeouts | Date |
| :---:   | :---:       | :-----:  | :-----:  | :------: | :-------:  | :------: | :---: | :------: | :--: |
| 1 | 1 | 0.12 | 0.12 | 0.13 | 57.55 | 0.53 | 7331.00 | 0 | 2018-03-16_18:44:05 |
| 1 | 25 | 2.89 | 3.13 | 3.68 | 239.07 | 3.96 | 7948.87 | 0 | 2018-03-16_18:45:05 |
| 1 | 50 | 5.77 | 5.99 | 6.73 | 177.65 | 6.54 | 8167.07 | 0 | 2018-03-16_18:46:05 |
| 20 | 400 | 28.16 | 28.79 | 31.03 | 621.76 | 30.55 | 8147.87 | 0 | 2018-03-16_18:47:05 |
