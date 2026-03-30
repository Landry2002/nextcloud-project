from webdav3.client import Client
import json

# Configuration WebDAV pour Nextcloud (avec HTTP)
options = {
    'webdav_hostname': 'http://192.168.11.110:8080/remote.php/dav/files/admin/',
    'webdav_login': 'admin',
    'webdav_password': 'Admin1234!'   # Remplacez par le vrai mot de passe
}

client = Client(options)

# Créer un fichier temporaire
data = {"timestamp": "2026-03-30", "value": "Upload via WebDAV"}
with open('/tmp/webdav_test.json', 'w') as f:
    json.dump(data, f)

# Upload du fichier
client.upload_sync(remote_path='webdav_test.json', local_path='/tmp/webdav_test.json')
print("Fichier uploadé avec succès")
