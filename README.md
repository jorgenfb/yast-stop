# yast-stop
Command line utility to stop running time records in Yast

## Setup
1. clone this repo: ```git clone git@github.com:jorgenfb/yast-stop.git```
2. Initialize yastlibs submodule: ```cd yast-stop && git submodule update --init --recursive yastlibs```

## Usage
Run ```yast-stop.py```, specifying your username / email and either your password or previously generated token

Example 1: 
```
./yast-stop.py -u yourusername -p yourpassword
```

Example 2: 
```
./yast-stop.py -yourusername -x yourtoken
```
