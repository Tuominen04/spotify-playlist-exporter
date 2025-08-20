import csv
import re
import os

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials


def get_spotify_session(client_id: str, client_secret: str) -> spotipy.Spotify:
    """Authenticate with Spotify using client credentials."""
    client_credentials_manager = SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret
    )
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def extract_playlist_id(playlist_link: str) -> str:
    """Extract playlist ID from a Spotify playlist URL."""
    match = re.match(r"https://open\.spotify\.com/playlist/([a-zA-Z0-9]+)", playlist_link)
    if not match:
        raise ValueError("Expected format: https://open.spotify.com/playlist/<playlist_id>")
    return match.group(1)


def fetch_tracks(session: spotipy.Spotify, playlist_id: str) -> list:
    """Fetch all tracks from a given Spotify playlist."""
    tracks = []
    results = session.playlist_tracks(playlist_id)
    tracks.extend(results["items"])

    while results["next"]:
        results = session.next(results)
        tracks.extend(results["items"])

    print(f"Found {len(tracks)} tracks in playlist")
    return tracks


def write_csv(tracks: list, output_file: str) -> None:
    """Write track info (name, artist) to a CSV file."""
    with open(output_file, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=",", skipinitialspace=True)
        writer.writerow(["track", "artist"])  # header

        for track in tracks:
            name = track["track"]["name"]
            artists = ", ".join(artist["name"] for artist in track["track"]["artists"])
            writer.writerow([f"{name}", f" {artists}"])


if __name__ == "__main__":
    # Load environment variables
    load_dotenv()
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    PLAYLIST_LINK = os.getenv("PLAYLIST_LINK")
    OUTPUT_FILE = os.getenv("OUTPUT_FILE_NAME", "track_info.csv")

    if not CLIENT_ID or not CLIENT_SECRET or not PLAYLIST_LINK:
        raise EnvironmentError("Missing CLIENT_ID, CLIENT_SECRET, or PLAYLIST_LINK in .env file")

    # Run workflow
    session = get_spotify_session(CLIENT_ID, CLIENT_SECRET)
    playlist_id = extract_playlist_id(PLAYLIST_LINK)
    tracks = fetch_tracks(session, playlist_id)
    write_csv(tracks, OUTPUT_FILE)

    print(f"✅ Export complete! Saved to {OUTPUT_FILE}")
