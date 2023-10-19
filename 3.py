import matplotlib.pyplot as plt
import pandas as pd

# Example data (replace with your own data)
timestamps = ["2023-10-19 10:00:00", "2023-10-19 10:15:00", "2023-10-19 10:30:00", "2023-10-19 10:45:00"]
predicted_emotions = [0.5, -0.3, 0.8, -0.1]  # Values between -1 (sad) and 1 (happy)

# Convert timestamps to datetime objects
timestamps = pd.to_datetime(timestamps)

# Create a DataFrame with timestamps and predicted emotions
data = {'Timestamp': timestamps, 'Predicted Emotion': predicted_emotions}
df = pd.DataFrame(data)

# Plot the line chart
plt.figure(figsize=(10, 5))
plt.plot(df['Timestamp'], df['Predicted Emotion'], marker='o', linestyle='-', color='b')

# Set y-axis labels
plt.yticks([-1, -0.5, 0, 0.5, 1], ['sad', '', 'neutral', '', 'happy'])

# Set x-axis label
plt.xlabel('Time')

# Set plot title
plt.title('Predicted Emotion Over Time')

# Show the plot
plt.grid()
plt.show()
