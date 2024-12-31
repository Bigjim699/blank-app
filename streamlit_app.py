import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import requests

# Example player data for the last 5 games
data = {
    'Game': ['Game 1', 'Game 2', 'Game 3', 'Game 4', 'Game 5'],
    'Points': [25, 30, 15, 20, 18],
    'Assists': [5, 7, 4, 6, 8],
    'Rebounds': [10, 8, 9, 7, 10]
}

df = pd.DataFrame(data)

# Display data in the app
st.title('Player Performance')
st.write('Stats for the last 5 games:')
st.dataframe(df)

# Create a plot for the data
fig, ax = plt.subplots()
df.set_index('Game')[['Points', 'Assists', 'Rebounds']].plot(kind='bar', ax=ax)
st.pyplot(fig)

# Fetch live player data from the API based on user input
player_name = st.text_input("Enter Player Name:", "LeBron James")

# Example API call (replace with the actual API URL and key)
url = 'https://api.sportsdata.io/v3/nba/scores/json/PlayerSeasonStats/2024'
headers = {'Authorization': 'Bearer YOUR_API_KEY'}

# Fetch data from the API
response = requests.get(url, headers=headers)
data = response.json()  # Parse the JSON data

# Displaying the data for the player entered
player_found = False
for player in data:
    if player['Name'] == player_name:
        st.write(f"Stats for {player_name}:")
        st.write(f"Points: {player['Points']}")
        st.write(f"Assists: {player['Assists']}")
        st.write(f"Rebounds: {player['Rebounds']}")
        player_found = True

if not player_found:
    st.write("Player not found or invalid player name.")
