import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')

# Access the properties using the section and key name
runtime = config.get('environment', 'runtime')
url = config.get('remote.driver', 'url')
browser_name = config.get('remote.driver', 'browser.name')
browser_version = config.get('remote.driver', 'browser.version')
app_url = config.get('sd', 'app.url')
print(app_url)