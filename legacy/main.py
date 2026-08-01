# Generated from: 00-Capstone-Project.ipynb
# Converted at: 2026-01-25T08:25:44.302Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Capstone Project
# ## Overview
# 
# If you are planning on going out to see a movie, how well can you trust online reviews and ratings? *Especially* if the same company showing the rating *also* makes money by selling movie tickets. Do they have a bias towards rating movies higher than they should be rated?
# 
# ### Goal:
# 
# **Your goal is to complete the tasks below based off the 538 article and see if you reach a similar conclusion. You will need to use your pandas and visualization skills to determine if Fandango's ratings in 2015 had a bias towards rating movies better to sell more tickets.**
# 
# ---
# ---
# 
# **Complete the tasks written in bold.**
# 
# ---
# ----
# 
# ## Part One: Understanding the Background and Data
# 
# 
# **TASK: Read this article: [Be Suspicious Of Online Movie Ratings, Especially Fandango’s](http://fivethirtyeight.com/features/fandango-movies-ratings/)**


# ----
# 
# **TASK: After reading the article, read these two tables giving an overview of the two .csv files we will be working with:**
# 
# ### The Data
# 
# This is the data behind the story [Be Suspicious Of Online Movie Ratings, Especially Fandango’s](http://fivethirtyeight.com/features/fandango-movies-ratings/) openly available on 538's github: https://github.com/fivethirtyeight/data. There are two csv files, one with Fandango Stars and Displayed Ratings, and the other with aggregate data for movie ratings from other sites, like Metacritic,IMDB, and Rotten Tomatoes.
# 
# #### all_sites_scores.csv


# -----
# 
# `all_sites_scores.csv` contains every film that has a Rotten Tomatoes rating, a RT User rating, a Metacritic score, a Metacritic User score, and IMDb score, and at least 30 fan reviews on Fandango. The data from Fandango was pulled on Aug. 24, 2015.


# Column | Definition
# --- | -----------
# FILM | The film in question
# RottenTomatoes | The Rotten Tomatoes Tomatometer score  for the film
# RottenTomatoes_User | The Rotten Tomatoes user score for the film
# Metacritic | The Metacritic critic score for the film
# Metacritic_User | The Metacritic user score for the film
# IMDB | The IMDb user score for the film
# Metacritic_user_vote_count | The number of user votes the film had on Metacritic
# IMDB_user_vote_count | The number of user votes the film had on IMDb


# ----
# ----
# 
# #### fandango_scape.csv


# `fandango_scrape.csv` contains every film 538 pulled from Fandango.
# 
# Column | Definiton
# --- | ---------
# FILM | The movie
# STARS | Number of stars presented on Fandango.com
# RATING |  The Fandango ratingValue for the film, as pulled from the HTML of each page. This is the actual average score the movie obtained.
# VOTES | number of people who had reviewed the film at the time we pulled it.


# ----
# 
# **TASK: Import any libraries you think you will use:**


# IMPORT HERE!

# Data handling
import numpy as np
import pandas as pd

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns


# ## Part Two: Exploring Fandango Displayed Scores versus True User Ratings
# 
# Let's first explore the Fandango ratings to see if our analysis agrees with the article's conclusion.
# 
# **TASK: Run the cell below to read in the fandango_scrape.csv file**


fandango = pd.read_csv("fandango_scrape.csv")
fandango

# **TASK: Explore the DataFrame Properties and Head.**


fandango.head()

fandango.info()

fandango.columns

fandango.shape

fandango.describe()

fandango.tail()

# **TASK: Let's explore the relationship between popularity of a film and its rating. Create a scatterplot showing the relationship between rating and votes. Feel free to edit visual styling to your preference.**


# CODE HERE

plt.figure(figsize=(10,6),dpi=150)
sns.scatterplot(data=fandango,x="RATING",y="VOTES");
plt.title("Relationship Between Movie Rating and Popularity (Votes)")
plt.xlabel("Rating")
plt.ylabel("Number of Votes")
plt.show()

# 
# **TASK: Calculate the correlation between the columns:**


# CODE HERE

fandango[['STARS','RATING', 'VOTES']].corr()


# **TASK: Assuming that every row in the FILM title column has the same format:**
# 
#     Film Title Name (Year)
#     
# **Create a new column that is able to strip the year from the title strings and set this new column as YEAR**


# CODE HERE

# Extract year from FILM column and convert to integer

#fandango['YEAR'] = fandango['FILM'].apply(lambda title:title.splite('(')[-1])
fandango['YEAR'] = fandango['FILM'].str.extract(r'\((\d{4})\)').astype(int)
fandango[['FILM', 'YEAR']].head()

# **TASK: How many movies are in the Fandango DataFrame per year?**


#CODE HERE


fandango['YEAR'].value_counts()

# **TASK: Visualize the count of movies per year with a plot:**


#CODE HERE

plt.figure(figsize=(8,5))
sns.countplot(data=fandango,x='YEAR')

plt.title("Count of Movies per Year in Fandango Dataset")
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.show()

# **TASK: What are the 10 movies with the highest number of votes?**


#CODE HERE

#fandango.sort_values('VOTES', ascending=False).head(10)[['FILM', 'VOTES']]
fandango.nlargest(10,'VOTES')

# **TASK: How many movies have zero votes?**


#CODE HERE

no_votes = fandango['VOTES']==0
no_votes.sum()

# **TASK: Create DataFrame of only reviewed films by removing any films that have zero votes.**


#CODE HERE

fan_reviewed = fandango[fandango['VOTES']>0]
fan_reviewed

# ----
# 
# **As noted in the article, due to HTML and star rating displays, the true user rating may be slightly different than the rating shown to a user. Let's visualize this difference in distributions.**
# 
# **TASK: Create a KDE plot (or multiple kdeplots) that displays the distribution of ratings that are displayed (STARS) versus what the true rating was from votes (RATING). Clip the KDEs to 0-5.**


#CODE HERE

plt.figure(figsize=(10,4),dpi=150)
sns.kdeplot(data=fan_reviewed,x='RATING',clip=[0,5],fill=True,label='True Rating')
sns.kdeplot(data=fan_reviewed,x='STARS',clip=[0,5],fill=True,label='Stars Displayed')
plt.legend(loc=(1.05,0.5))


# **TASK: Let's now actually quantify this discrepancy. Create a new column of the different between STARS displayed versus true RATING. Calculate this difference with STARS-RATING and round these differences to the nearest decimal point.**


#CODE HERE

fan_reviewed['STARS_DIFF'] = fan_reviewed['STARS'] - fan_reviewed['RATING']
fan_reviewed['STARS_DIFF'] = fan_reviewed['STARS_DIFF'].round(2)
fan_reviewed



# **TASK: Create a count plot to display the number of times a certain difference occurs:**


#CODE HERE

plt.figure(figsize=(12,4),dpi=150)
sns.countplot(data=fan_reviewed,x='STARS_DIFF',palette='magma')

# **TASK: We can see from the plot that one movie was displaying over a 1 star difference than its true rating! What movie had this close to 1 star differential?**


#CODE HERE

fan_reviewed[fan_reviewed['STARS_DIFF']==1]

# ## Part Three: Comparison of Fandango Ratings to Other Sites
# 
# Let's now compare the scores from Fandango to other movies sites and see how they compare.
# 
# **TASK: Read in the "all_sites_scores.csv" file by running the cell below**


all_sites = pd.read_csv("all_sites_scores.csv")
all_sites

# **TASK: Explore the DataFrame columns, info, description.**


all_sites.columns

all_sites.info()

all_sites.describe()

all_sites.head()

# ### Rotten Tomatoes
# 
# Let's first take a look at Rotten Tomatoes. RT has two sets of reviews, their critics reviews (ratings published by official critics) and user reviews. 
# 
# **TASK: Create a scatterplot exploring the relationship between RT Critic reviews and RT User reviews.**


# CODE HERE
plt.figure(figsize=(10,4),dpi=200)
sns.scatterplot(data=all_sites,x='RottenTomatoes',y='RottenTomatoes_User')
plt.title("Rotten Tomatoes: Critics vs User Ratings")
plt.xlabel("Rotten Tomatoes Critic Score")
plt.ylabel("Rotten Tomatoes User Score")
plt.show()




# Let's quantify this difference by comparing the critics ratings and the RT User ratings. We will calculate this with RottenTomatoes-RottenTomatoes_User. Note: Rotten_Diff here is Critics - User Score. So values closer to 0 means aggrement between Critics and Users. Larger positive values means critics rated much higher than users. Larger negative values means users rated much higher than critics.
# 
# **TASK: Create a new column based off the difference between critics ratings and users ratings for Rotten Tomatoes. Calculate this with RottenTomatoes-RottenTomatoes_User**


#CODE HERE
all_sites['Rotten_Diff'] = all_sites['RottenTomatoes'] - all_sites['RottenTomatoes_User']
all_sites[['RottenTomatoes', 'RottenTomatoes_User', 'Rotten_Diff']].head()



# Let's now compare the overall mean difference. Since we're dealing with differences that could be negative or positive, first take the absolute value of all the differences, then take the mean. This would report back on average to absolute difference between the critics rating versus the user rating.


# **TASK: Calculate the Mean Absolute Difference between RT scores and RT User scores as described above.**


# CODE HERE
mad_rt = all_sites['Rotten_Diff'].abs().mean()
mad_rt



# **TASK: Plot the distribution of the differences between RT Critics Score and RT User Score. There should be negative values in this distribution plot. Feel free to use KDE or Histograms to display this distribution.**


#CODE HERE

plt.figure(figsize=(10,4),dpi=200)
sns.histplot(data=all_sites,x='Rotten_Diff',bins=30,kde=True)
plt.title("RT Critics Score minus User Score");
plt.xlabel("RottenTomatoes - RottenTomatoes_User")
plt.ylabel("Count")
plt.show()



# **TASK: Now create a distribution showing the *absolute value* difference between Critics and Users on Rotten Tomatoes.**


#CODE HERE

abs_diff = all_sites['Rotten_Diff'].abs()
plt.figure(figsize=(10,4),dpi=200)
sns.histplot(abs_diff,bins=30,kde=True)
plt.title("Absolute Difference Between RT Critics and User Scores")
plt.xlabel("|RottenTomatoes - RottenTomatoes_User|")
plt.ylabel("Count")
plt.show()



# **Let's find out which movies are causing the largest differences. First, show the top 5 movies with the largest *negative* difference between Users and RT critics. Since we calculated the difference as Critics Rating - Users Rating, then large negative values imply the users rated the movie much higher on average than the critics did.**


# **TASK: What are the top 5 movies users rated higher than critics on average:**


# CODE HERE

all_sites.nsmallest(5,'Rotten_Diff')[['FILM', 'RottenTomatoes', 'RottenTomatoes_User', 'Rotten_Diff']]



# **TASK: Now show the top 5 movies critics scores higher than users on average.**


# CODE HERE

all_sites.nlargest(5,'Rotten_Diff')[['FILM', 'RottenTomatoes', 'RottenTomatoes_User', 'Rotten_Diff']]




# ## MetaCritic
# 
# Now let's take a quick look at the ratings from MetaCritic. Metacritic also shows an average user rating versus their official displayed rating.


# **TASK: Display a scatterplot of the Metacritic Rating versus the Metacritic User rating.**


# CODE HERE

plt.figure(figsize=(10,4),dpi=150)
sns.scatterplot(data=all_sites,x='Metacritic',y='Metacritic_User')
plt.title("Metacritic: Critics Rating vs User Rating")
plt.xlabel("Metacritic Critic Rating")
plt.ylabel("Metacritic User Rating")
plt.show()



# ## IMDB
# 
# Finally let's explore IMDB. Notice that both Metacritic and IMDB report back vote counts. Let's analyze the most popular movies.
# 
# **TASK: Create a scatterplot for the relationship between vote counts on MetaCritic versus vote counts on IMDB.**


#CODE HERE

plt.figure(figsize=(10,4),dpi=150)
sns.scatterplot(data=all_sites,x='Metacritic_user_vote_count', y='IMDB_user_vote_count')
plt.title("Metacritic vs IMDb: User Vote Counts")
plt.xlabel("Metacritic User Vote Count")
plt.ylabel("IMDb User Vote Count")
plt.show()



# **Notice there are two outliers here. The movie with the highest vote count on IMDB only has about 500 Metacritic ratings. What is this movie?**
# 
# **TASK: What movie has the highest IMDB user vote count?**


#CODE HERE

all_sites.nlargest(1,'IMDB_user_vote_count')[['FILM','IMDB_user_vote_count','Metacritic_user_vote_count']]



# **TASK: What movie has the highest Metacritic User Vote count?**


#CODE HERE

all_sites.nlargest(1,'Metacritic_user_vote_count')[['FILM','Metacritic_user_vote_count','IMDB_user_vote_count']]



# ## Fandago Scores vs. All Sites
# 
# Finally let's begin to explore whether or not Fandango artificially displays higher ratings than warranted to boost ticket sales.


# **TASK: Combine the Fandango Table with the All Sites table. Not every movie in the Fandango table is in the All Sites table, since some Fandango movies have very little or no reviews. We only want to compare movies that are in both DataFrames, so do an *inner* merge to merge together both DataFrames based on the FILM columns.**


#CODE HERE

combined_df = fandango.merge(all_sites,on='FILM',how='inner')
combined_df.head()







# ### Normalize columns to Fandango STARS and RATINGS 0-5 
# 
# Notice that RT,Metacritic, and IMDB don't use a score between 0-5 stars like Fandango does. In order to do a fair comparison, we need to *normalize* these values so they all fall between 0-5 stars and the relationship between reviews stays the same.
# 
# **TASK: Create new normalized columns for all ratings so they match up within the 0-5 star range shown on Fandango. There are many ways to do this.**
# 
# Hint link: https://stackoverflow.com/questions/26414913/normalize-columns-of-pandas-data-frame
# 
# 
# Easier Hint:
# 
# Keep in mind, a simple way to convert ratings:
# * 100/20 = 5 
# * 10/2 = 5


# CODE HERE

combined_df['RT_norm'] = combined_df['RottenTomatoes'] / 20
combined_df['RT_user_norm'] = combined_df['RottenTomatoes_User'] / 20
combined_df['Meta_norm'] = combined_df['Metacritic'] / 20
combined_df['Meta_user_norm'] = combined_df['Metacritic_User'] / 2
combined_df['IMDB_norm'] = combined_df['IMDB'] / 2
combined_df['Fandango_STARS_norm'] = combined_df['STARS']
combined_df['Fandango_RATING_norm'] = combined_df['RATING']
combined_df.head()





# **TASK: Now create a norm_scores DataFrame that only contains the normalizes ratings. Include both STARS and RATING from the original Fandango table.**


#CODE HERE

norm_scores = combined_df[['Fandango_STARS_norm','Fandango_RATING_norm','RT_norm','RT_user_norm','Meta_norm',
    'Meta_user_norm','IMDB_norm']]
norm_scores.head()





# ### Comparing Distribution of Scores Across Sites
# 
# 
# Now the moment of truth! Does Fandango display abnormally high ratings? We already know it pushs displayed RATING higher than STARS, but are the ratings themselves higher than average?
# 
# 
# **TASK: Create a plot comparing the distributions of normalized ratings across all sites. There are many ways to do this, but explore the Seaborn KDEplot docs for some simple ways to quickly show this. Don't worry if your plot format does not look exactly the same as ours, as long as the differences in distribution are clear.**
# 
# Quick Note if you have issues moving the legend for a seaborn kdeplot: https://github.com/mwaskom/seaborn/issues/2280


#CODE HERE
plt.figure(figsize=(10,6))
sns.kdeplot(all_sites['RT_norm'], label='Rotten Tomatoes', fill=True)
sns.kdeplot(all_sites['Meta_norm'], label='Metacritic', fill=True)
sns.kdeplot(all_sites['IMDB_norm'], label='IMDB', fill=True)
plt.title('Distribution of Normalized Ratings Across Sites')
plt.xlabel('Normalized Rating (0–5)')
plt.ylabel('Density')
plt.legend()
plt.tight_layout()
plt.show()



# **Clearly Fandango has an uneven distribution. We can also see that RT critics have the most uniform distribution. Let's directly compare these two.** 
# 
# **TASK: Create a KDE plot that compare the distribution of RT critic ratings against the STARS displayed by Fandango.**


#CODE HERE
all_sites['RT_critics_norm'] = all_sites['RottenTomatoes'] / 20
plt.figure(figsize=(10,6))

sns.kdeplot(all_sites['RT_critics_norm'],label='RT Critics (Normalized)',fill=True)

sns.kdeplot(fandango['STARS'],label='Fandango Stars (Displayed)',fill=True)

plt.title('RT Critics vs Fandango Displayed Star Ratings')
plt.xlabel('Rating (0–5)')
plt.ylabel('Density')
plt.legend()
plt.tight_layout()
plt.show()




# **OPTIONAL TASK: Create a histplot comparing all normalized scores.**


#CODE HERE
plt.figure(figsize=(10,6))

sns.histplot(all_sites['RT_critics_norm'], bins=20, label='RT Critics', stat='density')
sns.histplot(all_sites['RottenTomatoes_User'], bins=20, label='RT Users', stat='density')
sns.histplot(all_sites['Meta_user_norm'], bins=20, label='Metacritic Users', stat='density')
sns.histplot(all_sites['IMDB_norm'], bins=20, label='IMDB', stat='density')
sns.histplot(fandango['STARS'], bins=20, label='Fandango Stars', stat='density')

plt.title('Histogram of Normalized Ratings Across All Sites')
plt.xlabel('Normalized Rating (0–5)')
plt.ylabel('Density')
plt.legend()
plt.tight_layout()
plt.show()



# 
# ### How are the worst movies rated across all platforms?
# 
# **TASK: Create a clustermap visualization of all normalized scores. Note the differences in ratings, highly rated movies should be clustered together versus poorly rated movies. Note: This clustermap does not need to have the FILM titles as the index, feel free to drop it for the clustermap.**


# CODE HERE

# Select ONLY existing normalized columns

norm_scores = all_sites[['RT_norm','RT_critics_norm','Meta_norm','Meta_user_norm','IMDB_norm']]

# Drop film titles implicitly (not included)
# Sort movies by average rating

norm_scores = norm_scores.loc[norm_scores.mean(axis=1).sort_values().index]

# Create clustermap

sns.clustermap(norm_scores,cmap='coolwarm',linewidths=0.5,figsize=(12,10),standard_scale=1)

plt.suptitle('Clustermap of Normalized Movie Ratings Across Platforms',y=1.02)

plt.show()



# **TASK: Clearly Fandango is rating movies much higher than other sites, especially considering that it is then displaying a rounded up version of the rating. Let's examine the top 10 worst movies. Based off the Rotten Tomatoes Critic Ratings, what are the top 10 lowest rated movies? What are the normalized scores across all platforms for these movies? You may need to add the FILM column back in to your DataFrame of normalized scores to see the results.**


# CODE HERE

# Step 1: Sort by Rotten Tomatoes critic score (lowest)

worst_10 = all_sites.sort_values('RT_norm').head(10)


# Step 2: Select FILM + all normalized rating columns

worst_10_norm_scores = worst_10[['FILM','RT_norm','RT_critics_norm','Meta_norm','Meta_user_norm','IMDB_norm']]

# Step 3: Reset index for clean display (optional)

worst_10_norm_scores = worst_10_norm_scores.reset_index(drop=True)
worst_10_norm_scores






# **FINAL TASK: Visualize the distribution of ratings across all sites for the top 10 worst movies.**


# CODE HERE

# Select 10 worst movies by Rotten Tomatoes critic score
worst_10 = all_sites.sort_values('RT_norm').head(10)

# Select normalized scores
worst_10_scores = worst_10[['FILM','RT_norm','RT_critics_norm','Meta_norm','Meta_user_norm','IMDB_norm']]

# Melt for seaborn
worst_10_melted = worst_10_scores.melt(id_vars='FILM',var_name='Platform',value_name='Normalized Rating')

plt.figure(figsize=(12,6))

sns.violinplot(data=worst_10_melted,x='Platform',y='Normalized Rating')

plt.title('Rating Distribution Across Platforms\nTop 10 Worst Movies (RT Critics)')
plt.xlabel('Platform')
plt.ylabel('Normalized Rating (0–5)')

plt.xticks(rotation=30)
plt.show()


# ---
# ----
# 
# <img src="https://upload.wikimedia.org/wikipedia/en/6/6f/Taken_3_poster.jpg">
# 
# **Final thoughts: Wow! Fandango is showing around 3-4 star ratings for films that are clearly bad! Notice the biggest offender, [Taken 3!](https://www.youtube.com/watch?v=tJrfImRCHJ0). Fandango is displaying 4.5 stars on their site for a film with an [average rating of 1.86](https://en.wikipedia.org/wiki/Taken_3#Critical_response) across the other platforms!**




0.4+2.3+1.3+2.3+3

9.3/5

# ----
