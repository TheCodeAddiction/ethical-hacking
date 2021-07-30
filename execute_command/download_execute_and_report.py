import requests
def downloadFile(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1] #get's the name of the file
    with open(file_name,"wb") as out_file:
        out_file.write(get_response)

