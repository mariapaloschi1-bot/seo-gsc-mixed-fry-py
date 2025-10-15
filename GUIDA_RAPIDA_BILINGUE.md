# 🌍 Guida Rapida - Tool SEO Bilingue (IT + EN)

## ✨ Cosa È Cambiato

**Prima (v5.0):**
```
❌ Solo CSV italiani da Google Search Console Italia
❌ KeyError con CSV inglesi
```

**Ora (v5.1 Bilingue):**
```
✅ CSV italiani (GSC Italia)
✅ CSV inglesi (GSC UK/US/International)
✅ Rilevamento automatico
✅ Zero configurazione
```

---

## 🚀 Quick Start

### 1. Download e Installazione
```bash
# Estrai il file
unzip SEO_MIXED_FRY_V5_BILINGUE.zip

# Installa dipendenze
pip install -r requirements.txt

# Avvia Streamlit
streamlit run app.py
```

### 2. Carica i Tuoi CSV
Esporta da Google Search Console **in qualsiasi lingua**:

#### 📁 File Necessari (5)
- `Dates.csv` o `Data.csv`
- `Queries.csv` o `Query.csv`
- `Pages.csv` o `Pagine.csv`
- `Countries.csv` o `Paesi.csv`
- `Devices.csv` o `Dispositivi.csv`

#### 🔍 Colonne Riconosciute

| Metrica | 🇮🇹 Italiano | 🇬🇧 Inglese |
|---------|--------------|-------------|
| Query | Query più frequenti | Top queries |
| Pagine | Pagine principali | Top pages |
| Data | Data | Date |
| Clicks | Clic | Clicks |
| Impressioni | Impressioni | Impressions |
| CTR | CTR | CTR |
| Posizione | Posizione | Position |
| Paese | Paese | Country |
| Dispositivo | Dispositivo | Device |

---

## 📊 Esempio Pratico

### CSV Italiano (GSC Italia)
```csv
Data,Clic,Impressioni,CTR,Posizione,Query più frequenti
2025-10-15,1234,45678,2.70%,5.6,boscolo gift
2025-10-14,1189,44321,2.68%,5.7,regali aziendali
```

**Risultato:** ✅ Caricato correttamente

---

### CSV Inglese (GSC UK/US)
```csv
Date,Clicks,Impressions,CTR,Position,Top queries
2025-10-15,1234,45678,2.70%,5.6,boscolo gift
2025-10-14,1189,44321,2.68%,5.7,corporate gifts
```

**Risultato:** ✅ Caricato correttamente

---

### CSV Misto (scenario reale)
```
📁 Queries.csv → Colonne inglesi (Top queries)
📁 Dates.csv → Colonne italiane (Data, Clic)
📁 Pages.csv → Colonne inglesi (Top pages)
```

**Risultato:** ✅ Funziona senza problemi!

---

## 🎯 Verifica Funzionamento

Dopo aver caricato i CSV, controlla che:

### ✅ Tab Overview
- [ ] Metriche aggregate visualizzate (Total Clicks, Impressions, CTR, Position)
- [ ] Grafico temporale con picchi e cali
- [ ] Donut chart dispositivi (Mobile, Desktop, Tablet)
- [ ] Bubble chart geografico con paesi

### ✅ Tab Query Analysis
- [ ] Lista top 100 query
- [ ] Colonne: Query, Clicks, Impressions, CTR, Position, CTR Target, Potenziale Clicks
- [ ] CTR Target realistici (algoritmo Scenario A/B)
- [ ] Possibilità di scaricare CSV

### ✅ Tab Pages
- [ ] Lista pagine principali
- [ ] Categoria URL automatica (Homepage, Product, Blog, etc.)
- [ ] CMS Detection (WordPress, Shopify, Magento, Salesforce)

### ✅ Tab Geographic
- [ ] Tabella paesi con metriche
- [ ] Mappa geografica interattiva
- [ ] Bubble chart con dimensioni clicks

### ✅ Tab Business Intelligence
- [ ] Eventi personalizzati con label PICCO/CALO
- [ ] 9 pulsanti festività (Black Friday, Natale, Cyber Monday, etc.)
- [ ] Filtri data range

---

## 🔧 Troubleshooting

### Errore: "KeyError: 'Query'"
**Causa:** CSV con colonne in lingua non supportata (es. tedesco, francese)  
**Soluzione:** Contatta lo sviluppatore per aggiungere il mapping

### Errore: "Empty DataFrame"
**Causa:** CSV vuoto o formato non valido  
**Soluzione:** Verifica di aver esportato dati dal periodo corretto in GSC

### Warning: "Missing columns"
**Causa:** CSV parziale (es. solo Dates.csv caricato)  
**Soluzione:** Carica tutti e 5 i file richiesti

---

## 📈 Dati di Test (CSV Forniti)

I CSV inglesi forniti dall'utente contengono:

### Countries.csv
- **140 paesi**
- **Italy (principale):** 466,020 clicks, 15.3M impressions, 3.04% CTR

### Dates.csv
- **365 giorni** di dati
- **Periodo:** Ottobre 2024 - Ottobre 2025
- **Peak clicks:** ~2,000/giorno

### Queries.csv
- **Top query:** "boscolo gift" (24,608 clicks, 20.27% CTR, pos 1.3)
- **Seconda:** "boscolo" (14,891 clicks)

### Pages.csv
- **Homepage:** https://www.boscologift.com/it/ (45,906 clicks)
- **Top category:** /it/gadget-personalizzati (32,115 clicks)

### Devices.csv
- **Mobile:** ~60% traffico
- **Desktop:** ~35%
- **Tablet:** ~5%

**✅ Tutti i file caricati e analizzati correttamente con la versione bilingue!**

---

## 🆘 Supporto Rapido

### Contatti
- **CSV non riconosciuto?** Invia prime 5 righe del file
- **Errore durante il caricamento?** Controlla formato (CSV, separatore `,` o `;`)
- **Vuoi supporto per altre lingue?** Richiedi estensione (DE, FR, ES, PT)

### Risorse
- 📖 **README_BILINGUE.md** - Documentazione completa
- 📝 **CHANGELOG_BILINGUE.md** - Storia modifiche tecniche
- 🚀 **GUIDA_RAPIDA_BILINGUE.md** - Questo documento

---

## 🎉 Ready to Go!

Il tool è ora pronto per analizzare CSV da qualsiasi versione internazionale di Google Search Console.

**Lingue supportate:**
- 🇮🇹 Italiano ✅
- 🇬🇧 Inglese ✅
- 🇩🇪 Tedesco ⏳ (su richiesta)
- 🇫🇷 Francese ⏳ (su richiesta)
- 🇪🇸 Spagnolo ⏳ (su richiesta)

---

**Versione:** 5.1 Bilingue  
**Data:** 15 ottobre 2025  
**Stato:** Production Ready 🚀
