#!/usr/bin/env python
import twitter

USERNAME = "wenwu"
PASSWD = "CBAnbaWW"

def main():
    api = twitter.Api(username=USERNAME, password=PASSWD)
    followers = api.GetFollowers()
    print [f.name for f in followers]
if __name__ == '__main__':
  main()
