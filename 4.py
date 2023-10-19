import pandas as pd

# Replace these lists with your data
audio_file_names = ["audio1.wav", "audio2.wav", "audio3.wav"]
predicted_emotions = ["happy", "sad", "happy"]

# Create a DataFrame
data = {'Audio File Name': audio_file_names, 'Predicted Emotion': predicted_emotions}
df = pd.DataFrame(data)

# Print the DataFrame
print(df)