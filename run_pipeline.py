# run_pipeline.py

from utils.transcript_fetcher import fetch_transcript
from agents.summary_agent import generate_summary
from agents.notes_agent import generate_notes

def main():
    print("Welcome to your YouTube Learning Agent!")
    url = input("Enter a YouTube video URL: ")

    print("\n Fetching transcript...")
    try:
        transcript = fetch_transcript(url)
    except Exception as e:
        print("Error fetching transcript:", e)
        return

    print("\nGenerating summary...")
    summary = generate_summary(transcript)
    print("\n Summary:\n", summary)

    print("\n Generating notes...")
    notes = generate_notes(transcript)
    print("\n Notes:\n", notes)

if __name__ == "__main__":
    main()
