# 🛒 Rastreador de Preços Automático (Web Scraper)

Um script automatizado desenvolvido em Python para monitorar os preços de produtos no Mercado Livre. O sistema faz a extração de dados (Web Scraping), compara o valor atual com a meta de preço do usuário e envia notificações em tempo real através de um canal do Discord via Webhooks.

## 🚀 Funcionalidades

- **Monitoramento em Lote:** Capacidade de verificar múltiplos links de produtos em uma única execução.
- **Notificações no Discord:** Integração nativa com Webhooks do Discord para alertas imediatos.
- **Prevenção de Bloqueios:** Implementação de cabeçalhos de navegador (*User-Agent*) e intervalos (*delays*) para evitar restrições de *Rate Limit* pelos servidores do site.
- **Segurança de Credenciais:** Uso de variáveis de ambiente (`.env`) para manter URLs de Webhooks e chaves privadas seguras e fora do código fonte.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Requests:** Para realizar as requisições HTTP e consumir a API do Discord.
- **BeautifulSoup 4:** Para realizar o parsing e extração de dados do HTML estruturado.
- **Python-dotenv:** Para o gerenciamento seguro de variáveis de ambiente.

## ⚙️ Como Instalar e Configurar

Siga os passos abaixo para rodar o projeto localmente na sua máquina:

## 📞 Contatos e Redes

Projeto desenvolvido com foco em automação e integração de APIs. Se você gostou do projeto ou quer trocar uma ideia sobre Python, me chame nas redes:

- **GitHub:** [DeregL2](https://github.com/DeregL2)
- **LinkedIn:** [Seu Nome Aqui](https://www.linkedin.com/in/derick-maschio/)