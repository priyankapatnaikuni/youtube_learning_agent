# utils/transcript_fetcher.py

from youtube_transcript_api import YouTubeTranscriptApi
import re

def extract_video_id(url: str) -> str:
    """
    Extracts the video ID from a YouTube URL.
    Example: https://www.youtube.com/watch?v=abc123 → abc123
    """
    match = re.search(r"v=([^&]+)", url)
    return match.group(1) if match else url

def fetch_transcript(url: str) -> str:
    """
    Fetches the transcript for a YouTube video.
    Returns the full transcript as plain text.
    """
    video_id = extract_video_id(url)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = " ".join([entry['text'] for entry in transcript])
    return full_text