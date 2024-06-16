from enum import Enum
from baseDir import appPath


class msg():
    mergeName = "合并"
    fileSaveSuccess = "文件保存成功!"
    fileNotExist = '文件路径不存在!'
    haveChange = '转换已存在!'
    pathError = '文件路径不合法,请去除路径中的特殊字符!'

class fileFormat():
    videoFormat = "(*.mp4 *.mkv *.rmvb *.ts *.avi *.wmv *.mpeg *.m4v *.mov *.asf *.asx *.flv *.f4v *.3pg *.vob *.FLV *.MOV)"
    docFormat = "(*.doc *.md *.pdf)"
    audioFormat = "(*.wav *.mp3 *.wma)"
    subtitleFormat = "(*.srt *.lrc *.ssa *.vtt)"

class basePath():
    app = appPath()
    fileListPath = app+"./lib/fileList.txt"
    ffmpegPath = app+".\\lib\\ffmpeg.exe"
    icon = app+"./img/aet1v-zqt6v-001.ico"

class logType(Enum):
    warning = 1
    endIng = 2
    error = 3

class changeType(Enum):
    audioChange = 1
    audioChange_batch = 2

class chek():
    noCheck = 0
    checked = 2