all:
	echo "all"

install:
	cp src/YouTubeFFMPEG.svg /usr/share/pixmaps/
	cp src/youtube-ffmpeg.server /usr/lib/bonobo/servers/
	cp src/youtube-ffmpeg.py /usr/local/bin/
    chmod a+x /usr/local/bin/youtube-ffmpeg.py
