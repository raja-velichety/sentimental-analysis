data= LOAD '/home/chandu-pc/Desktop/tweets.csv' USING PigStorage(',') as (id: chararray,text:chararray);

extract_details = FOREACH data GENERATE $0 as id,$1 as text;

tokens = foreach extract_details generate id,text, FLATTEN(TOKENIZE(text)) As word;
dictionary = load '/home/chandu-pc/Desktop/AFINN-111.txt' using PigStorage('\t') AS(word:chararray,rating:int);

word_rating = join tokens by word left outer, dictionary by word using 'replicated';

rating = foreach word_rating generate tokens::id as id,tokens::text as text, dictionary::rating as rate;

 word_group = group rating by (id,text);

avg_rate = foreach word_group generate group, AVG(rating.rate) as tweet_rating;


positive_tweets = filter avg_rate by tweet_rating>=0;

negative_tweets = filter avg_rate by tweet_rating<0;

grp= group positive_tweets all;
pos_count= foreach grp generate COUNT(positive_tweets);
Dump pos_count;
same with negative tweets
neg= group negative_tweets all;
neg_count= foreach neg generate COUNT(negative_tweets);
Dump neg_count;

