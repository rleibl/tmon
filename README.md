# tmon
Temperature monitoring project with Raspberry Pi.
This is a toy project for self education.

## Server
This is an educational project, so the server is written using the python 3 standard library, instead of using one of the obvious frameworks like django or pyramid.

## Client
```
   client/client.py
```
The client is a single standalone python script using only the python 3 standard library.
This script can be copied to the Raspberry as is.

At the top of the script, there are some settings that are system dependent. These need to be set before running.

After setting these, running the client will collect data and drop it off at the server.

### cron
It probably makes sense to add the script to cron. Simplest way on the Pi is to put a script into /etc/cron.hourly/

Note that the name of the script may not contain a '.', otherwise run-parts() will not run it. Also, it needs to be executable. Remember that the script is run as root.

```
#!/bin/sh
cd /home/pi/tmon/
python3 client.py >> tmon_client.log
```

## Testing
All test files are in the test/ directory and named test\_\*.py

Running
```
python -m unittest
```
Finds and runs all of these tests

## Cron
To regularly check that tmon is running use scripts/cron/checktmon
e.g. add or link it to /etc/cron.hourly/

Note that in case of a failed check, this tries to send an email using
`scripts/send\_tmon\_error.py`. Both files will need to be adjusted.
