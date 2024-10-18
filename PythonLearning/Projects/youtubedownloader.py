from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    # youtubeObject = youtubeObject.streams.filter(res="720p") # gets a 720p resolution
    try:
        youtubeObject.download()
        # Specify a download path
        # youtubeObject.download(output_path='your_directory_path_here')
        print("Download is completed successfully")
    except:
        print("An error has occured while downloading")
    
    print("Download is completed successfully")

link = input("Enter the Youtube video URL: ")
Download(link)