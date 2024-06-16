import sys
import re

import os
from enum import Enum

sys.path.append(os.getcwd())
# import fileUtils



datePatterns = [r'\[[\d]{2}:[\d]{2}.[\d]{2}\]',  # [mm:s.ss]
                r'[\d]+:[\d]+:[\d]+,[\d]+',      # 00:00:25,800 --> 00:00:27,370]  #0:01:02.23,
                r'[\d]+:[\d]{2}:[\d]{2}.[\d]{2}' #00:00:02.123
                ]

# [lrc,srt,ssa]
subtitlePatterns = [ '(?<=\]).*(?=\n|\[)',
                     r'.*(?=\n\n)',
                     r'(?<=Effect,).*']

class subtitleType(Enum):
    srt = 'srt'
    lrc = 'lrc'
    ssa = 'ssa'
    vtt = 'vtt'

linePattern = {subtitleType.lrc.value: r'\[.*\].*\n\[.*\]( |\n)',
               subtitleType.srt.value: r'([\d]*)\n.+-->.+\n.+\n\n',
               subtitleType.vtt.value: r'([\d]*)\n.+-->.+\n.+\n\n',
               subtitleType.ssa.value: r'Dialogue.*'}

def subtitle_convert(pageData):
    outPath = None
    for item in pageData.subitile_list:
        if os.path.isfile(item):
            data = getData(item)
            if outPath == None: outPath = item[0:item.rindex('.') + 1] + subtitleType.lrc.value
            changeToSRT(data,outPath)
        elif os.path.isdir(item):
            for p1 in os.listdir(item):
                if p1.endswith('.vtt'):
                    outPtah = item + '/' + p1[:p1.rindex('.')] + '.lrc'
                    data = getData(os.path.join(item, p1))
                    changeToSRT(data, outPtah)
                    print(p1)





def getData(source):
    fileFormat = list(filter(lambda x: source.endswith(x), linePattern.keys()))
    if (len(fileFormat) == 0): raise Exception("暂不支持源格式")
    fileFormat = fileFormat[0]
    sourceTxt = ''
    with open(source, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            sourceTxt = sourceTxt + line

    # 获取[时间-字幕-时间]等整行
    pattern = linePattern[fileFormat]

    result = []
    lineNo = 0
    lines = re.finditer(pattern, sourceTxt)
    lineData = None
    tempLine = re.search(pattern, sourceTxt).group()
    # 获取日期格式
    subPattern = datepattern = lineDate = None
    if(re.search(datePatterns[0],tempLine)):
        lineDate = lineDateA
        datepattern = 0
    if (re.search(datePatterns[1],tempLine)):
        lineDate = lineDateB
        datepattern = 1
    if(re.search(datePatterns[2],tempLine)):
        datepattern = 2
        lineDate = lineDateC
    for subtitlePattern in subtitlePatterns:
        if (re.search(subtitlePattern, tempLine)):
            subPattern = subtitlePattern
    for line in lines:
        lineNo += 1
        # 封装为行
        line = Line(line.group(), lineNo,lineDate,datepattern,subPattern)
        result.append(line)
    return result


def changeToSRT(subtitles, outPath=None):
    # lineDate.targetType = subtitleType.srt
    with open(outPath, 'w+', encoding='utf-8') as f:
        for line in subtitles:
            line.start = '[{:02d}:{:02d}:{:02d}.{:02d}]'.format(*line.start)
            line.end = '[{:02d}:{:02d}:{:02d}.{:02d}]'.format(*line.end)
            str = '{line.lineNo}\n{line.start} --> {line.end}\n{line.subtitle}\n\n'.format(line=line)
            f.write(str)


def changeToLRC(subtitles, outPath=None):
    # lineDate.targetType = subtitleType.lrc


    with open(outPath, 'w+', encoding='utf-8') as f:

        for line in subtitles:

            line.start = '[{1:02d}:{2:02d}.{3:02d}]'.format(*line.start)
            line.end = '[{1:02d}:{2:02d}.{3:02d}]'.format(*line.end)
            str = '{line.start}{line.subtitle}\n{line.end}\n'.format(line=line)
            f.write(str)


class Line():
    def __init__(self,lineText,lineNo,lineDate,datepattern,subPattern):
        dates = re.findall(datePatterns[datepattern],lineText)
        self.start = lineDate(dates[0])
        self.end = lineDate(dates[1])
        self.subtitle= re.search(subPattern,lineText).group()
        self.lineNo = lineNo


def lineDateA(lineText):
    hour = 0
    minute = int(re.search('(?<=\[)[\d]{2}', lineText).group())
    secone = int(re.search('(?<=:)[\d]{2}', lineText).group())
    ms = int(re.search('[\d]*(?=\])', lineText).group())
    return [hour,minute,secone,ms]
def lineDateB(lineText):
    hour = int(re.search('[\d].+?(?=:)',lineText).group())
    minute = int(re.search('(?<=:)[\d]+(?=:)', lineText).group())
    secone = int(re.search('[\d]+(?=,)', lineText).group())
    ms = int(re.search('(?<=,)[\d]+', lineText).group())
    return [hour,minute,secone,ms]
def lineDateC(lineText):
    hour = int(re.search('[\d]+(?=:)', lineText).group())
    minute = int(re.search('(?<=:)[\d]+(?=:)', lineText).group())
    secone = int(re.search('[\d]+(?=\.)', lineText).group())
    ms = int(re.search('(?<=\.)[\d]+', lineText).group())
    return [hour,minute,secone,ms]

