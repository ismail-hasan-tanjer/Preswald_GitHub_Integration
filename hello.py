from preswald import text, plotly, connect, get_df, table, slider
import pandas as pd
import plotly.express as px

# Welcome message
text("# Welcome to Preswald!")
text("This is my first app. 🎉")

# Load the CSV
connect()  # load in all sources, which by default is the sample_csv
df = get_df('weather_classification_data.csv')

# Add a slider to filter the data
threshold = slider("Threshold", min_val=0, max_val=100, default=50)

# Filter the data based on the threshold
filtered_df = df[df["value"] > threshold]

# Create a scatter plot
fig = px.scatter(df, x='quantity', y='value', text='item',
                 title='Quantity vs. Value',
                 labels={'quantity': 'Quantity', 'value': 'Value'})

# Add labels for each point
fig.update_traces(textposition='top center', marker=dict(size=12, color='lightblue'))

# Style the plot
fig.update_layout(template='plotly_white')

# Show the plot
plotly(fig)

# Create a dynamic scatter plot for filtered data
fig2 = px.scatter(filtered_df, x='quantity', y='value', text='item',
                  title='Filtered Quantity vs. Value',
                  labels={'quantity': 'Quantity', 'value': 'Value'})

# Add labels and styling for the filtered plot
fig2.update_traces(textposition='top center', marker=dict(size=12, color='orange'))
fig2.update_layout(template='plotly_white')

# Show the filtered plot
plotly(fig2)

# Show the data
table(df)

# Display Filtered Data
table(filtered_df, title="Filtered Data")



