# The-Advanced-Summarizer
## Overview
Currently, there are vast quantities of textual data available, including online documents, articles, news, and reviews that contain long strings of text that need to be summarised. The importance of text summarisation is due to several reasons, including the retrieval of significant information from a long text within a short period, easy and rapid loading of the most important information, and resolution of the problems associated with the criteria needed for summary evaluation.

In order to get the better of the problem, we have come up with a solution using software to summarise our video or text. It contains three parts; first one is to summarise the YouTube video and the next one is to summarise the text article and last one is to summarise any text.

## Block Diagram
![](/images/blockdiagram.jpeg)

## Methodology

- If the input is a link to a YouTube video, the software will automatically extract the transcript of the video using **YouTube API** and then summarise it.
- If the input is a link to a text article, the software will automatically extract the text using **Web Scrapping** and then summarise it.
- If the input is a text, the software will directly summarise it.
- The algorithm that is used to summarise the text is **TF-IDF**.
- The complete backend has been developed using **Django**.

## Interface
The outcome of this project are two main tools - A chrome extension and a website - both are eligible for summarising the input. The input can either be a link of YouTube video or long text-based article or just a text input.

* ### Website
    It contains three inputs:
    
    * Link to any YouTube video or text-based article
    * Text input
    * Target length of the summary

    ### **Link to the website**: [The-Advanced-Summarizer](https://miniproject-b05.netlify.app/)

    Screenshot of the website: 

    ![Interface](/images/web1.png)

* ### Chrome Extension
    Screenshot of the chrome extension: 

    ![Extension](/images/extension.jpg)

    ![Extension](/images/extension2.png)


## Tools Used
* Python programming Language
* Django (backend)
* HTML
* CSS
* NLP 
* API
* Netlify
* Heroku


## Results
The results of the project are as follows:

![Results](/images/web2.png)


![Extension](/images/extension.jpg)


![Results](/images/extension2.png)

## Team

Link to the team page: [Team](https://miniproject-b05.netlify.app/team/)

## Contact
If you have any questions, please feel free to contact me at: 
[Email](mailto:mayank9404@gmail.com) [LinkedIn](https://www.linkedin.com/in/mayank9404/)