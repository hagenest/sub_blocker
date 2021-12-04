import praw
import os
from dotenv import load_dotenv


load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    username=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD"),
    user_agent=os.getenv("USER_AGENT"),
)

subList = os.getenv("SUBREDDITS").split(",")

def getSubmissions(sub):
    """returns all submissions to a sub in the last year"""
    submissions = []
    for submission in list(reddit.subreddit(sub).top("week", limit=None)):
        submissions.append(submission)
    return submissions

def getSubmissionAuthors(submissions):
    authors = []
    for submission in submissions:
        authors.append(submission.author.name)
    return authors

def getComments(sub):
    """
    Returns a list of every comment on the specified subreddit in the last year
    """
    comments = []
    for submission in list(reddit.subreddit(sub).top("week", limit=None)):
        for comment in list(submission.comments):
            comments.append(comment)
    return comments

def getAuthors(comments):
    authors = []
    for comment in comments:
        if comment.author != None:
            authors.append(comment.author.name)
    return authors

    
def countOccurences(list):
    """
    Returns a dictionary with the number of occurences of each user
    """
    occurences = {}
    for user in list:
        if user in occurences:
            occurences[user] += 1
        else:
            occurences[user] = 1
    return occurences

def dropUsers(dict, x):
    """
    Remove all entries from dict who have less then x occurences
    """
    for key in list(dict.keys()):
        if dict[key] < x:
            del dict[key]
    return dict
        
def convertToList(dict):
    """
    Returns a list with only the keys of the dictionary
    """
    return list(dict.keys())

def blockUsers(list):
    """
    Blocks all users in the list
    """
    for user in list:
        blocked = []
        for entry in reddit.user.blocked():
            blocked.append(entry.name)
        if user not in blocked:
            reddit.redditor(user).block()

def subBlocker(subList):
    for sub in subList:
        activeUsers = getAuthors(getComments(sub))
        activeUsers = countOccurences(activeUsers)
        activeUsers = dropUsers(activeUsers, 5)
        activeUsers = convertToList(activeUsers)
        blockUsers(activeUsers)
        print(activeUsers)

def subBlocker2(subList):
    for sub in subList:
        users = getSubmissionAuthors(getSubmissions(sub))
        #users = countOccurences(users)
        #users = dropUsers(users, 5)
        #users = convertToList(users)
        blockUsers(users)
        print(users)



def unblockAll():
    """Unblocks every blocked reddit user"""
    for user in reddit.user.blocked():
        user.unblock()

if __name__ == "__main__":
    #unblockAll()
    subBlocker2(subList)
    #print(getAuthors(getComments("asktankies")))