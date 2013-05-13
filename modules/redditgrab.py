#!/usr/bin/env python
"""
redditgrab.py - Get specified number of images from specified subreddit
Author: uncurlhalo <jmelton116@gmail.com>
"""

import praw, random, sys

agent = ("RedditURL Grab Phenny IRC module 0.1 by /u/Uncurlhalo")
r = praw.Reddit(user_agent=agent)

def redditgrab(phenny, input):
	subreddit = input.group(2)
	retrieved_list = list()
	
	submissions = r.get_subreddit(subreddit).get_hot(limit=50)
	
	for submission in submissions:
		retrieved_list.append(submission.url + "  (" + submission.title + ")")
		
	if input.group(3):
		num = int(input.group(3))
		#select a random set
		if num > 10 or num <= 0:
			phenny.say("SHUTUP FATASS!")
		else:
			selected = random.sample(retrieved_list, num)
			if len(retrieved_list) == 0:
				phenny.say("[Reddit] Nothing found for \"%s\" :(" % subreddit)
			for item in selected:
				message = item
				phenny.say(message)
	else:
		selected = random.sample(retrieved_list, 1)
		for item in selected:
			message = item
			phenny.say(message)
	
redditgrab.rule = r'(^r\/([a-zA-Z-_]+)(\s(\d){0,2})?)'

if __name__ == "__main__":
    print(__doc__.strip())
