import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("uname")._site_view_()
elif 'aarch' in arc:
	__import__("uname")._site_view_()
else:
	exit(f' device machine {arc}')
