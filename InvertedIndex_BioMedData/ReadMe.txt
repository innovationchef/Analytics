Problem Statement : Question Answering System from large volume of medical data.

Note: 
1. The database has been downloaded from “Scopus”. Abstract of Top 2000 research papers based on “cancer” was downloaded as csv file and then this file was parsed to create 2000 text files. 
2. Download the zipfile and go to the folder from the terminal - type “python inverted-index.py 10” to run the code. 10 stands for the number of files you want to use for analysis out of 2000. 
3. The terminal will ask “enter query ----- ”. Enter your question and the code will return the documents relevant to the question. 4. Enter the name of the file you wish to see through the terminal.

Features: 
1. I have not considered stemming of words or semantic analysis. I need time to do that, but I can do that. That will reduce the number of relevant documents significantly. 
2. Normal Spelling mistake will be processed if you commit such mistakes while entering the question. 
3. I have tested the following questions on my code --- 
    is cancer fatal? 
    how many patients die from cancer? 
    how to help cancer patient? 
    how strong is cancer? 
    how to cure cancer? 
    4. I have made a function to rank the documents retrieved on the basis of noun entities and adjectives. But, I need more time to implement and test them rigourously.
