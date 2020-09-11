# TripAdvisor comments analyzer

Develop from January 2020 to June 2020 in Madrid, Spain.

## About:

This Python script allow you to extract the comments from a TripAdvisor hotel and perform a sentiment analysis. The user has to insert some parameters for the script to work, first, the main URL of the webpage, second, the full URL of the TripAdvisor hotel that he want to extract the comments from, and finally, the number of pages of comments that the user wants to extract. Then, when the script is run, the program would extract all the comments using web scraping and performing a sentiment analysis in each one of them. The sentiment analysis will output two main values ranging from 1 to -1: Polarity and Subjectivity. The polarity value indicates if the comment is positive or negative, been 1 the most positive and -1 the most negative. The subjectivity value indicates if the is objective or subjective, been 1 completely objective and -1 completely subjective. Finally, all the data is dumped in a csv file containing the polarity value, the subjectivity value and the comment itself.

## Team:

This project was developed by my self during the second semester of my year studing in the Politecnico di Milano, but done remotly from Spain due to Covid19. 

## Development:

First, I studied the TripAdvisor page structure to see how I could extract the comments using web scrapping. During the study I discover that the comments did not fully show up in the hotel page, so I went around it by clicking in each comment before extracting it. Then I searched the HTML code to find what was the best HTML tag to extract the comments. Once I had everything figured out, I Implemented the web scraping algorithm using Python together with the xpath method from the LXML library.

After extracting each comment, I did a sentiment analysis on it using the Text Blob library to extract the polarity and subjectivity of the comment. Then I inserted the comment text, the polarity value and the subjectivity value, each one of them in a separate list, so at the end I could add the three lists to a Data Frame and dump it on a csv file using the Pandas library.


## Languages and tools:

During the development of this project the following lenguages and tools were used:

- <img alt="Python" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"/> Python
- <img alt="Pandas" width="26px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Pandas_mark.svg/1200px-Pandas_mark.svg.png"/> Pandas
- <img alt="LXML" width="26px" src="https://www.rbcafe.es/wp-content/uploads/lxml.png"/> LXML
- <img alt="TextBlob" width="26px" src="https://textblob.readthedocs.io/en/dev/_static/textblob-logo.png"/> TextBlob