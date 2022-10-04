import requests

class user():
    
  def __init__(self, username, password):
      self.username = username
      self.password = password
      self.token = requests.post(f'https://api.tigitaal.nl/auth/login/{username}/{password}').json()["data"]
    
  def reload():
      response = requests.get(f'https://api.tigitaal.nl/user/reload/{self.token}')
      return response.json()

  def reloadadvanced():
      response = requests.get(f'https://api.tigitaal.nl/user/reloadadvanced/{self.username}/{self.password}')
      return response.json()

  # Buggy/doesnt work
  def pfp(pfp):
      response = requests.post(f'https://api.tigitaal.nl/user/reload/{self.token}/{pfp}')
      return response.json()

  def nickname(nickname):
      response = requests.post(f'https://api.tigitaal.nl/user/nickname/{self.username}/{self.password}/{nickname}')
      return response.json()

  def mail(email):
      response = requests.post(f'https://api.tigitaal.nl/user/mail/{self.username}/{self.password}/{email}')
      return response.json()
  
  def aboutme(aboutme):
      response = requests.post(f'https://api.tigitaal.nl/user/aboutme/{self.username}/{self.password}/{aboutme}')
      return response.json()
