import pandas as pd

# Replace these lists with your data
audio_file_names = ["audio1.wav", "audio2.wav", "audio3.wav"]
predicted_keywords = ["keyword1", "keyword2", "keyword3"]

# Create a DataFrame with appropriate columns
data = {'Audio File Name': audio_file_names, 'Predicted Keyword': predicted_keywords}
df = pd.DataFrame(data)

# Print the DataFrame
print(df)