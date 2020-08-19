"""
song metadata downloader.py

This scripts is a wrapper for youtube_dl, which downloads youtube videos.The
scripts adds the functionality of editing the metadata of the downloaded file.

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


def metadata():
    """
    handles getting album and artist, metadata, and editing the file
    """
    if argv[-1][0:8] not in {"https:/", "http://"}:
        url = [arg for arg in argv if arg[0:8] in {"https:/", "http://"}][0]
    else:
        url = argv[-1]
    album, artist = get_album(url)
    metadata = get_meta(album, artist)
    edit_file(metadata)


def argument_remaker(args):
    """
    turns the sys.argv junk back into what was typed at the terminal.
    """
    if "--extract-audio" in args:
        music = True
    else:
        music = False
    return " ".join(args[1:]), music


def main():
    cmd_args, music = argument_remaker(argv)
    system(f"youtube_dl {cmd_args}")
    if music:
        metadata()


if __name__ == "__main__":
    main()
