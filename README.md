## Inspiration
The gaming industry has grown tremendously in the recent past. A recent report released by the Entertainment Software Association (ESA) estimated that 42% of Americans play video games for at least 3 hours every week. Additionally, more than 150 million Americans play online and offline video games. Another forecast by PwC suggested that by 2020, the revenue generated from video games would reach $93.18 billion USD. In addition, the global social gaming market would reach $22.52 billion USD.
- COVID-19 saw video games explode in popularity, as consumers were forced to stay at home and keep themselves entertained.
- In the year to date, $29.4 billion of video games have been sold in the US - a 23% increase from last year.
- Mobile game sales on iPhones rose 44% in Japan and 20% in the European Union in July, according to data from Sensor Tower.
**Through all this we have lost something, it's the fun and communication from in-person events. Our project is aimed to bring that fun alive again in this amidst of times.**
## What it does
When you open the web app you will have two bots, Gaming Arena and Gamer Bot. Gaming Arena will provide you with information about similar types of games using Cohere AI and give you the online version of the fun when you enter `wanna play {game name}`. The second bot is mainly focused on all those people who miss the in-person activities

## How we built it
We build all the generation and recommendation tools using Cohere AI NLP model.
![Model](https://media.discordapp.net/attachments/1007170629188980846/1008307491630759966/prompt-task-description.png)
### GitHub
We used GitHub extensively for PR, issues, Wiki, Actions, hosting, release, and many more.
![Github](https://media.discordapp.net/attachments/1007170629188980846/1008307491932754101/Screenshot_2022-08-14_101256.jpg)

![Github](https://media.discordapp.net/attachments/1007170629188980846/1008307492146655293/Screenshot_2022-08-14_101323.jpg?width=1440&height=516)

![Github](https://media.discordapp.net/attachments/1007170629188980846/1008307492482191380/Screenshot_2022-08-14_122401.jpg?width=1224&height=570)

## Challenges we ran into
While implementing Cohere we had a lot of problems, sometimes the model will generate Chinese characters and other weird characters and it was so hard to spot it but we adjusted the temperature and deleted the white spaces, and fixed it. The other problem was hosting the bots on Heroku since the Heroku hosting sleep after a few minutes our bots will not be able to retrieve the data from the Cohere API so we used colab and hosted it locally. So the only time it will work is if we run the code and if that PC is off the bots will go to sleep.

## Accomplishments that we're proud of
We are so happy to be able to complete this job at the last minute. Even though we immediately started doing it. We procrastinated to the last minute lol.

## What we learned
We learned a lot about using the Python telegram bot API and pyTelegramBotAPI we used both of them with obvious python to implement the two bots. We also learned about tokenization and how Cohere's endpoints work. Besides that, it was the first time for the 3 of the members to try the next and we were so happy to experiment with it. The routings were easy.

## What's next
We would like the users to benefit a lot from the Cohere AI by generating more things and add the classification model to the users to filter out games based on age and other metrics. 

