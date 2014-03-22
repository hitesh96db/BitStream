

def main():
	return dict()

def info_extractor():
	import os
	import json

	url = request.vars["url"]
	d = ["title","thumbnail","duration","quality"]
	command = "youtube-dl -o '%(title)s.%(ext)s' --get-thumbnail --get-title --get-duration --get-format "+url
	info = os.popen(command).read()[:-1].split("\n")
	info_extracted = zip(d,info)
	jsonob = json.dumps(dict(info_extracted))
	return jsonob

def chkdir():
	import os

	path = request.vars["path"]
	command = "cd "+path
	k = os.system(command)
	return k

def autocomplete():

	import os
	
	path = request.vars["path"]
	search = path.split("/")[-1]
	path = reduce(lambda x,y:x+y,map(lambda x: "/"+x,path.split("/")[1:-1]))
	path +="/"
	os.chdir(path)
	list = os.popen("ls").read()[:-1]
	if search is not "":
        	t = os.popen("ls --ignore='*.*' | grep '^"+search+"'").read()[:-1]	
		return str(t.split("\n"))
	else:
		return str(os.popen("ls --ignore='*.*' | grep '^"+search+"'").read()[:-1].split("\n"))
	
def real_download():

	import os
	url = request.vars["url"]
        ext = request.vars["ext"]
        path = request.vars["path"]
	os.chdir(path)

	if ext == "mp4" or ext == "flv":
		command = "youtube-dl -o '%(title)s.%(ext)s' -f "+ext+" "+url
		result = os.popen(command).read()[:-1]
		if "100%" in result or "downloaded" in result:
			return "success"
		else:
			return "failure"
	else:
		
		command = "youtube-dl -o '%(title)s.%(ext)s' -x --audio-format "+ext+" "+url
		result = os.popen(command).read()[:-1]
		if "100%" in result or "downloaded" in result:
			return "success"
		else:	
			return "failure"

