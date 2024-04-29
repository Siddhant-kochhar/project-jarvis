from youtube_transcript_api import YouTubeTranscriptApi
from src.openai_chat import get_response_from_openai


def get_transcript(youtube_url):
    video_id = youtube_url.split("v=")[-1]
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    # Try fetching the manual transcript
    try:
        transcript = transcript_list.find_manually_created_transcript()
        language_code = transcript.language_code  # Save the detected language
    except:
        # If no manual transcript is found, try fetching an auto-generated transcript in a supported language
        try:
            generated_transcripts = [trans for trans in transcript_list if trans.is_generated]
            transcript = generated_transcripts[0]
            language_code = transcript.language_code  # Save the detected language
        except:
            # If no auto-generated transcript is found, raise an exception
            raise Exception("No suitable transcript found.")

    full_transcript = " ".join([part['text'] for part in transcript.fetch()])
    return {"transcript": full_transcript, "language": language_code}  # Return both the transcript and detected language


def get_youtube_video_summary(youtube_url):
    transcript = get_transcript(youtube_url=youtube_url).get("transcript", "")
    prompt = "You are a high school teacher. You will be given a youtube transcript and you will have to identify the main concept discussed in it and prepare a well structured note for the student's reference."
    
    response = get_response_from_openai(prompt=prompt, question=transcript)
    return response.content

# print(get_youtube_video_summary(youtube_url="https://www.youtube.com/watch?v=l8mWvDUwOt4"))