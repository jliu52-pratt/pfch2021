#!/usr/bin/env python
# coding: utf-8

# # Info644 Final Project - Videogame Sales

# ## Introduction

# In[1]:


get_ipython().run_cell_magic('HTML', '', '\n<div style="width:100%;height:0;padding-bottom:75%;position:relative;"><iframe src="https://giphy.com/embed/aX0RqLt2ARSW4" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a href="https://giphy.com/gifs/video-games-nintendo-mario-aX0RqLt2ARSW4">via GIPHY</a></p>')


# In 1972, the electrnoic game 'Pong' was released by the American game manufacturer Atari, Inc and took the world by storm. Since then, the video game industry has grown at an exponential rate as the video games global market is forecast to worth $256.97 billion by 2025 (Source: Mordor Intelligence). 
# 
# Video game addiction has also recently been included in the American Psychiatric Association's (APA) Diagnostic and Statistical Manual of Mental Disorders (DSM-5). Though not formally recognized as a mental disorder, APA warned viewers of the dangers of internet gaming as ""gamers" play compulsively, to the exclusion of other interests, and their persistent and recurrent online activity results in clinically significant impairment or distress." The obsession with gaming has only increased as the pandemic has left people cooped indoors.  
# 
# For the purpose of this project and stemming from my own personal interest in video games, I wanted to identify what kind of trends and patterns we can draw from different regions of the world, and see if the data we are seeing matches the forecasted worth in global sales. The dataset I have used is a video games sales dataset from a web scrape of www.vgchartz.com. This dataset contains a list of video games with sales greater than 10,000 copies. Each record includes a breakdown of the video game’s name, rank, platform, year, genre, publisher, and sales (in North America, Europe, Japan, and worldwide). There are 11 fields and over 16,598 records. 
# 
# I used python to create several scripts that can extract different sets of data to see if there are compelling patterns and trends I can draw on from over 16,000 records. Some analyses include looking at global sales and pulling out specific video games and their sale records. I used Tableau to create all my visualizations and embedded them into this jupyter notebook.
# 
# The first python script was used to count the number of videogames sold and look at the top 10 most sold video games. The second python script was used to extract data and looking at the max games sold by region, platforms, and genres. 
# 
# The dataset can be found here: https://github.com/GregorUT/vgchartzScrape.
# 
# Info on video games addiction APA research can be found here: https://www.psychiatry.org/patients-families/internet-gaming
# 
# The full video game sales tableau story can be seen here: https://public.tableau.com/shared/2SFYY87J5?:display_count=y&:origin=viz_share_link
# 
# For exploring and analysing data, pandas library and jupyter notebook was used.
# For visualization, tableau public and wordcloud was used. 

# ## Importing libraries and reading CSV files with pandas

# In[2]:


# let's begin by importing the basic libraries

import numpy as nb
import pandas as pd #data processing csv file
import csv

# open, analyze, and read the .csv file and turn it into a normal Pandas Data Frame

vgsales = pd.read_csv('/Users/janetliu/Desktop/videogames_sales/vgsales.csv')


# ## Checking and cleaning data values

# In[3]:


# we can then check the first 10 rows to see what our data looks like

vgsales.head(10)


# In[4]:


# I am going to do a quick search to see how many rows are included in the dataset

print('Total reports: ' + str(len(vgsales)))


# In[5]:


#let's check what data types we're working with. As we can see, we have a mix of integers, objects, and floats.  

vgsales.dtypes


# In[6]:


# I'm going to change some objects into categories. 

vgsales.dtypes

for col in [
    'Platform','Genre', 'Publisher']: vgsales[col] = vgsales[col].astype('category')


# In[7]:


# then re-print the datatypes to make sure the changes were made

vgsales.dtypes


# In[8]:


#let's check if our dataset include null values. We can see we have 271 in the "Year" column, and 58 in the "Publisher" column.
vgsales.isnull().sum()


# In[9]:


#we can use dropna() function to remove missing values since we have a goood number of records, and set how='any' to remove a row or column with any NA values present.
vgsales.dropna(how='any',inplace=True)
vgsales


# In[10]:


#now we can see our new dataset without nulls and how many rows were dropped. The new total row is now 16291. 
vgsales.info()


# ## Writing new CSV file with pandas

# In[11]:


#With my new dataset, lets save the modified file into our local drive so we can prepare our python scripts and embed it with charts created on Tableau Public Story.
vgsales.to_csv('vgsales_modified.csv')


# ## Python Scripts with embedded Tableau Charts

# ## Top 10s

# Top 10 Global Video Games

# In[12]:


#the first script is to find out what the toop 10 most sold games are
vgsales.groupby('Name')['Global_Sales'].max().sort_values(ascending=False).head(10)


# In[13]:


get_ipython().run_cell_magic('HTML', '', "\n<div class='tableauPlaceholder' id='viz1620288558321' style='position: relative'><noscript><a href='#'><img alt='Top 10 Global Video Games ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;pu&#47;publisherplatform&#47;Top10GlobalGames&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='publisherplatform&#47;Top10GlobalGames' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;pu&#47;publisherplatform&#47;Top10GlobalGames&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1620288558321');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1000px';vizElement.style.height='627px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>")


# From the chart, we can see Wii sports gained 82.74 million in global sales, followed by Super Mario Bros (40.24 million), Mario Kart Wii (35.82 million), and Wii Sports resort (33.0 million).

# In[14]:


get_ipython().run_cell_magic('HTML', '', "\n<div class='tableauPlaceholder' id='viz1620288464725' style='position: relative'><noscript><a href='#'><img alt='Top 10 Global Video Games ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;pu&#47;publisherplatform&#47;Top10GlobalGamesbyRegion&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='publisherplatform&#47;Top10GlobalGamesbyRegion' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;pu&#47;publisherplatform&#47;Top10GlobalGamesbyRegion&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1620288464725');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1000px';vizElement.style.height='627px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>")


# If we look at the top 10 global games by region, we can see most of the sale of Wii sports (41.49 million) and Super Mario Bros (29.08 million) were from North America alone.

# In[15]:


get_ipython().run_cell_magic('HTML', '', "\n<div class='tableauPlaceholder' id='viz1620288790613' style='position: relative'><noscript><a href='#'><img alt='Top 10 Global Games by Genre, Publisher, and Platform ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;pu&#47;publisherplatform&#47;Top10GlobalGamesbyGenrePublisherandPlatform&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='publisherplatform&#47;Top10GlobalGamesbyGenrePublisherandPlatform' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;pu&#47;publisherplatform&#47;Top10GlobalGamesbyGenrePublisherandPlatform&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1620288790613');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1000px';vizElement.style.height='627px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>")


# The top 10 global games come from 3 publishers and belong in 7 genres. "Activism" has produced a popular game for each of it's platform with the well-known shooter game, Call of Duty. "Nintendo" has been producing a variety of genres including its two most popular series on New Super Mario and Wii Sports. The last publisher is "Take-Two Interactive" with its action game Grand Theft Auto. 

# ## Most Popular

# Most Popular Genres

# In[16]:


# As the dataset contains over 16,000 records, I wanted to write Python scripts that can pull out certain data on value counts. The first is to see what the video game genre types are, and how many top ranked video games are listed under each.
vgsales["Genre"].value_counts().sort_values(ascending=False).head(10)


# In[17]:


get_ipython().run_cell_magic('HTML', '', "\n<div class='tableauPlaceholder' id='viz1620288949767' style='position: relative'><noscript><a href='#'><img alt='Most Popular Genres ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;pu&#47;publisherplatform&#47;MostPopularGenres_1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='publisherplatform&#47;MostPopularGenres_1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;pu&#47;publisherplatform&#47;MostPopularGenres_1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1620288949767');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1000px';vizElement.style.height='627px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>")


# As we can see from the chart about, 3,251 of the most popular video games belong in the action genre and 2,304 belong in the sports genre. This data indicates that gamers are interested in games that require movement and speed. 

# Most Popular Publishers & Platforms

# In[18]:


#number of publishers sorted by count
vgsales["Publisher"].value_counts().sort_values(ascending=False).head(10)


# In[19]:


#number of platforms sorted by count
vgsales["Platform"].value_counts().sort_values(ascending=False).head(10)


# In[20]:


get_ipython().run_cell_magic('HTML', '', "\n<div class='tableauPlaceholder' id='viz1620289203693' style='position: relative'><noscript><a href='#'><img alt='Most Popular Publishers and Platforms ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;pu&#47;publisherplatform&#47;MostPopularPublishersandPlatforms&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='publisherplatform&#47;MostPopularPublishersandPlatforms' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;pu&#47;publisherplatform&#47;MostPopularPublishersandPlatforms&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1620289203693');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1000px';vizElement.style.height='627px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>")


# Here is a graph that shows us the vast number of popular games that have been released by various publishers. My above graph only shows 10 different publishers, but it already contains a massive scale. We can see the publihsers "Namco" and "Sega" are some of the top publishers that have continiously released a variety of games for different platforms. 

# ## Sales over Time

# Total Sales by Region

# In[21]:


#from the total sums by region, we can see most of the sales for the most popular games are from North America. It would be interesting if we could find other data that shows video game sales for other Asian countries, as the APA research conducted on online game addiction was primarily on Asian countries.
vgsales.JP_Sales.sum()


# In[22]:


vgsales.NA_Sales.sum()


# In[23]:


vgsales.EU_Sales.sum()


# Yearly Sales by Region

# In[24]:


vgsales.groupby(['Year'])['JP_Sales', 'EU_Sales', 'NA_Sales', 'Other_Sales'].sum()


# In[25]:


get_ipython().run_cell_magic('HTML', '', "\n<div class='tableauPlaceholder' id='viz1620289919487' style='position: relative'><noscript><a href='#'><img alt='Yearly Sales by Region ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;pu&#47;publisherplatform&#47;YearlySalesbyRegion&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='publisherplatform&#47;YearlySalesbyRegion' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;pu&#47;publisherplatform&#47;YearlySalesbyRegion&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1620289919487');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1000px';vizElement.style.height='627px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>")


# We can see the years of 2006 to 2009 brought the most video game sales for all regions. 2008 seemed to be a good year, as North America had 351 million in sales. Since then, there has been a steep decline than exponentially growing as the market has forecasted. This rise in sales may have been contributed by Wii, as the console was released on November 19, 2006.

# Top 50 Game Sales over Time

# In[26]:


vgsales.groupby('Year')['Global_Sales'].max().sort_values(ascending=False)


# In[27]:


get_ipython().run_cell_magic('HTML', '', "\n<div class='tableauPlaceholder' id='viz1620290100580' style='position: relative'><noscript><a href='#'><img alt='Top 50 Game Sales over Time ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;pu&#47;publisherplatform&#47;Top50GameSalesoverTime&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='publisherplatform&#47;Top50GameSalesoverTime' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;pu&#47;publisherplatform&#47;Top50GameSalesoverTime&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1620290100580');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1000px';vizElement.style.height='627px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>")


# If we look at the top 50 game sales for the top 10 years, we can see 2006 has been a good year that produced a variety of game genres for video gamers. These include the Wii platform games that became a big hit (again, the console was released in 2006). Action games have been doing well over time. It was a big hit in the early years of 2002 with the release of grand theft auto, followed by shooter games in the more recent years such as call of duty. It would be good for the gaming industry to produce more sport games, since the sport genre that has been doing suprisingly well. 

# ## Most Sold Games/Genres by Region

# Most sold games by Region

# In[28]:


##here is breakdown of the most sold games by region, starting with North America
vgsales.groupby('Name')['NA_Sales'].max().sort_values(ascending=False).head(10)


# In[29]:


##most sold games in Europe
vgsales.groupby('Name')['EU_Sales'].max().sort_values(ascending=False).head(10)


# In[30]:


##and most sold games in Japan
vgsales.groupby('Name')['JP_Sales'].max().sort_values(ascending=False).head(10)


# Most Sold Games by Genre

# In[31]:


##and here is a breakdown of the most sold game genres by region, starting with North America
vgsales.groupby('Genre')['NA_Sales'].max().sort_values(ascending=False).head(10)


# In[32]:


##wmost sold game genres by Europe
vgsales.groupby('Genre')['EU_Sales'].max().sort_values(ascending=False).head(10)


# In[33]:


##and most sold game genres by Japan
vgsales.groupby('Genre')['JP_Sales'].max().sort_values(ascending=False).head(10)


# In[34]:


get_ipython().run_cell_magic('HTML', '', "\n<div class='tableauPlaceholder' id='viz1619942460510' style='position: relative'><noscript><a href='#'><img alt='Most Sold Games&#47;Genres by Region ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;pu&#47;publisherplatform&#47;MostSoldGamesGenresbyRegion&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='publisherplatform&#47;MostSoldGamesGenresbyRegion' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;pu&#47;publisherplatform&#47;MostSoldGamesGenresbyRegion&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1619942460510');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='1000px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='1227px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='1000px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='1227px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='927px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>")


# We can combine the most sold games/genres by region and can see these games vary greatly. North America and Europe tend to have a variety of popular games from the action, racing, shooting, and sports category. While North America has a preference for WII Sports (41.49 million in sales), we can see Europe (huge football fans) enjoy FIFA. Surprisngly, Japan gamers have a completely different preference with little interest in action and shooting games, but prefer the role-playing genre such as the pokemon series. From this data, it would seem the video game industry will do well releasing shooting or sport games that would gain big sales in Europe and North America as well as role-playing games for Japan.

# ## Top 100 Games Wordcloud

# In[35]:


get_ipython().run_cell_magic('HTML', '', '\n<a href="https://www.wordclouds.com/?yygpKSi20tfP1MvMTS8t0kvOz9WPqsoyNaxy0SvISwcA" target="_blank"><img src="https://i.imgur.com/Zzj51zD.png" border="0" alt="Made with WordClouds.com"/></a>')


# To wrap it up, here is a word cloud that pulls text from the top 100 most popular games. We can see the greatest count in text is wii, mario, and shooter.

# ## Tableau Story

# In[36]:


##view the full tableau story below


# In[37]:


get_ipython().run_cell_magic('HTML', '', "\n<div class='tableauPlaceholder' id='viz1620290879946' style='position: relative'><noscript><a href='#'><img alt='Video Game Sales ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;pu&#47;publisherplatform&#47;VideoGameSales&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='publisherplatform&#47;VideoGameSales' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;pu&#47;publisherplatform&#47;VideoGameSales&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1620290879946');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1016px';vizElement.style.height='991px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>")

