import moviepy.editor
video = moviepy.editor.VideoFileClip("F:\AAFAQ RASHID\VIDEOS\Hindi and Urdu Songs\kabir.mp4")
audio = video.audio
audio.write_audiofile("result.mp3")
