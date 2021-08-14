import requests
from pprint import pprint

url = "https://yandex.ru/dev/disk/poligon/"

TOKEN =
# HOST: https://cloud-api.yandex.net:443

API_BASE_URL = "https://cloud-api.yandex.net/"

headers = {
    'accept': 'application/json',
    'Authorization': f'OAuth {TOKEN}'
}
file_path = input("Введите  полный путь к файлу:")
name_file = input('Введите путь к папке через /  название файла:')

class YaUploader:
    def __init__(self, TOKEN: str):
        self.TOKEN = TOKEN

    def upload(self, file_path: str):
        r = requests.get(API_BASE_URL + "v1/disk/resources/upload", params={"path": name_file}, headers=headers)
        pprint(r.json())
        pprint(r.status_code)
        upload_url = r.json()['href']
        r = requests.put(upload_url, headers=headers, files={'file': open(file_path, 'rb')})


if __name__ == '__main__':
    path_to_file = file_path
    token =
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

