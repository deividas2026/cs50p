extensions = [
	{"name": ".gif", "mime-type": "image/gif"},
	{"name": ".jpg", "mime-type": "image/jpeg"},
	{"name": ".jpeg", "mime-type": "image/jpeg"},
	{"name": ".png", "mime-type": "image/png"},
	{"name": ".pdf", "mime-type": "application/pdf"},
	{"name": ".txt", "mime-type": "text/plain"},
	{"name": ".zip", "mime-type": "application/zip"},
]

filename = input("File name: ").strip().lower()

for extension in extensions:
	if filename.endswith(extension["name"]):
		print(extension["mime-type"])
		break
else:
	print("application/octet-stream")

