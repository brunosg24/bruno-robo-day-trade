<div align="center">

<img src="assets/cover.svg" alt="Bruno Robô Day Trade — projeto experimental" width="100%">

# Bruno Robô Day Trade
### Estudos de automação e análise de mercado

Projeto experimental em Python, com uma estrutura inicial de API utilizando FastAPI. A ideia é explorar conceitos de análise de dados e automação aplicados ao mercado financeiro.

[![Acessar repositório](https://img.shields.io/badge/REPOSITÓRIO-GitHub-181717?style=for-the-badge&logo=github)](https://github.com/brunosg24/bruno-robo-day-trade)

</div>

---

## ✦ Sobre o projeto
O repositório está em fase inicial. Atualmente contém uma aplicação FastAPI mínima, arquivo de configuração e lista inicial de dependências. Recursos de análise técnica, modelos preditivos e gestão de risco são possibilidades de evolução, não funcionalidades implementadas nesta versão.

## Estrutura atual
```text
bruno-robo-day-trade/
├── backend/
│   ├── app.py
│   ├── config.py
│   └── requirements.txt
├── .env.example
└── README.md
```

## Tecnologias e estudos
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)

- Python e FastAPI.
- Fundamentos de análise de dados.
- Estudos de visão computacional e machine learning.

## Executar localmente
```bash
git clone https://github.com/brunosg24/bruno-robo-day-trade.git
cd bruno-robo-day-trade
python -m venv .venv
```

Ative o ambiente virtual e instale as dependências:
```bash
# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

pip install -r backend/requirements.txt
uvicorn backend.app:app --reload
```

A API inicial fica disponível em http://127.0.0.1:8000.

## Atenção: configuração e segurança
O arquivo backend/config.py contém valores de exemplo e configurações de desenvolvimento. Antes de qualquer uso real, mova credenciais para variáveis de ambiente, substitua segredos de exemplo, desative o modo DEBUG e revise a configuração de segurança. Nunca publique chaves ou senhas reais.

## Próximos passos
- Organizar configurações por ambiente.
- Criar testes automatizados para a API.
- Definir e documentar os dados de entrada e saída.
- Implementar módulos de análise de forma incremental.
- Avaliar modelos com dados históricos e metodologia reproduzível.

## Status
**Em desenvolvimento — estrutura inicial.** Este projeto não fornece sinais de compra ou venda e não deve ser utilizado como ferramenta de decisão financeira.

<div align="center">
Desenvolvido por **Bruno** · [GitHub](https://github.com/brunosg24)
</div>
