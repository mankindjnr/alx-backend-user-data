# PERSONAL DATA
## ==================================================
## LOGGING LEVELS

There are 5 logging levels:
### 1. DEBUG
Detailed information, typically of interest only when diagnosing problems.

### 2. INFO
Confirmation that things are working as expected.

### 3. WARNING
An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

### 4. ERROR
Due to a more serious problem, the software has not been able to perform some function.

### 5. CRITICAL
A serious error, indicating that the program itself may be unable to continue running.

### logging.debug()
By default, the logging level is set to warning. Hence its only going to display warnings or higher, due to this, if your code runs correctly,nothing is displaye to the console. To change the logging level, use the following command in the code:
```python
logging.basicConfig(level=logging.DEBUG)
```
This displays in the console but if you want to write to a log file instead, use the following command:
```python
logging.basicConfig(filename="test.log", level=logging.DEBUG)
```
You can also change the format of the log file using the following command:
```python
logging.basicConfig(filename="test.log", level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
```

## Logging the value of variables
```python
x = 10
logging.info("x is {}".format(x))
```

## Logging exceptions - traceback
```python
try:
    a = 5/0
except Exception as e:
    logging.error("Exception occurred", exc_info=True)
    # or logging.exception("Exception occurred")
```

### -------------------------------------------------------------
## CUSTOM LOGGING
```python
import logging

# createa logger file with the module name
logger = logging.getLogger(__name__)
logger.info("Hello from logger")

# create a handler
# handlers allow us to handle the logs in different ways
handler = logging.StreamHandler('test.log')
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("Hello from handled logger")
```
