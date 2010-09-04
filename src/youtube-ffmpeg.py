#!/usr/bin/env python

import pygtk
pygtk.require('2.0')

import gtk
import gnomeapplet
import gobject
import sys
import logging
import commands
import os
import pynotify
from threading import Thread

# DOCS 
# http://unpythonic.blogspot.com/2007/08/using-threads-in-pygtk.html

class Sample_Applet(gnomeapplet.Applet):
    title = 'YouTube FFMPEG Applet'
    version = '0.1'
    image_file = '/usr/share/pixmaps/YouTubeFFMPEG.svg'
    TARGET_TYPE_TEXT = 80
    toButton = [( "text/plain", 0, TARGET_TYPE_TEXT )]
    _savePath = "%s/VideosYouTube" % os.getenv('HOME')

    logging.basicConfig(level=logging.DEBUG)

    def __init__(self, applet, iid):
        logging.debug('__init__')

        gtk.gdk.threads_init()	

        pynotify.init("YouTube")
        # save the applet object
        self.applet = applet

        # determine the size to draw the icon
        size = self.applet.get_size() - 2
        pixbuf = gtk.gdk.pixbuf_new_from_file_at_size(self.image_file, size, size)
        image = gtk.Image()
        image.set_from_pixbuf(pixbuf)

        # set up the applet tooltip
        tooltips = gtk.Tooltips()
        tooltips.set_tip(image, self.title)

        # set up the applet itself
        self.applet.add(image)
        self.applet.connect('button-press-event', self.button_press)
        self.applet.connect('change-size', self.change_size, image)
        self.applet.connect('change-background', self.change_background)
        self.applet.show_all()
        self.applet.connect('drag_drop', self.drop_cb)
        self.applet.drag_dest_set(gtk.DEST_DEFAULT_MOTION | gtk.DEST_DEFAULT_HIGHLIGHT | gtk.DEST_DEFAULT_DROP, self.toButton, gtk.gdk.ACTION_COPY)
        self.applet.connect('drag_data_received', self.got_data_cb)

        if not os.path.isdir(self._savePath):
            os.makedirs(self._savePath)


    def got_data_cb(self, wid, context, x, y, data, info, time):
      # Got data.
      print data.get_text()
      self._downloadFileThreaded(data.get_text())
      context.finish(True, False, time)

    def _downloadFileThreaded(self, url):
      Thread(target=self._downloadFile, args=(url,)).start()


    def _informDownload(self, url):
      title = commands.getoutput("/usr/local/bin/youtube-dlf -e '%s'" % url)
      icone = 'dialog-warning'
      title = "download"
      msg = "download do video: <b>" + title + "</b> url::  " + url + " - iniciado"

      n = pynotify.Notification(title, msg, icone)
      n.show()

    def _downloadFile(self, url):
      self._informDownload(url)
      command = "cd %s/; /usr/local/bin/youtube-dlf -b '%s' &" % (self._savePath, url)
      os.system(command)

    def drop_cb(self, widget, context, selection, targetType, time):
      pass

    # when the applet window changes size
    def change_size(self, applet, new_size, image):
        logging.debug('change_size')
        self.do_image(self.image_file, image)

    # when the theme background changes
    def change_background(self, applet, type, color, pixmap):
        logging.debug('change_background')

        applet.set_style(None)
        applet.modify_style(gtk.RcStyle())

        if type == gnomeapplet.COLOR_BACKGROUND:
            applet.modify_bg(gtk.STATE_NORMAL, color)
        elif type == gnomeapplet.PIXMAP_BACKGROUND:
            applet.get_style().bg_pixmap[gtk.STATE_NORMAL] = pixmap

    # when the applet is clicked
    def button_press(self, button, event):
        logging.debug('button_press')

        # left mouse button
        if event.button == 1:
            logging.debug('show guests')

        # right mouse button
        elif event.button == 2:
            logging.debug('show options')

# function to run/register the class
def Sample_factory(applet, iid):
    Sample_Applet(applet, iid)
    return gtk.TRUE

if __name__ == '__main__':
    gobject.type_register(Sample_Applet)

    # Use parameter "run-in-window" to just run as a regular
    # application for debugging purposes
    if len(sys.argv) > 1 and sys.argv[1] == 'run-in-window':
        # create the main window
        main_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        main_window.set_title(Sample_Applet.title)
        main_window.connect('destroy', gtk.main_quit)
        main_window.set_default_size(36, 36)

        # create the applet and run in the window
        app = gnomeapplet.Applet()
        Sample_factory(app, None)
        app.reparent(main_window)

        # run it
        main_window.show_all()
        gtk.main()
    else:
        # create as an applet
        gnomeapplet.bonobo_factory('OAFIID:GNOME_YouTubeFfMpeg_Factory', Sample_Applet.__gtype__, Sample_Applet.title, Sample_Applet.version, Sample_factory)
