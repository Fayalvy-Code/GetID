# Faya Harvard lvy
# https://www.facebook.com/Faya.codeOfficial

import os, sys, requests, json

class GetID:
  
  def __init__(self) -> None:
      self.ses = requests.Session()
      self.url = 'https://www.facebook.com/Faya.codeOfficial'
  
  def PasteUid(self):
      os.system('clear' if sys.platform.lower() == 'linux' else 'cls')
      print(f' [ Masukan Link Profil Facebook Atau Halaman, Link Postingan ]\n      [ {self.url} ]')
      self.Type = input('\n # @FayaLvy_> ') ; self.FindID(self.Type)
  
  def FindID(self, typeUser):
      try:
          url = self.ses.get('https://id.traodoisub.com/').text
          cookies = {
             'cf_clearance': 'ARotwUlnlZsrT7nGTbmc4YoU7T_2RGUZRYBbQCwIn.s-1717953863-1.0.1.1-yREA3jhlwZJAKA3TRW0T4DeKay4lZd4QLIx03ML4UBF247AgftUSzF1XmWKrQMmoa9Svh5K.2bikNHHzLS1XmA'
          }
          headers = {
             'authority': 'id.traodoisub.com',
             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
             'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
             'cache-control': 'max-age=0',
             'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
             'sec-ch-ua-arch': '""',
             'sec-ch-ua-bitness': '""',
             'sec-ch-ua-full-version': '"124.0.6327.4"',
             'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
             'sec-ch-ua-mobile': '?1',
             'sec-ch-ua-model': '"CPH2127"',
             'sec-ch-ua-platform': '"Android"',
             'sec-ch-ua-platform-version': '"12.0.0"',
             'sec-fetch-dest': 'document',
             'sec-fetch-mode': 'navigate',
             'sec-fetch-site': 'none',
             'sec-fetch-user': '?1',
             'upgrade-insecure-requests': '1',
             'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'
          }
          data = {
             'link':typeUser
          }
          response = self.ses.post('https://id.traodoisub.com/api.php', headers = headers, data = data).json()
          if "success" in response:
             print(f'\n # UserID : {response["id"]}\n # Code   : {response["code"]}\n # Status : success\n # UserAgn: {headers["user-agent"]} \n\n [ Jangan Lupa Follow & Berikan Bintang 🌟 ]') ; sys.exit()
          else:
             print('\n [ Gagal Mengambil ID ]') ; sys.exit()
      except Exception as e:
          sys.exit(e)

GetID().PasteUid()          
