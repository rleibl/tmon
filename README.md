# tmon
Temperature monitoring project with Raspberry Pi.
This is a toy project for self education.

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
