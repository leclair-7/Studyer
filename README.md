###Studyer Readme

##Since I'm in school, this is an app to help me study "more effectively" which is another way of saying "less".

##The documentation is for my friends to read and for me to use.
==============================================================================================================
#Since this project is for a good time with a focus on good, the documentation at times has an air of irony, a lack of seriousness, etc.

To Do List:
* get on a big screen with a big (visual) debugger to implement those heuristics
* found some participants to evaluate anser heuristics, just need a quiz/tracking backend/etc./etc./etc...
* put on a website
* with web stuff - add pictures - sleek UI
* password and profile on the site
* option for peg100 learning (need another pickle file for the user
* design a better inter session data storage technique [ would a real DB be useful??, nonsense ] 
* module for link technique learning - directions examples and such
* put options if they want to stop studying, save progress and go on
* link the amount of times Student has answered the question with likelihood it is asked 
* unit tests for every function, code coverage
* displaying pictures on django site,

Date timestamp control functions to maybe use:
Below is how to see the timestamp in various ways (this was surprisingly tricky to find/figure out)

    time.asctime( time.localtime(time.time() ) )
    delta.days, delta.seconds, delta.microseconds
    str(timedeltaobject)
    to get elapsed time from datetime, may be the better option
    s = datetime.datetime.now(), t = datetime.datetime.now()
    t-s will be a timedelta object

###Features To Do:
We realize that the time taken for answering a question also includes some 
functions running that are heavy on the computation front, however since it's consistant
improvement of the user's knowledge will still be reflected

###TESTING
unit test modules

###UI
this will be on a Django driven webpage

###QUESTION ANSWER HEURISTICS
find a way to train a model with user data only, maybe that and a combo of aggregate will be better

then presumably...
it'll feel pretty accurate to me the user

###QUIZ
getting close enough to the right answer function
put question answer time in performance,
when the user doesn't get a close answer, have a hint

    ideas for criteria for answer being right:
    quantify by weighing the criteria: sync with one's confidence of mastery of material
    this is how markdown displays code!!!! :) :) :)

## "f it"  - B A
## "I heard that pause" - B A

###REMEMBERING YOUR PAST
* use past quiz sessions for customized future sessions

* Memory 100 peg list helper, make it make crazy associations based on nouns not being on top 10000 english used
but also being syntactically close to current noun and the one associated with the number

* for hints language ambiguity is an issue...