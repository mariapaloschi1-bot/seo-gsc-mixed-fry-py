# 🌍 SEO Mixed Fry - Versione Bilingue (IT + EN)

## ✨ Novità: Supporto CSV Google Search Console in Italiano E Inglese

Questa versione supporta **automaticamente** i CSV esportati da Google Search Console sia in **Italiano** che in **Inglese**, senza richiedere configurazioni manuali.

---

## 📊 Colonne CSV Supportate

### 🇮🇹 **Italiano (interfaccia GSC italiana)**

| Colonna GSC IT           | Nome Interno Tool |
|--------------------------|-------------------|
| Data                     | Date              |
| Clic                     | Clicks            |
| Impressioni              | Impressions       |
| CTR                      | CTR               |
| Posizione                | Position          |
| Query più frequenti      | Query             |
| Pagine principali        | Page              |
| Paese                    | Country           |
| Dispositivo              | Device            |

### 🇬🇧 **Inglese (interfaccia GSC inglese)**

| Colonna GSC EN   | Nome Interno Tool |
|------------------|-------------------|
| Date             | Date              |
| Clicks           | Clicks            |
| Impressions      | Impressions       |
| CTR              | CTR               |
| Position         | Position          |
| Top queries      | Query             |
| Top pages        | Page              |
| Country          | Country           |
| Device           | Device            |

---

## 🚀 Come Funziona

Il tool **rileva automaticamente** la lingua dei CSV caricati:

1. **Carica i tuoi CSV** (italiano O inglese)
2. Il sistema riconosce le colonne automaticamente
3. **Nessuna configurazione manuale richiesta**

### Esempio Pratico

**CSV Italiano:**
```csv
Data,Clic,Impressioni,CTR,Posizione,Query più frequenti
2025-10-15,1234,45678,2.70%,5.6,boscolo gift
```

**CSV Inglese:**
```csv
Date,Clicks,Impressions,CTR,Position,Top queries
2025-10-15,1234,45678,2.70%,5.6,boscolo gift
```

✅ **Entrambi funzionano perfettamente!**

---

## 📦 File CSV Richiesti

Come sempre, carica questi 5 file esportati da Google Search Console:

1. **Dates.csv** / **Date.csv** - Dati temporali
2. **Queries.csv** - Top query
3. **Pages.csv** - Pagine principali
4. **Countries.csv** / **Country.csv** - Dati geografici
5. **Devices.csv** - Dati per dispositivo

**Nota:** I nomi dei file possono essere in italiano o inglese (es. "Dates.csv" o "Data.csv").

---

## ⚙️ Requisiti Tecnici

### Streamlit Cloud (Python 3.13+)
```
streamlit==1.39.0
pandas==2.2.3
plotly==5.24.1
numpy==2.1.2
requests==2.32.3
```

### Locale (Python 3.9+)
Stesso requirements.txt, compatibile con Python 3.9-3.13.

---

## 🔧 Modifiche Tecniche (per sviluppatori)

### Mapping Colonne Esteso

Il sistema ora include **doppio mapping** nella funzione `parse_csv_robust()`:

```python
column_mapping = {
    # Italiano
    'Data': 'Date',
    'Clic': 'Clicks',
    'Impressioni': 'Impressions',
    'Posizione': 'Position',
    'Query più frequenti': 'Query',
    'Pagine principali': 'Page',
    'Paese': 'Country',
    'Dispositivo': 'Device',
    
    # Inglese
    'Top queries': 'Query',
    'Top pages': 'Page'
    # Date, Clicks, Impressions, Position, Country, Device già in inglese
}
```

### Rilevamento Automatico

Il sistema:
1. Legge le colonne del CSV caricato
2. Applica il mapping se trova corrispondenze (IT o EN)
3. Mantiene i nomi originali se già in formato standard
4. Normalizza tutti i dati al formato interno comune

---

## 🎯 Casi d'Uso Testati

✅ **CSV completamente in italiano** (es. export da GSC Italia)  
✅ **CSV completamente in inglese** (es. export da GSC USA/UK)  
✅ **Mix di file** (es. Queries.csv in EN + Dates.csv in IT)  
✅ **CSV con encoding UTF-8 e BOM**  
✅ **CSV con separatori `;` o `,`**  

---

## 📝 Changelog

### v5.1 - Bilingue (2025-10-15)
- ✨ Aggiunto supporto CSV in inglese
- 🌍 Rilevamento automatico lingua colonne
- 🔧 Mapping esteso: "Top queries" → Query, "Top pages" → Page
- 📚 Documentazione bilingue

### v5.0 - Finale Completo
- 7 modifiche UI/UX
- Fix compatibilità Python 3.13
- Fix grafici e descrizioni
- CTR target realistici
- Bubble chart geografico

---

## 🆘 Supporto

Se riscontri problemi con CSV in altre lingue (tedesco, francese, spagnolo), contatta lo sviluppatore per estendere il mapping.

**Lingue attualmente supportate:**
- 🇮🇹 Italiano
- 🇬🇧 Inglese (US/UK)

---

## 📄 Licenza

Uso interno - Tool SEO per analisi Google Search Console

---

**Versione:** 5.1 Bilingue  
**Data:** 15 ottobre 2025  
**Compatibilità:** Python 3.9+ | Streamlit Cloud ✅
