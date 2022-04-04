# Wordle-Bot

I designed a bot in python to do Wordle using logic

This was my first Python project 

If it has not already been uploaded: Final_Wordle_Bot will be the final file 
I hope it works for you 

To do this task I have been using letter frequency counts and have moved onto counting the frequency of a letter in certain positions

I have then been taking this data to choose the best words to pick, taking input data from the result and filtering the words using the input 

There are 2 functions: 
- Explore looks around for common letter which we do not know about - this is when we do not have enough data to narrow in on a certain guess 
- Complete looks to use the known data to formulate a guess which is most helpful for further info while also hopefully being the correct answer
