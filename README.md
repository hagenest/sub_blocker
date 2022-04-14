# sub blocker

This python script blocks users who are active in a subreddit. Great if you're part of a community who has a vocal and annoying sub-community :)

## install dependecies
```
praw, python-dotenv (dunno exact name?)
```
## create .env file like this
```
# API-Keys from reddit
CLIENT_ID=
CLIENT_SECRET=
# duh
USERNAME=
PASSWORD=
# reddit wants a descriptive user-agent
USER_AGENT=automatic user blocker /u/$username
# subreddits to block, seperated by ","
SUBREDDITS=cryptocurrency,genzedong
```
## run sub_blocker.py
^
## Caveats
- Bot is very slow, but that's because of the reddit API, no chance to change that
- Bot is buggy af
- Further configuration has to be made in code
- I don't recommend going back further than a week
