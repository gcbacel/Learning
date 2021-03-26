#########################################################################################
##   Python function to split a video in n parts, each part with a different duration  ##
##   Author: Gunther Bacellar                                                          ##
##   Email: gcbacel@hotmail.com                                                        ##
#########################################################################################

from moviepy.editor import VideoFileClip

# split a video in n parts by different duration (in seconds). last_block = True includes the final block of the video
# Ex: split_video("video.mp4", 120, 240, 1200, last_block = True) splits video.mp4 in 3 parts from 120-240s, 240-1200s and 1200s-end of video
def split_video(video_file, *args, last_block = False):
    video_splits = list(args)
    if last_block:
        video_size = VideoFileClip(full_video).duration
        video_splits.append(video_size)
    for i in range(1, len(video_splits)):
        print(f"Starting to process {len(video_splits)-1} video(s)")
        print(f"Processing video part #{i}")
        clip = VideoFileClip(video_file).subclip(video_splits[i-1], video_splits[i])
        clip.write_videofile(f"video_part{i}.mp4", codec="libx264", temp_audiofile='tempaudio.m4a',
                             remove_temp=True, audio_codec='aac', logger=None)
    print(f"All {len(video_splits)-1} video(s) were created sucessfully")