import pandas as pd

# Load the channel data
df = pd.read_csv('youtube_channel_data.csv')

# Cleaning function
def clean_data(df):
    # Remove rows with null values
    df = df.dropna()
    
    # Example: Convert subscriber count to integer
    df['subscriber_count'] = df['subscriber_count'].astype(int)
    
    return df

# Clean the data
cleaned_df = clean_data(df)

# Save the cleaned data
cleaned_df.to_csv('cleaned_youtube_channel_data.csv', index=False)
print("Data cleaned and saved to 'cleaned_youtube_channel_data.csv'.")
