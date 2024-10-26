import os
from enum import Enum


class Mediatype(Enum):
    PHOTO = "photo"
    VIDEO = "video"
    AUDIO = "audio"
    def __str__(self):
        return self.value


class MediafileExceptionBadExt(Exception):
    pass


class MediaFile:
    def __init__(self, filename: str, base: str, ext: str, mediatype: Mediatype):
        self._filename = filename
        self._base = base
        self._ext = ext
        self._mediatype = mediatype
        self._loaded = False
        self._filedata = None

    def __str__(self):
        loaded_str = "loaded" if self._loaded else "not loaded"
        return f"{self._filename} ({loaded_str}): {self._mediatype}"

    @staticmethod
    def getMediaFile(filename: str):
        base, ext = os.path.splitext(filename)
        mediafile = None
        if ext == ".jpeg":
            mediafile = MediaFilePhoto(filename, base, ext)
        if ext == ".mp4":
            mediafile = MediaFileVideo(filename, base, ext)
        if ext == ".mp3":
            mediafile = MediaFileAudio(filename, base, ext)

        return mediafile

    def load(self):
        self._loaded = True
        # TODO: Загрузка файла
        # filedata = ...


class MediaFileVisual(MediaFile):
    def __init__(self, filename: str, base: str, ext: str, mediatype: Mediatype):
        super().__init__(filename, base, ext, mediatype)
        self._resolution = None
        self._aspectratio = None

    def __str__(self):
        return super().__str__() + f", resolution={self._resolution}, aspectratio={self._aspectratio}"

    @property
    def resolution(self):
        return self._resolution

    @property
    def aspectratio(self):
        return self._aspectratio


class MediaFilePhoto(MediaFileVisual):
    def __init__(self, filename: str, base: str, ext: str):
        super().__init__(filename, base, ext, Mediatype.PHOTO)
        self._creationdatetime = None

    def __str__(self):
        return super().__str__() + f", creationdatetime={self._creationdatetime}"

    def load(self):
        super().load()
        # TODO: определить с помощью  filedata параметры
        #self._creationdatetime = ...

    @property
    def creationdatetime(self):
        return self._creationdatetime

class MediaFileVideo(MediaFileVisual):
    def __init__(self, filename: str, base: str, ext: str):
        super().__init__(filename, base, ext, Mediatype.VIDEO)
        self._tracklength = None
        self._framerate = None
        self._bitrate = None

    def __str__(self):
        return super().__str__() + f", tracklength={self._tracklength}, framerate={self._framerate}, bitrate={self._bitrate}"

    def load(self):
        super().load()
        # TODO: определить с помощью  filedata параметры
        # resolution = ...
        # aspectratio = ...
        # framerate = ...
        # bitrate = ...

    @property
    def tracklength(self):
        return self._tracklength

    @property
    def framerate(self):
        return self._framerate

    @property
    def bitrate(self):
        return self._bitrate


class MediaFileAudio(MediaFile):
    def __init__(self, filename: str, base: str, ext: str):
        super().__init__(filename, base, ext, Mediatype.AUDIO)
        self._tracklength = None
        self._bitrate = None

    def __str__(self):
        return super().__str__() + f", tracklength={self._tracklength}, bitrate={self._bitrate}"

    def load(self):
        super().load()
        # TODO: определить с помощью filedata параметры
        #tracklength = ...
        #bitrate = ...

    @property
    def tracklength(self):
        return self._tracklength

    @property
    def bitrate(self):
        return self._bitrate


if __name__ == "__main__":
    md1 = MediaFile("file1.jpeg", "file1", "jpeg", Mediatype.PHOTO)
    print(md1)

    photofile1 = MediaFile.getMediaFile("file2.jpeg")
    photofile1.load()
    print(photofile1)

    videofile1 = MediaFile.getMediaFile("file3.mp4")
    videofile1.load()
    print(videofile1)
    print(videofile1.resolution)

    audiofile1 = MediaFile.getMediaFile("file4.mp3")
    audiofile1.load()
    print(audiofile1)
