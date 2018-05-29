import requests

email = ''
password = ''
url = 'https://wifi.sspbrno.cz/login.html'

login_data = {
    'os_username': email,
    'os_password': password,
    'login': 'Log In',
}
s = requests.session()
s.post(url, login_data)