#----------------------------------------------------------------------------------------
# This python script allows you to downlaod Youtube video. 
# Requirement: Your machine should have Python3, pip, & pytube.
# OR
#  Go to https://pypi.org/project/pytube/#files & download "Source Distribution",    keep this file "YT_Video_CLI.py" into downloaded folder.
# Open terminal in same folder and run cmd "python3 YT_Video_CLI.py"
#----------------------------------------------------------------------------------------

from pytube import YouTube, Stream, Playlist

 

def video_downloader(video_url):
    # passing the video url and progress_callback to the YouTube object
    my_video = YouTube(video_url)
    # downloading the video in high resolution
    my_video.streams.get_highest_resolution().download()

    #my_video.streams.get_highest_resolution().download(output_path="/home/aaeuu156/Desktop", filename="filename")


    size = my_video.streams.get_highest_resolution().filesize_mb

    print("len:", my_video.length)
    print("size:",size)
    print("des",my_video.description)

    # return the video title
    return my_video.title

try:

    YT_VideoOrPlaylist = input('Enter P for Playlist OR V for Video: ')

    if YT_VideoOrPlaylist == 'P':

        youtube_playlist_link = input('Enter the YouTube Playlist link:')
        playlist = Playlist(youtube_playlist_link)


        a=0
        print(f'Downloading: {playlist.title}')
        #Downloading: Python Tutorial for Beginers (For Absolute Beginners)
        for video in playlist.videos:
            #print("-----------------------------------------------------------")
            #print(video.streams.get_by_resolution("1080p"))
            #print(video.streams.get_highest_resolution())

            a = a+1
            #print(video.streams.last())
            #print(video.streams.first())

            print(a,'-----------------------------------------------------------')

            print(video.title)


            strng1 = str(a)
            strng2 = str(". ")
            strng3 = video.title
            print ("Heloooooooooooooooo")
            filename= strng1 + strng2 + strng3
            
            print(filename)
            output_path="/home/aaeuu156/Desktop/Study/Lecture/1. C++ College Wallah"
            print(output_path)
            video.streams.get_highest_resolution().download(output_path, filename)

            print("Downloaded successfully in Home Dir ------------------------------------------")

        print("-----------------------------------------Downloaded successfully------------------------------------------")

    elif YT_VideoOrPlaylist == 'V':
        # getting the url from the user
        youtube_link = input('Enter the YouTube Video link:')
        print(f'Downloading your Video, please wait.......')
    
        # passing the url to the function
        video = video_downloader(youtube_link)
        # printing the video title
        print(f'"{video}" downloaded successfully!!')

    else:
      print("Please choose valid Option next time.")


except:
    print(f'Failed to download video, Invalid link')
