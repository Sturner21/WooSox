# WooSox
Compilation of projects created and used during internship with Worcester Red Sox

## suiteInfoAuto
The purpose of suiteInfoAuto was to give the clients who were attending Worcester Red Sox games in suites the necessary documents to take full advantage of the park's amenities.
### Motivation
I was motivated to start this project out of constructive laziness. I was given a list of clients who would be attending games during the week in the suites. I was told that I must email the sales representatives individually with parking passes and "Know Before You Go" sheets. 5 suites would be used on any given night and there were 6 games during a week. Sending out 30 emails that were basically the same was tedious and error prone when done manually. I quickly recognized that Python would be much more efficient at this than I could and it could save me a ton of time. Sending 30 emails by hand took 90 minutes and with this program took 6 minutes. In other words, this program was at least 90% more efficient than I was at emailing.
### Basic Overview
suiteInfoAuto is a fairly simple program at heart. I used the Gmail API because there was more documentation available for it which helped immensely with troubleshooting. This is why there are reference variables and documents in the code that are not included in this repository. Those documents are specific to my google account which I did not want the public to have access to. The program starts with loading in all necessary data for it to construct and email from. Such as, sales representitive's emails, dates of games, which suites would be used, etc. From there the main function of the program, Walking Dog, is created. The name for this came from one of my coworkers who mentioned out of the blue that it would be a good name. I found it so amusing that I kept it. The function starts a loop that will go 5 times, once for every suite that will be used during a game. From there, it deduces which salesperson should get the email. The subject line is "game date - party attending - suite they are in". The body of the message is personalized by discussing the date, suite, and special parking spots given to them for the game. After that, the 3 necessary PDFs are attached to the message, and the message is sent. The program will print the message ID as an indicator that it is working and is not stuck on a problem. The only thing left to do in the program is call the function and tell it which game to send emails for.


I will flush out README after the summer and summarize all projects

I do not intend for others to use this project for themselves. Therefore, I will not be providing an information on how one should install, run, or use the project. However, if anyone would like to use this code as a skeleton for their own project they are more than welcome to.
