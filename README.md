# SEO Mixed Fry - Tool di Analisi GSC

Tool professionale per l'analisi avanzata dei dati Google Search Console con focus su trend, geografia, intent delle query e opportunità business.

**Made with ❤️ by Maria Paloschi**

## 🚀 Quick Start

```bash
# Installa dipendenze
pip install -r requirements.txt

# Avvia l'applicazione
streamlit run app.py
```

## 📋 Requisiti

- Python 3.8+
- Streamlit, Pandas, Plotly, NumPy (vedi requirements.txt)

## ✨ Ultime Modifiche (v5 Final)

### 🎨 Miglioramenti UI/UX
- ✅ **Contrasto migliorato**: Sfondo `#2d3748` per file uploader, selectbox e input
- ✅ **Pulsanti festività ridisegnati**: Multiriga, compatti, colori personalizzati per festività
- ✅ **Eventi business più chiari**: Label "PICCO" e "CALO" con descrizioni esplicite

### 📊 Miglioramenti Analytics
- ✅ **Bubble chart geografico avanzato**: 
  - Gradient colori (rosso→arancione→verde) basato su CTR
  - Scala logaritmica per impressioni
  - Colorbar con legenda
  - Bubble size normalizzate

### 🛍️ CMS Detection Avanzato
Riconoscimento automatico pattern per:
- **Shopify**: `/products/` (prodotti), `/collections/` (categorie)
- **WordPress/WooCommerce**: `/product/`, `/product-category/`
- **Magento**: `.html` con ID numerico, `/p/`
- **Salesforce Commerce**: `/s/p/` (prodotti), `/s/c/` (categorie)
- **Blog**: `/blog/`, `/news/`, `/magazine/`, date in URL (2015-2025)

### 🎯 CTR Target Realistici
Calcolo intelligente basato su benchmark reali (Backlinko/Sistrix):
- **Pos 1**: 28.5% → **Pos 10**: 2.5%
- **Pos 11-20**: 1.5% → **Pos 21-30**: 0.8%
- Algoritmo adattivo: se CTR vicino a baseline → target conservativo +15%
- Se CTR basso → colma 60% del gap verso baseline
- Cap massimo: 130% del benchmark

## 📊 Funzionalità Principali

### 1️⃣ TREND ANALYSIS
- 📈 Rilevamento automatico picchi e cali (con label "PICCO"/"CALO")
- 🎄 Analisi 9 festività italiane con colori personalizzati
- 📅 Grafici temporali interattivi
- 📊 Statistiche weekend vs settimana

### 2️⃣ GEOGRAPHIC
- 🗺️ Performance per paese con filtri avanzati
- 💎 Identificazione mercati opportunità (alto impression, basso CTR)
- 🫧 **Bubble chart migliorato** con gradient colori e scala logaritmica
- 📊 Tabelle dettagliate con potenziale clic

### 3️⃣ INTENT
- 🎯 Classificazione automatica: Commerciale, Informazionale, Transazionale, Navigazionale
- 📥 Export CSV completo con tutte le query classificate
- 📊 Donut chart distribuzione intenti
- 🔍 Filtro brand/non-brand

### 4️⃣ BUSINESS
- 🏢 **Categorizzazione URL CMS-aware** (WordPress, Shopify, Magento, Salesforce)
- 📊 Donut chart performance per categoria
- 💎 **Opportunità SEO con CTR target realistici** basati su benchmark
- 📈 Calcolo potenziale clic ottimizzato

## 📁 File CSV Richiesti

Esporta da Google Search Console:
1. **Date.csv** - Performance per data
2. **Paesi.csv** - Performance per paese
3. **Query.csv** - Performance per query
4. **Pagine.csv** - Performance per URL
5. **Dispositivi.csv** - Performance per device

### Come Esportare da GSC
1. Vai su Google Search Console → Rendimento
2. Seleziona dimensione (Data, Paesi, Query, Pagine, Dispositivi)
3. Clicca "Esporta" → "Scarica CSV"

## 🎨 Design

- **Dark mode professionale** con gradiente ciano/turchese
- **Contrasto alto** per massima leggibilità
- **Responsive** - adattamento automatico schermi
- **Grafici Plotly interattivi** con template dark ottimizzato

## 🔧 Configurazione

### Brand Keyword
Inserisci il tuo brand nella sidebar per filtrare analisi brand vs non-brand.

### Festività Italiane
9 festività pre-configurate con colori personalizzati:
- 🎄 Natale (rosso)
- 🛍️ Black Friday (ciano)
- 🏷️ Saldi Invernali (viola)
- 💕 San Valentino (rosa)
- 👩‍👧‍👦 Festa Mamma (arancione)
- ☀️ Saldi Estivi (giallo)
- 📚 Back to School (blu)
- 🎃 Halloween (arancione scuro)
- 👨‍👧‍👦 Festa Papà (turchese)

## 🛠️ Troubleshooting

### CSV non caricato
- Verifica encoding (UTF-8, Latin-1 supportati)
- Controlla nomi colonne (Data/Date, Clic/Clicks, ecc.)

### Dati non visualizzati
- Carica tutti e 5 i file CSV richiesti
- Inserisci keyword brand se vuoi filtri brand/non-brand

## 📝 Changelog

**v5 Final** (Ottobre 2025)
- ✅ Rimossa tab AI/API (non funzionante)
- ✅ Contrasto UI migliorato (#2d3748 per controlli)
- ✅ Eventi business con label chiare
- ✅ Pulsanti festività multiriga con colori diversi
- ✅ Bubble chart geografico ridisegnato
- ✅ CMS detection per WordPress, Shopify, Magento, Salesforce
- ✅ CTR target realistici con algoritmo adattivo

## 📄 Licenza

Tool sviluppato per analisi SEO professionale.

---

*Per supporto contatta Maria Paloschi*
