# Em's Tik Tok Projects lol

Are you here from Tik Tok?
**PLEASE** read this before jumping in!

The files in this repo are light-hearted and casually made in my free time. If you're interested in making any changes, feel free to DM me and make a pull request.

The code presented here in this repository is made with good intentions and for recreational fun, it is not meant to:
1. Be used against others.
2. Be used to exploit others.
3. Be used to illicit dangerous, harmful, or destructive behavior in any manner.

Basically, lets have fun and be a good people :)
To read more about ethical dependencies, check out Wampum.codes' article on using indigenous wisdom in software development and design
[here](https://foundation.mozilla.org/en/blog/indigenous-wisdom-model-software-design-and-development/)


## Hinge Analysis

So you wanna learn more about about your Hinge habits? Look no further!

To request your data, follow the steps [here on Hinge's site](https://hingeapp.zendesk.com/hc/en-us/articles/360011235813-How-do-I-request-a-copy-of-my-personal-data-)

If you do not have a background in programming and would like to plug your data and go, *a website for that is coming soon!*

If you're interested in running this python script yourself, continue reading.

### Prerequisites

Before running, make sure you've got [Python](https://www.python.org/downloads/) set up in your development environment.

### Installation
```
# Option 1: Copy paste the contents of lib/analyze.py into a python file located in the same directory as your Hinge matches.json file

# Option 2: Cloning the repository
$ git clone git://github.com/emam97/tiktok.git
```

### Usage
```
python analyze.py matches.json

```

### Examples
Given your python file is `analyze.py` and the file you received from Hinge is `matches.json` in the directory 
`C:/User/em/hinge_data`
```
$ C:/User/em/hinge_data> python analyze.py matches.json
Parsing data...
Analysis complete!

You've interacted with 100 people on Hinge

Total shots you've shot: 45 (you sent a like)
Total slam dunks: 61 (you've matched with someone or they've matched with you)
Total people you've blessed with your time: 41 (you sent a message at least once)
-------------


Fun Stuff ~

You've rejected 39 people (ouch)
You match with 61% of profiles you see on Hinge.

You've ghosted at least 20 people, or at least 30% of all the people you match.
Total you've dropped the ball: 10 (you sent a like and they matched, no chatting)
Total they've dropped the ball: 10 (they sent a like and you matched, no chatting)

Total shots they've shot and scored: 31 (they sent a like and you matched)
Total shots you've shot and scored: 30 (you sent a like and they matched)
```


