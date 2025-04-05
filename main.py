from src.YT_video_link import link_downloader
from src.Text_summarization import modelling
downloader=link_downloader()
model=modelling()

video_url = input("Enter YouTube video link: ")
video_id = downloader.extract_video_id(video_url)
transcript=downloader.get_transcript(video_id)
summarized_text=model.model2(transcript)
print(summarized_text)