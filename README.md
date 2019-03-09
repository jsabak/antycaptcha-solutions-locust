# antycaptcha-solutions-locust
Tests for AntyCAPTCHA implemented with locust

## How to implement tests with locust

### Dependences
* locust
* har-transformer - take har-transformer from my repository, it has urlignore implemented 
with regex instead of ordinary string search [TODO: make a pull request with that changes]
* .urlignore - has many regexes to ignore 

### Steps

1. Record a HAR file with actions you want to test
1. Put HAR files into separate directory 
1. Run transformer to convert HAR files to locustfile.py
1. Refactor locustfile.py, add test data and some assertions

### Directory structure of the tests
```text
/antycaptcha-solution-locust
+-- exercises
+-- stf
+-- listeners
    +-- csv_listener.py
    +-- influx_listener.py
.gitignore
.urlignore
locustfile.py
mainpage.py
LICENSE
README.md
```

Directories *exercises* and *stf* contain classes with tests for particular exercises.
*listeners* folder contains addiditonal listerner to save test data to CSV files or to influxdb. 
*mainpage.py* contains a test loading main Antycaptcha's page. 
*locustfile.py* is a main file using to run locust.

### Running tests

* locust -l - lists all available locusts (workers/threads)
* locust -H <host> - runs locust against a *host*

## Styleguide for writing locust tests for Antycaptcha
1. Use separate *.py files for the exercises
1. Remove protocol and hostname from *url* parameter of *client.get* and *client.put* calls
1. Edit *name* parameter for *client.get* and *client.put* calls, to be readable
1. Remove headers from *client.get* and *client.put* calls, unless you really need them
1. Name classes with steps as *ExerciseXSteps(TaskSequence)*
1. Add iterrupt task at the end of the tasks in task sequence in order to allow other tasks to run
    ```python
    @seq_task(100)  # 100 is a number big enough to be greater than number of steps in most scenarios
    def stop(self):
        self.interrupt()
    ```
1. Import and add the class with task steps in locustfile.py:
    ```python
    # import the steps
    from exercises.exercise1 import Exercise1Steps
    
    class ALTTaskSet(TaskSet):
        tasks = [Exercise1Steps] # insert the steps into the list of steps
    
    class AntycaptchaLoadTest(HttpLocust):
        task_set = LFTaskSet
        min_wait = 4000
        max_wait = 4000
    ```
