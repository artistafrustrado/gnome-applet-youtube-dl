#!/bin/bash

wget -O /usr/lib/bonobo/servers/youtube-ffmpeg.server  http://github.com/artistafrustrado/gnome-applet-youtube-dl/raw/master/src/youtube-ffmpeg.server
wget -O /usr/local/bin/youtube-ffmpeg.py  http://github.com/artistafrustrado/gnome-applet-youtube-dl/raw/master/src/youtube-ffmpeg.py
wget -O /usr/share/pixmaps/YouTubeFFMPEG.svg  http://github.com/artistafrustrado/gnome-applet-youtube-dl/raw/master/src/YouTubeFFMPEG.svg
chmod a+x /usr/local/bin/youtube-ffmpeg.py
