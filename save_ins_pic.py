#coding:utf-8
import urllib2
import re

def save_image():
    promt = raw_input("Do you want to save it?")
    num = 0
    if promt == "yes":
        for i in range(1, len(result)):
            response = urllib2.urlopen(result[i])
            source = response.read()
            with open("%d.jpg" % num, "wb") as f:
                f.write(source)
            num += 1
        print "All Done!"
        print "%d Pictures have been saved!" % num
    else:
        print "Goodbye!"

def save_video():
    promt = raw_input("Do you want to save the video?")
    num = 1
    if promt == "yes":
        response = urllib2.urlopen(result_video[0])
        source = response.read()
        with open("%d.mp4" % num, "wb") as f:
            f.write(source)
        print "All Done!"

    else:
        print "Goodbye!"

promt = raw_input("Please type the link:")
url = promt
request = urllib2.Request(url)
response = urllib2.urlopen(request)
source = response.read().decode('utf-8')
pattern = re.compile('"config_width":750,"config_height":\d+},{"src":"(.*?)","config_width":1080', re.S)
pattern_video = re.compile('"video_url":"(.*?)"')
result = re.findall(pattern, source)
if len(result) > 1:
    for i in range(1, len(result)):
        print result[i]
    print "%d Pictures found!" % (len(result)-1)
    save_image()
else:
    print result[0]
    print "1 Picture Found!"
    promt = raw_input("Do you want to save it?")
    if promt == "yes":
        response = urllib2.urlopen(result[0])
        source = response.read()
        with open("1.jpg", "wb") as f:
            f.write(source)
        print "Picture saved!"

result_video = re.findall(pattern_video, source)
if result_video != []:
    print "Video found!"
    print result_video[0]
    save_video()





