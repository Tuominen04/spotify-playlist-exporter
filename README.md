# Spotify Playlist Exporter

A simple Python script to export song titles and artists from a Spotify playlist into a CSV file. [🔗](https://tuominen04.github.io/projects/spotify_playlist_exporter/)

## Features
- Exports all tracks from any public Spotify playlist
- Saves track name and artist(s) to a CSV file

## Requirements
- Python 3.8+
- A Spotify Developer account ([create here](https://developer.spotify.com/dashboard/))
- Spotify API credentials (Client ID & Client Secret)

## Setup

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/spotify-playlist-exporter.git
   cd spotify-playlist-exporter

1. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

1. **Create a `.env` file**
Copy `example.env` to `.env` and fill in your own Spotify credentials:
   ```bash
   cp .env.example .env
   
1. **Run the script:**
    ```bash
     python main.py

1. **Check the outhput**
Your playlist tracks will be saved in `track_info.csv`.

## Example output

|Track|Artist|
|--|--|
|Sonne|Rammstein|
|Storytime|Nightwish|
|Amongst Stars|Amorphis|
