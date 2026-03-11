import os
import time
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

def enviar_mensagem_discord(mensagem: str, webhook_url: str) -> None:
    """Envia uma mensagem de texto para um canal do Discord via Webhook."""
    payload = {"content": mensagem}
    try:
        resposta = requests.post(webhook_url, json=payload)
        
        if resposta.status_code in [200, 204]:
            print("Alerta enviado ao Discord com sucesso.")
        else:
            print(f"Erro ao enviar alerta ao Discord. Status HTTP: {resposta.status_code}")
            
    except Exception as e:
        print(f"Falha de conexão com o Discord: {e}")

def verificar_preco(url: str, preco_desejado: float, webhook_url: str) -> None:
    """Faz o scraping da página do produto, extrai o preço e compara com o valor alvo."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        resposta = requests.get(url, headers=headers)
        
        if resposta.status_code != 200:
            print(f"Erro ao acessar {url}. Status HTTP: {resposta.status_code}")
            return

        soup = BeautifulSoup(resposta.text, 'html.parser')

        titulo_elemento = soup.find('h1', class_='ui-pdp-title')
        titulo = titulo_elemento.text.strip() if titulo_elemento else "Título desconhecido"

        preco_elemento = soup.find('span', class_='andes-money-amount__fraction')
        
        if preco_elemento:
            preco_atual = float(preco_elemento.text.replace('.', ''))
            
            print(f"Verificando: {titulo[:30]}... | Atual: R$ {preco_atual:.2f} | Alvo: R$ {preco_desejado:.2f}")

            if preco_atual <= preco_desejado:
                mensagem_alerta = (
                    f"**ALERTA DE QUEDA DE PREÇO**\n\n"
                    f"**Produto:** {titulo}\n"
                    f"**Preço Atual:** R$ {preco_atual:.2f}\n"
                    f"**Seu Alvo:** R$ {preco_desejado:.2f}\n\n"
                    f"[Link para compra](<{url}>)" 
                )
                enviar_mensagem_discord(mensagem_alerta, webhook_url)
        else:
            print(f"Preço não encontrado na página: {url}")

    except Exception as e:
        print(f"Erro no processamento da URL {url}: {e}")

# ==========================================
# Configurações de Ambiente e Dados
# ==========================================

MEU_WEBHOOK = os.getenv("WEBHOOK_DISCORD")

produtos_monitorados = [
    {
        "url": "https://produto.mercadolivre.com.br/MLB-6191775714-xiaomi-poco-c85-256gb-16gb-ram-lancamento-2026-brinde-top1-_JM",
        "preco_alvo": 3000.00
    },
    {
        "url": "https://www.mercadolivre.com.br/placa-me-dell-inspiron-15r-5537-3537-c-i7-4500u-180ghz-verde/p/MLB63136188?pdp_filters=item_id:MLB4404881757#is_advertising=true&searchVariation=MLB63136188&backend_model=search-backend&position=1&search_layout=grid&type=pad&tracking_id=7771344e-27a8-4832-8b4a-2b401a502db8&ad_domain=VQCATCORE_LST&ad_position=1&ad_click_id=NjQwODY5N2ItZjQ2Zi00MzE2LWJmOTctMzg2ZGM5YmU3ZjFh",
        "preco_alvo": 2000.00
    }
]

# ==========================================
# Execução Principal
# ==========================================

if __name__ == "__main__":
    print("Iniciando monitoramento de preços...\n")

    for produto in produtos_monitorados:
        verificar_preco(produto["url"], produto["preco_alvo"], MEU_WEBHOOK)
        
        # Delay entre requisições para evitar rate limiting do servidor
        time.sleep(2) 
        
    print("\nCiclo de verificação finalizado.")