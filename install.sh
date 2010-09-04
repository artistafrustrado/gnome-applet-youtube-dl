#!/bin/bash

wget -O /usr/lib/bonobo/servers/youtube-ffmpeg.server  http://github.com/artistafrustrado/gnome-applet-youtube-dl/raw/master/src/youtube-ffmpeg.server
wget -O /usr/local/bin/youtube-ffmpeg.py  http://github.com/artistafrustrado/gnome-applet-youtube-dl/raw/master/src/youtube-ffmpeg.py
wget -O /usr/share/pixmaps/YouTubeFFMPEG.svg  http://github.com/artistafrustrado/gnome-applet-youtube-dl/raw/master/src/YouTubeFFMPEG.svg
wget -O /usr/share/pixmaps/YouTubeFFMPEG.png  http://github.com/artistafrustrado/gnome-applet-youtube-dl/raw/master/src/YouTubeFFMPEG.svg
wget -O /usr/local/bin/youtube-dlf http://bitbucket.org/rg3/youtube-dl/raw/6bb800654cbb/youtube-dl
chmod a+x /usr/local/bin/youtube-ffmpeg.py
chmod a+x /usr/local/bin/youtube-dlf

mkdir $HOME/VideosYouTube
