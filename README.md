# Using LLM to estimate news sentiment and build trading strategies

## 1. Training Dataset
#### There are many publicly available datasets that classify sentence sentiment, but most of them only distinguish between three categories: positive, negative, and neutral.

#### This makes it difficult to quantify the degree of sentiment as a numerical score. Our dataset is based on the paper "SLee, J., Youn, H., Poon, J., & Han, S. (2023). StockEmotions: Discover Investor Emotions for Financial Sentiment Analysis and Multivariate Time Series.", which classifies sentences into 12 different emotions. We have transformed these 12 emotions into sentiment scores to serve as training data for the LLM - Llama 3.

## 2. Strategy Description
#### We used Selenium for web scraping and collected all news articles related to TSMC (NYSE: TSM) from Yahoo Finance over the past month, sorting them in chronological order.

#### The sample period spans from January 17, 2025, to February 17, 2025, during which we gathered a total of 167 news headlines and summaries.

#### We then fed these news articles into a trained Llama model, which provided sentiment scores for each piece of news. By averaging the sentiment scores of all news articles for each day, we formulated a trading strategy: if the total daily sentiment score exceeds the monthly median, we buy; if it falls below the median, we sell.

## 3. Final Result

#### Over the past month, the strategy executed four buy trades and four sell trades, resulting in a final monthly return of 8.22%. During the same period, TSM's return was -3.6%. This demonstrates that the strategy significantly outperformed the buy-and-hold strategy.

#### However, this strategy currently has several limitations:

#### (1) Hardware Constraints: Due to hardware limitations, we used the 3B-parameter version of Llama 3.2. If a larger LLM with more parameters were available, the prediction accuracy could be further improved.

#### (2) Training Data: There are very few datasets that quantify sentiment scores in practice. Most datasets only classify sentiment into three categories, making it difficult for the LLM to achieve precise numerical sentiment quantification.

#### (3) Experimental Data: In recent years, many social media platforms (such as X and Reddit) have discontinued free web scraping access, requiring paid API subscriptions. If a large volume of user-generated sentiment data could be obtained, the model's prediction accuracy might be further enhanced.
