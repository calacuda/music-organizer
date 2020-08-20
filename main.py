"""
song metadata downloader.py

this script will loop over all the music files in a directory and find meta
data for them.

By: Calacuda | MIT Licence
"""


from os import system
from sys import argv
import eyed3


def edit_file(metadata):
    """
    edits the new audio file to add the meta data.
    """
    pass


def get_meta(album, artist):
    """
    returns the metadata for ALBUM by ARTIST.
    """
    pass


def get_album(url):
    """
    return the album and artist of the song.
    """
    album, artist = " "
    return album, artist


def give_metadata(song):
    """
    handles getting album and artist, metadata, and editing the file
    """
    album, artist = song  # the stuff to get album and artist info from the song file
    metadata = get_meta(album, artist)
    edit_file(metadata)


def main():
    give_metadata()
    

if __name__ == "__main__":
    main()
