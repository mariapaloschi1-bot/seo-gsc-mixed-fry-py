# SEO Mixed Fry - Tool di Analisi GSC

Tool professionale per l'analisi dei dati Google Search Console con focus su trend, geografia, intent delle query e opportunità business.

Made with ❤️ by Maria Paloschi

## 🚀 Installazione Rapida

```bash
# Clona o scarica il progetto
cd seo_tool_v5_improved_modified

# Installa le dipendenze
pip install -r requirements.txt

# Avvia l'applicazione
streamlit run app.py
```

## 📋 Requisiti

- Python 3.8 o superiore
- Le dipendenze sono specificate in `requirements.txt`

## 📊 Funzionalità

### 1. TREND ANALYSIS
- 📈 Rilevamento automatico picchi e cali di performance
- 🎄 Analisi festività italiane (Natale, Black Friday, Saldi, ecc.)
- 📊 Grafici temporali interattivi
- 📅 Statistiche weekend vs settimana

### 2. GEOGRAPHIC
- 🗺️ Performance per paese con grafici a barre
- 💎 Identificazione mercati con opportunità
- 🫧 Bubble chart avanzato (dimensione = clic, colore = CTR)
- 🔍 Filtri per regione (Europa, Americhe)

### 3. INTENT
- 🎯 Classificazione automatica query per intento
- 🛒 Commerciale, ℹ️ Informazionale, 💳 Transazionale, 🧭 Navigazionale
- 📥 Export CSV completo con tutte le query classificate
- 📊 Visualizzazione distribuzione con donut chart

### 4. BUSINESS
- 🏢 Categorizzazione URL intelligente (Homepage, Categorie, Prodotti, Blog)
- 🛍️ Supporto CMS: WordPress, Shopify, Magento, Salesforce
- 💎 Opportunità SEO con CTR target realistici
- 📈 Calcolo potenziale clic basato su benchmark di settore

## 📁 File CSV Richiesti

Il tool richiede 5 file CSV esportati da Google Search Console:

1. **Date.csv** - Performance per data
2. **Paesi.csv** - Performance per paese
3. **Query.csv** - Performance per query
4. **Pagine.csv** - Performance per URL
5. **Dispositivi.csv** - Performance per device

### Come Esportare da GSC

1. Vai su Google Search Console
2. Seleziona "Rendimento"
3. Clicca su ogni dimensione (Data, Paesi, Query, Pagine, Dispositivi)
4. Clicca sull'icona "Esporta" in alto a destra
5. Scegli "Scarica CSV"

## 🎨 Caratteristiche Tecniche

- **Design Dark Mode** con gradiente ciano/turchese
- **Contrasto Alto** per massima leggibilità
- **Responsive** - si adatta a diversi schermi
- **Performance ottimizzate** con session state
- **Grafici interattivi** Plotly con template scuro

## 🔧 Configurazione

### Brand Keyword
Inserisci la keyword del tuo brand nella sidebar per filtrare le analisi tra query brand e non-brand.

### Filtri Festività
9 festività italiane pre-configurate con date automatiche per analisi stagionale.

## 📈 CTR Target Realistici

Il tool calcola CTR target basati su benchmark reali di settore:
- Posizione 1: 28.5%
- Posizione 2: 15.7%
- Posizione 3: 11.0%
- Posizione 4-10: scala graduale
- Posizione 11+: valori conservativi

## 🛠️ Troubleshooting

### Errore di encoding CSV
Il tool prova automaticamente più encoding (UTF-8, Latin-1, CP1252). Se i dati non vengono caricati, verifica che i CSV siano ben formattati.

### File non riconosciuto
Assicurati che i CSV contengano le colonne corrette:
- Data/Date, Clic/Clicks, Impressioni/Impressions, CTR, Posizione/Position
- Query più frequenti/Query
- Pagine principali/Page
- Paese/Country
- Dispositivo/Device

## 📝 Note di Versione

**v5 - Modifiche Finali**
- ✅ Rimossa tab AI/API
- ✅ Migliorato contrasto file upload e filtri
- ✅ Eventi business con label esplicative
- ✅ Pulsanti festività multiriga ottimizzati
- ✅ Bubble chart geografico riprogettato
- ✅ Categorizzazione URL CMS-aware (WordPress, Shopify, Magento, Salesforce)
- ✅ CTR target realistici basati su benchmark

## 🤝 Supporto

Per domande o segnalazioni contatta Maria Paloschi.

## 📄 Licenza

Tool sviluppato per analisi SEO professionale.
