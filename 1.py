import matplotlib.pyplot as plt
import pandas as pd

# Example data (replace with your own data)
timestamps = ["2023-10-19 10:00:00", "2023-10-19 10:15:00", "2023-10-19 10:30:00"]
keywords_detected = ["keyword1", None, "keyword2"]

# Convert timestamps to datetime objects
timestamps = pd.to_datetime(timestamps)

# Create a DataFrame with timestamps and detected keywords
data = {'Timestamp': timestamps, 'Keywords Detected': keywords_detected}
df = pd.DataFrame(data)

# Plot the timeline
plt.figure(figsize=(10, 3))
plt.eventplot(df['Timestamp'], orientation='horizontal', lineoffsets=1, linelengths=1, linewidths=2, colors='b')
plt.yticks([1], ['Keywords'])
plt.xlabel('Time')
plt.title('Keyword Detection Timeline')

# Show the plot
plt.grid()
plt.show()