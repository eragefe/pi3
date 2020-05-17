#! /usr/bin/env python
import time
from socket import error as socket_error
from mpd import MPDClient, MPDError, CommandError, ConnectionError

class MPDConnect(object):
    def __init__(self, host='localhost', port=6600):
        self._mpd_client = MPDClient()
        self._mpd_client.timeout = 10
        self._mpd_connected = False

        self._host = host
        self._port = port

    def connect(self):
        if not self._mpd_connected:
            try:
                self._mpd_client.ping()
            except(socket_error, ConnectionError):
                try:
                    self._mpd_client.connect(self._host, self._port)
                    self._mpd_connected = True
                except(socket_error, ConnectionError, CommandError):
                    self._mpd_connected = False

    def disconnect(self):
        self._mpd_client.close()
        self._mpd_client.disconnect()

    def spdif(self):
        self._mpd_client.clear()
        self._mpd_client.add("alsa://hw:0,1")
        self._mpd_client.play()

    def fetch(self):

        song_stats = self._mpd_client.status()
        state = song_stats['state']

        return({'state':state,})
def main():
  client = MPDConnect()
  client.connect()

  while True:

    info = client.fetch()
    state = info['state']

    if (state == 'stop'):
       print "spdif input connected"
       time.sleep(0.5)
       client.spdif()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
