# Assignment_2

## Interpretor setup

### Step 1: Build docker image

```
docker build -t assignment_2:latest .
```

### Step 2.1: Set interpretor in Pycharm
Select the docker interpretor in Pycharm named assignment_2:latest

### Step 2.2: Launch script from container
To run the script from a container (an instance of the image assignment_2:latest), run the container like this :
```
docker run -ti -v "$PWD:/w" -w /w assignment_2:latest /bin/bash
```
Then the ```*main.py``` can be ran with the command :
```
python main.py
```