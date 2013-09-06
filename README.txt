The purpose of this script is to scrape public tweets for a designated query (query modifiers are found in the twitter api wiki).
The tweets will be collected and stored into a mongoDB on the local machine.
Work in progress...


Twython API must be installed (Twitter REST API)
PyMongo must be installed from the mongoDB website.

This could be better utilized with the twitter streaming API, which is in closed-beta.

client variable specifies the host mongoDB.
If the database 'twitter' does not exist and/or the collection 'tweets' within that database, both/either will be created on first insert.

a registered app key and secret must be punched in (obtained by registering an app on the twitter API)
a registered oauth_token and secret must be punched in for a twitter log-in account.

There is much more to be implemented but this is a working foundation.