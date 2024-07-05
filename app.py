import requests
from flask import Flask, request

app = Flask(__name__)

    # URL do webhook do Discord
discord_webhook_url = "https://discord.com/api/webhooks/1258292575853477908/2Bn-WBXZG05OvmSuYGeahY60cRpXBZkhDZhcqHcGad0pUqeDBkTEMsxdtBVo66PX44vv"

@app.route("/")
def index():
        user_ip = request.remote_addr
        message = f"Novo acesso detectado! IP: {user_ip}"
        send_discord_message(message)
        return "IP enviado para o Discord!"

def send_discord_message(message):
        payload = {"content": message}
        headers = {"Content-Type": "application/json"}
        response = requests.post(discord_webhook_url, json=payload, headers=headers)
        if response.status_code == 204:
            print("Mensagem enviada com sucesso!")
        else:
            print("Erro ao enviar mensagem:", response.text)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
