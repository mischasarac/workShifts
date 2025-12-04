# SkyCity Work Shifts

### Project Outline

I started this project when I first started working at the Adelaide Casino because I realised how absolutely horrific the timesheet scheduler was. Shifts also constantly get moved and updated so I wanted some python script to make all these adjustments in my google calendar so I didn't have to bare looking at the web design that was older than me.

### Using The Code

Unfortunately I wouldn't say this is my best-designed python code, so to use it you will need some programming experience. The biggest thing is knowing how to set up your google API. 

Unfortunately I wouldn't say I'm the biggest help in that regard, but to set everything up just follow the steps at https://developers.google.com/workspace/calendar/api/quickstart/python and save your credentials.json into this repo.

For *package installation* you can simply use the following

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -m requirements.txt
```

This should set you up with everything you need to start running the code.
To do this, run:
```bash
python3 -m main
```
You will get prompted to input some information about your work login, and once that is done the rest should be handled by itself.

*Good luck to the 3 people at SkyCity who know how to code!*