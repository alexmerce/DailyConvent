import subprocess
from src import MT


def videoMerge(pageData):
    with open(MT.basePath.fileListPath, "w", encoding="utf-8") as f:
        for fileName in pageData.videoList:
            txtW = "file "+"'file:"+fileName+"'"+"\n"
            f.write(txtW)
    cmdStr = '{a.ffmpegPath} -f concat -safe 0 -i {a.fileListPath} -c copy {a.mergeName}'.format(a=pageData)
    print(cmdStr)

    out = subprocess.Popen(cmdStr,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0].decode("utf-8")
    return out



def videoConver(pageData):
    cmdStr = '{ffmpegPath}  -i {videoInput} -c:v copy -c:a copy -strict -2 {videoOut}'.format(**pageData)
    if MT.chek.checked == pageData['reCode']:
        cmdStr = '{ffmpegPath} -i {videoInput} -c:a {acodec} -c:v {vcodec} -strict -2 {videoOut}'.format(**pageData)
    print(cmdStr)
    out = subprocess.Popen(cmdStr, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0].decode("utf-8")
    return out


def audioConver(pageData):
    cmdStr = '{a.ffmpegPath} -i {a.audioInputPath} -ab {a.bps}  {a.audioOutPath}'.format(a =pageData)
    if(pageData.audioInputPath.endswith(".flac")):
        cmdStr  = '{a.ffmpegPath} -i {a.audioInputPath} -ab {a.bps} map_metadata 0 -id3v2_version 3 {a.audioOutPath}'.format(a=pageData)
    print(cmdStr)
    # son = subprocess.Popen(cmdStr,stdin=subprocess.PIPE, stdout=subprocess.PIPE,  universal_newlines=True,bufsize=1,env=env)
    out = subprocess.Popen(cmdStr, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0].decode("utf-8")
    print(out)
    return out

    # p = os.popen(cmdStr,"r")
    # for line in p.readlines():
    #     print('<>>>>>>>>>')
    #     print(line)


    # print('----------------------------------------------------------------')
    #
    # while True:
    #     print("<<<<<<<")
    #     print(p.communicate()[0])
    #     p.stdout.flush()


    # while True:
    #     print("<<<<<<<")
    #     for line in iter(p.stdout.readline, ''):
    #         strLine = str(line).rstrip()
    #         p.stdout.flush()
    #         print(">>> " + strLine)

    # for line in iter(p.stdout.readline()):
    #     print(line.rstrip())
    #     print('---------------------------------------------')

    # out = p.communicate()
    # if not out:
    #     return 0
    # else:
    #     print(out.strip())


    # while subprocess.Popen.poll(p) is None:
    #     stream = p.stdout.readline()
    #     print(stream)



    # fl = fcntl.fcntl(p.stdout.fileno(), fcntl.F_GETFL)
    # while True:
    #     if p.poll() is not None:
    #         if p.returncode:
    #             pass
    #         break
    #     try:
    #         out = os.read(p.stdout.fileno(), 1024)
    #         print(out)
    #     except Exception:
    #         pass
    # for line in p.stdout:
    #     print(line.rstrip())
    #     print('-------------------------')
    #     sys.stdout.flush()


def audioConver_batch(pageData):
    cmdStr = '{a.ffmpegPath} -i {a.aInPath} -ab {a.bps_2}  {a.aOutPath}'.format(a =pageData)
    if(pageData.audioInputPath.endswith(".flac")):
        cmdStr  = '{a.ffmpegPath} -i {a.aInPath} -ab {a.bps_2} map_metadata 0 -id3v2_version 3 {a.aOutPath}'.format(a=pageData)
    print(cmdStr)
    # son = subprocess.Popen(cmdStr,stdin=subprocess.PIPE, stdout=subprocess.PIPE,  universal_newlines=True,bufsize=1,env=env)
    out = subprocess.Popen(cmdStr, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0].decode('utf-8','ignore')
    return out




'''
# 开启进程
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1,preexec_fn=os.setsid)
# 关闭进程
proc.terminate()
proc.wait()
os.killpg(proc.pid, signal.SIGTERM) 
print("程序已关闭")

'''
