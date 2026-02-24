# 🤖 Bruno Robô Day Trade - IA para Análise de Gráficos

Sistema automatizado de inteligência artificial para análise de gráficos financeiros com previsão probabilística de movimentos de mercado para day trade.

## 📋 Descrição

Um robô inteligente que:
- ✅ Recebe prints de gráficos (TradingView, MetaTrader, etc.)
- ✅ Analisa automaticamente com IA
- ✅ Identifica padrões técnicos
- ✅ Gera previsão probabilística do mercado
- ✅ Recomenda pontos de entrada, stop e alvo
- ✅ Calcula expectativa matemática
- ✅ Aprende com cada operação

## 🎯 Funcionalidades Principais

### 1️⃣ Análise de Imagens
- Upload de prints de gráficos
- Extração automática de indicadores
- Reconhecimento de padrões (triângulo, bandeira, rompimento)
- Identificação de suporte/resistência

### 2️⃣ Análise Técnica Automática
- **Tendência**: EMA 9, EMA 21, EMA 200
- **Momentum**: RSI, MACD
- **Volume**: Análise de volume institucional
- **Volatilidade**: ATR e desvio padrão

### 3️⃣ Motor de Previsão
- Modelo Bayesiano adaptativo
- Score multivariável com pesos estatísticos
- Probabilidade de continuação
- Nível de confiança

### 4️⃣ Recomendação Operacional
```
📈 PREVISÃO: ALTA (71% de probabilidade)
💰 Entrada: 128.450
🛑 Stop: 128.120
🎯 Alvo: 128.980
📊 R/R: 1:2.1
⚠️ Confiança: ALTA
```

### 5️⃣ Gestão de Risco
- Risco fixo por operação (1%)
- Ajuste dinâmico conforme performance
- Filtro de drawdown
- Filtro de horário e liquidez

### 6️⃣ Aprendizado Contínuo
- Registro de todas as análises
- Backtesting automático
- Recalibração semanal
- Relatórios de performance

## 🏗️ Arquitetura

```
bruno-robo-day-trade/
├── backend/
│   ├── app.py                 # FastAPI principal
│   ├── config.py              # Configurações
│   ├── requirements.txt        # Dependências
│   ├── models/
│   │   ├── __init__.py
│   │   ├── cnn_model.py       # Modelo CNN para análise
│   │   └── bayesian_model.py  # Modelo Bayesiano
│   ├── services/
│   │   ├── image_analysis.py  # Análise de imagens
│   │   ├── technical_analysis.py # Indicadores técnicos
│   │   ├── score_calculator.py # Score multivariável
│   │   ├── risk_manager.py    # Gestão de risco
│   │   └── prediction_engine.py # Motor de previsão
│   ├── database/
│   │   ├── models.py          # Modelos SQLAlchemy
│   │   └── db.py              # Conexão com BD
│   └── routes/
│       └── api.py             # Endpoints da API
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── index.js       # Home
│   │   │   └── dashboard.js   # Dashboard
│   │   ├── components/
│   │   │   ├── UploadImage.js
│   │   │   ├── ResultCard.js
│   │   │   └── HistoryChart.js
│   │   └── styles/
│   ├── package.json
│   └── .env.example
├── docker-compose.yml
├── Dockerfile
├── .env.example
└── README.md

```

## 🚀 Como Usar

### 1. Instalação Local

```bash
# Clone o repositório
git clone https://github.com/brunosg24/bruno-robo-day-trade.git
cd bruno-robo-day-trade

# Configure as variáveis de ambiente
cp .env.example .env

# Execute com Docker Compose
docker-compose up -d
```

### 2. Usar a Aplicação

1. Acesse: `http://localhost:3000`
2. Upload a imagem do gráfico
3. Clique em "Analisar"
4. Receba a previsão instantaneamente

## 📊 Exemplo de Saída

```
═════════════════════════════════════════════
       🤖 BRUNO ROBÔ - ANÁLISE DE GRÁFICO
═════════════════════════════════════════════

📈 TENDÊNCIA DETECTADA: ALTA ⬆️

🔍 INDICADORES:
   ✅ EMA 9 (128.350) > EMA 21 (128.120) > EMA 200 (127.890)
   ✅ RSI: 58 (Zona de compra ideal)
   ✅ MACD: Positivo (cruzamento de alta)
   ✅ Volume: +25% acima da média

───────────────────────────────────────────

📊 ANÁLISE MULTIFATORIAL:
   • Tendência confirmada: 30/30 pts
   • Pullback estruturado: 15/15 pts
   • Volume forte: 20/20 pts
   • RSI ideal: 10/10 pts
   • Estrutura de mercado: 13/15 pts
   
   Score Final: 88/100 ✅ OPERAÇÃO VÁLIDA

───────────────────────────────────────────

🎯 PREVISÃO PROBABILÍSTICA:

   Direção: ALTA ⬆️
   Probabilidade: 71%
   Confiança do modelo: ALTA

───────────────────────────────────────────

💰 RECOMENDAÇÃO OPERACIONAL:

   Entrada: 128.450
   Stop Loss: 128.120
   Take Profit: 128.980
   
   Risco: 33 pontos (-330 em contrato)
   Retorno: 70 pontos (+700 em contrato)
   Risco/Retorno: 1:2.1 ✅ Favorável

───────────────────────────────────────────

⚠️ AVISOS IMPORTANTES:
   • NÃO é garantia de lucro
   • Sempre respeite stop loss
   • Use gestão de risco (1% por trade)
   • Sistema trabalha com probabilidade
   • É ferramenta de apoio, não recomendação financeira

═════════════════════════════════════════════
```

## 🧠 Estratégia Matemática

### Score Multivariável

```
Score = (Tendência × 0.30) +
         (Pullback × 0.15) +
         (Volume × 0.20) +
         (Delta × 0.10) +
         (RSI × 0.10) +
         (Estrutura × 0.15)

Se Score ≥ 75 → Operação Válida
```

### Expectativa Matemática

```
E = (WinRate × RR) - (LossRate × 1)

Meta: E > +0.50 (positivo)
Win Rate esperado: 60-67%
Profit Factor: 1.8-2.3
```

### Bayesiano Adaptativo

```
P(Ganho|Setup) = (Prior × Likelihood) / Evidence

- Prior: taxa histórica do setup
- Likelihood: performance dos últimos 30 trades
- Evidence: normalização estatística
```

## 📈 Performance Esperada

Com disciplina e filtro forte:
- **Win Rate**: 60-67%
- **Profit Factor**: 1.8-2.3
- **Drawdown**: < 15%
- **Expectativa Matemática**: +0.60-0.80 por unidade de risco

## 🔐 Segurança e Avisos

⚠️ **IMPORTANTE:**
- Este sistema NÃO garante lucro
- NÃO substitui gestão de risco
- Trabalha com PROBABILIDADE estatística
- É uma FERRAMENTA DE APOIO
- NÃO é recomendação financeira

## 📱 Requisitos

- Python 3.9+
- Node.js 16+
- PostgreSQL 13+
- Docker e Docker Compose

## 🛠️ Tecnologias

**Backend:**
- FastAPI
- PyTorch / TensorFlow
- OpenCV
- TA-Lib
- SQLAlchemy
- PostgreSQL

**Frontend:**
- React / Next.js
- Axios
- Chart.js
- Tailwind CSS

## 📝 Licença

MIT

## 👨‍💻 Autor

Bruno SG24

---

**Desenvolvido com ❤️ para traders que buscam lucro consistente através de análise técnica profissional.