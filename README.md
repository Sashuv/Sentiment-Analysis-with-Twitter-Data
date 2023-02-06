# Sentiment Analysis of Twitter Data

This project is a sentiment analysis program built using python and utilizing the twitter dataset from Kaggle. 

**Dataset link:** https://www.kaggle.com/datasets/jp797498e/twitter-entity-sentiment-analysis
## Tools Used
- Python
- Pandas
- Scikit-learn
- Streamlit 
- Matplotlib 

## Preprocessing 
The data was preprocessed by removing the stopwords, punctuations, and converting all the text to lowercase. The resulting preprocessed data was then used to fit the algorithms. 

## Vectorization
Count Vectorizer was used for vectorization instead of Tf-Idf because it gave better results. 

## How to use the program
1. Clone the repository to your local machine using `git clone` command
2. Navigate to the project directory
3. Install the required packages using `pip install -r requirements.txt`
4. Launch the app using `streamlit run app.py`
5. The app will be available in your browser at `http://localhost:8501/`

## Results
The program achieved an accuracy of 92.87%, precision of 92.86%, recall of 92.90% and F1 score of 92.87%. These results indicate that the model is able to accurately predict the sentiment of the tweets in the dataset. However, further work can be done to improve the performance of the model, such as trying different algorithms, fine-tuning the parameters, and using a larger dataset.
Note: The results may vary depending on the data used.
