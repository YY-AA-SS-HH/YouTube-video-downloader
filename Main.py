import streamlit as st
import pytube


st.title("YouTube Video Downloader")

st.text("you can download youtube thumbnails too")

thumbnail_url = st.text_input("Enter Youtube thumbnail url")


def download_thumbnail(url):
    try:
        yt = pytube.YouTube(url)

        thumbnail = yt.thumbnail_url

        return thumbnail
    

    except Exception as e:
        return f"Error: {str(e)}"


if st.button("Download Thumbnail"):
    if thumbnail_url:
        
        t = download_thumbnail(thumbnail_url)
        
        st.image(t,caption="Youtube Thumbnail")     
    else:
        
        st.text("Please enter a valid URL")


video_url = st.text_input("Enter YouTube Video URL:")

def download_video(url):
    try:

        yt = pytube.YouTube(url)
        
        
        stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
        
        
        stream.download(output_path="Downloads")
        
        
        return f"Video downloaded successfully! Check the 'downloads' folder."
        
    except Exception as e:
        
        return f"Error: {str(e)}"


if st.button("Download"):
    
    if video_url:
        st.text(download_video(video_url))
        
    else:
        st.text("Please enter a valid YouTube video URL.")



st.text("Note: The downloaded video will be saved in the 'downloads' folder.")


