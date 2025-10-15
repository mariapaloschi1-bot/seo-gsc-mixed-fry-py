import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import numpy as np
import requests
import base64
import json
import time

# ============================================
# CONFIGURAZIONE PAGINA
# ============================================
st.set_page_config(
    page_title="SEO Mixed Fry - Tool di Analisi GSC",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# FIX 1: CSS CUSTOM CON CONTRASTO CORRETTO
# ============================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f0f0f 0%, #1a1a2e 100%);
    }
    
    /* FIX SIDEBAR SCURA */
    [data-testid="stSidebar"] {
        background-color: #0e1117 !important;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background-color: #0e1117 !important;
    }
    
    /* FIX SELECTBOX - TESTO CHIARO SU SFONDO SCURO */
    [data-testid="stSidebar"] [data-baseweb="select"] > div,
    [data-testid="stSidebar"] [data-baseweb="select"] input {
        background-color: #2d3748 !important;
        color: #ffffff !important;
    }
    
    [data-baseweb="select"] > div {
        background-color: #2d3748 !important;
        color: #ffffff !important;
        border: 1px solid #00d4ff !important;
    }
    
    [data-baseweb="select"] input {
        color: #ffffff !important;
    }
    
    /* FIX DROPDOWN MENU */
    [data-baseweb="popover"] {
        background-color: #2d3748 !important;
    }
    
    [role="option"] {
        background-color: #2d3748 !important;
        color: #ffffff !important;
    }
    
    [role="option"]:hover {
        background-color: #00d4ff !important;
        color: #000000 !important;
    }
    
    /* FIX INPUT FIELDS */
    input[type="text"],
    input[type="number"],
    input[type="password"] {
        background-color: #2d3748 !important;
        color: #ffffff !important;
        border: 1px solid #00d4ff !important;
    }
    
    /* FIX FILE UPLOADER */
    [data-testid="stFileUploader"] {
        background-color: #2d3748 !important;
        border: 2px solid #00d4ff !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }
    
    [data-testid="stFileUploader"] section {
        border: 2px dashed #00d4ff !important;
        background-color: #1a202c !important;
    }
    
    [data-testid="stFileUploader"] label {
        color: #ffffff !important;
    }
    
    /* FIX DATE INPUT */
    [data-baseweb="input"] input {
        background-color: #2d3748 !important;
        color: #ffffff !important;
        border: 1px solid #00d4ff !important;
    }
    
    /* Header migliorato */
    .main-header {
        text-align: center;
        padding: 30px;
        background: linear-gradient(135deg, #16213e 0%, #0f3460 100%);
        border-radius: 20px;
        border: 1px solid #1f4068;
        margin-bottom: 30px;
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #00d4ff, #00fff7, #4ecdc4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    
    .subtitle {
        font-size: 1.1rem;
        color: #00d4ff;
        font-weight: 500;
    }
    
    /* Tabs - colori vividi */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: #16213e;
        border-radius: 15px;
        padding: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 12px;
        color: #94a3b8;
        font-weight: 600;
        padding: 15px 25px;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(0, 212, 255, 0.1);
        color: #00d4ff;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #00d4ff, #4ecdc4) !important;
        color: white !important;
        box-shadow: 0 5px 20px rgba(0, 212, 255, 0.4);
    }
    
    /* Holiday buttons - MIGLIORATI */
    .holiday-btn-container {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        margin-bottom: 20px;
    }
    
    .holiday-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 8px 14px;
        min-width: 110px;
        min-height: 48px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        border: none;
        border-radius: 12px;
        color: white;
        font-weight: 600;
        font-size: 0.8rem;
        white-space: normal;
        line-height: 1.3;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        text-shadow: 0 1px 2px rgba(0,0,0,0.3);
    }
    
    .holiday-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    
    /* Stats cards - contrasto migliorato */
    .stat-card {
        background: linear-gradient(135deg, #16213e 0%, #1f4068 100%);
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #00d4ff;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0, 212, 255, 0.3);
    }
    
    .stat-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #00d4ff;
        margin-bottom: 8px;
        text-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
    }
    
    .stat-label {
        color: #e0e7ff;
        font-size: 1rem;
        font-weight: 500;
    }
    
    /* Section headers - testo chiaro */
    h3, h4, h5 {
        color: #00d4ff !important;
        font-weight: 600 !important;
    }
    
    /* Opportunity cards */
    .opportunity-card {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.1), rgba(78, 205, 196, 0.1));
        border: 2px solid #00d4ff;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 15px;
    }
    
    /* Market section cards */
    .market-section {
        background: linear-gradient(135deg, #16213e 0%, #1f4068 100%);
        border: 2px solid #00d4ff;
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 20px;
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 12px;
        padding: 12px 30px;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
    }
    
    /* Testo generale - contrasto alto */
    p, span, label, div {
        color: #e0e7ff !important;
    }
    
    /* Dataframe styling */
    .stDataFrame {
        background: #16213e;
        border-radius: 10px;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ============================================
# FESTIVITÀ ITALIANE - ORIGINALE NON MODIFICATO
# ============================================
HOLIDAYS = [
    {"name": "Natale", "start": "12-20", "end": "01-10", "emoji": "🎄", "color": "#dc2626"},
    {"name": "Black Friday", "start": "11-20", "end": "12-02", "emoji": "🛍️", "color": "#0891b2"},
    {"name": "Saldi Invernali", "start": "01-05", "end": "02-28", "emoji": "🏷️", "color": "#7c3aed"},
    {"name": "San Valentino", "start": "02-10", "end": "02-18", "emoji": "💕", "color": "#ec4899"},
    {"name": "Festa Mamma", "start": "05-05", "end": "05-15", "emoji": "👩‍👧‍👦", "color": "#f59e0b"},
    {"name": "Saldi Estivi", "start": "07-01", "end": "08-31", "emoji": "☀️", "color": "#eab308"},
    {"name": "Back to School", "start": "08-15", "end": "09-15", "emoji": "📚", "color": "#3b82f6"},
    {"name": "Halloween", "start": "10-20", "end": "11-05", "emoji": "🎃", "color": "#ea580c"},
    {"name": "Festa Papà", "start": "03-15", "end": "03-25", "emoji": "👨‍👧‍👦", "color": "#06b6d4"}
]

# ============================================
# PALETTE COLORI COERENTE
# ============================================
COLOR_PALETTE = {
    'primary': '#00d4ff',
    'secondary': '#4ecdc4',
    'accent': '#667eea',
    'success': '#10b981',
    'warning': '#f59e0b',
    'danger': '#ef4444',
    'chart_colors': ['#00d4ff', '#4ecdc4', '#667eea', '#a855f7', '#ec4899', '#f59e0b', '#10b981', '#06b6d4']
}

# ============================================
# FUNZIONI PARSING CSV
# ============================================
def parse_csv_robust(uploaded_file):
    """Parser CSV robusto"""
    try:
        encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'iso-8859-1', 'cp1252']
        
        for encoding in encodings:
            try:
                uploaded_file.seek(0)
                df = pd.read_csv(uploaded_file, encoding=encoding)
                
                column_mapping = {
                    'Data': 'Date',
                    'Clic': 'Clicks',
                    'Impressioni': 'Impressions',
                    'CTR': 'CTR',
                    'Posizione': 'Position',
                    'Query più frequenti': 'Query',
                    'Pagine principali': 'Page',
                    'Paese': 'Country',
                    'Dispositivo': 'Device'
                }
                
                df.rename(columns=column_mapping, inplace=True)
                
                if 'CTR' in df.columns:
                    df['CTR'] = df['CTR'].astype(str).str.replace('%', '').str.replace(',', '.').astype(float)
                
                for col in ['Clicks', 'Impressions']:
                    if col in df.columns:
                        df[col] = df[col].astype(str).str.replace('.', '').str.replace(',', '').astype(int)
                
                if 'Position' in df.columns:
                    df['Position'] = df['Position'].astype(str).str.replace(',', '.').astype(float)
                
                return df
            except:
                continue
        
        return None
    except Exception as e:
        st.error(f"❌ Errore parsing CSV: {str(e)}")
        return None

# ============================================
# FIX 3: CLASSIFICAZIONE INTENT CORRETTA
# ============================================
def classify_query_intents_improved(queries_df):
    """Classificazione PRECISA basata su intent keywords"""
    
    # Keywords per ogni intento - SPECIFICHE come richiesto
    commercial_keywords = [
        'prezzo', 'prezzi', 'price', 'costo', 'quanto costa',
        'sconto', 'sconti', 'coupon', 'offerta', 'offerte', 'discount', 'sale', 'saldi',
        'economico', 'conveniente', 'cheap', 'acquista', 'acquistare', 'comprare', 
        'compra', 'buy', 'purchase', 'black friday', 'cyber monday', 'promozione',
        'outlet', 'risparmia', 'low cost', 'deal', 'occasione', 'migliore prezzo'
    ]
    
    # Informazionali - CHI, COSA, DOVE, QUANDO, PERCHÉ, STORIA
    informational_keywords = [
        'chi', 'chi è', 'chi sono',
        'cosa', 'cosa è', "cos'è", 'cos è', 'che cosa',
        'dove', 'quando', 
        'perché', 'perchè', 'perche',
        'come', 'come fare', 'come si',
        'storia', 'storia di', 'storia del', 'storia della',
        'quale', 'quali', 'quanto', 'quanti', 'quante',
        'definizione', 'significato', 'guida', 'tutorial',
        'consigli', 'differenza', 'caratteristiche',
        'why', 'what', 'how', 'when', 'where', 'who', 'history'
    ]
    
    # Transazionali - PRODOTTI E CATEGORIE
    transactional_keywords = [
        'abiti', 'abbigliamento', 'vestiti', 'magliette', 'camicie', 'pantaloni', 'jeans',
        'gonne', 'giacche', 'cappotti', 'scarpe', 'sneakers', 'stivali', 'sandali',
        'borse', 'zaini', 'portafogli', 'accessori',
        'rossetto', 'rossetti', 'trucco', 'makeup', 'make up', 'cosmetici', 'profumi',
        'gioielli', 'orologi', 'anelli', 'collane', 'bracciali',
        'viaggio', 'hotel', 'volo', 'vacanza', 'voli', 'viaggi',
        'viaggio in', 'viaggiare',
        'prodotto', 'prodotti', 'articolo', 'catalogo'
    ]
    
    # Navigazionali - SITO UFFICIALE, LOGIN
    navigational_keywords = [
        'sito ufficiale', 'official site', 'official website',
        'homepage', 'sito', 'website',
        'login', 'accesso', 'accedi',
        'contatti', 'contact'
    ]
    
    results = {
        'commercial': [],
        'informational': [],
        'transactional': [],
        'navigational': []
    }
    
    for _, row in queries_df.iterrows():
        text = str(row.get('Query', '')).lower().strip()
        classified = False
        
        # Priorità 1: Navigazionale
        for kw in navigational_keywords:
            if kw in text:
                results['navigational'].append(row)
                classified = True
                break
        
        if not classified:
            # Priorità 2: Informazionale - MATCH PRECISO
            for kw in informational_keywords:
                # Match all'inizio della frase o con spazi
                if (text.startswith(kw + ' ') or 
                    text.startswith(kw + ',') or
                    ' ' + kw + ' ' in text or 
                    text == kw):
                    results['informational'].append(row)
                    classified = True
                    break
        
        if not classified:
            # Priorità 3: Commerciale
            for kw in commercial_keywords:
                if kw in text:
                    results['commercial'].append(row)
                    classified = True
                    break
        
        if not classified:
            # Priorità 4: Transazionale
            for kw in transactional_keywords:
                if kw in text:
                    results['transactional'].append(row)
                    classified = True
                    break
        
        # Fallback: Transactional
        if not classified:
            results['transactional'].append(row)
    
    return {k: pd.DataFrame(v) if v else pd.DataFrame() for k, v in results.items()}

# ============================================
# CATEGORIZZAZIONE URL AVANZATA
# ============================================
def categorize_urls_advanced(pages_df):
    """Categorizza URL analizzando pattern WordPress, Shopify, Magento, Salesforce"""
    
    categories = {
        'Homepage': [],
        'Categorie': [],
        'Prodotti': [],
        'Blog/News': []
    }
    
    for _, row in pages_df.iterrows():
        path = str(row.get('Page', '')).lower()
        classified = False
        
        # Homepage
        if (path == '/' or path == '' or path.endswith('index.html') or 
            path.endswith('index.php') or len(path.replace('/', '')) < 3):
            categories['Homepage'].append(row)
            classified = True
        
        # Blog/News patterns - expanded
        elif any(x in path for x in ['/blog/', '/news/', '/magazine/', '/articoli/', '/post/', '/notizie/']):
            categories['Blog/News'].append(row)
            classified = True
        
        # Date in URL (blog articles) - format: /2021/12/ or /2021-12-
        elif any(f'/{year}/' in path or f'/{year}-' in path for year in range(2015, 2026)):
            categories['Blog/News'].append(row)
            classified = True
        
        # SHOPIFY PRODUCTS: /products/ in path
        elif '/products/' in path:
            categories['Prodotti'].append(row)
            classified = True
        
        # SHOPIFY COLLECTIONS: /collections/ in path
        elif '/collections/' in path or '/collection/' in path:
            categories['Categorie'].append(row)
            classified = True
        
        # WORDPRESS PRODUCTS (WooCommerce): /product/ in path
        elif '/product/' in path:
            categories['Prodotti'].append(row)
            classified = True
        
        # WORDPRESS CATEGORIES (WooCommerce)
        elif '/product-category/' in path or '/categoria-prodotto/' in path:
            categories['Categorie'].append(row)
            classified = True
        
        # MAGENTO PRODUCTS: /p/ or -p- with numbers
        elif ('/p/' in path or '-p-' in path) and any(c.isdigit() for c in path):
            categories['Prodotti'].append(row)
            classified = True
        
        # MAGENTO CATEGORIES & PRODUCTS: .html URLs
        elif path.endswith('.html'):
            # Check if URL has 3+ consecutive digits (likely product ID)
            has_product_id = False
            digit_count = 0
            for c in path:
                if c.isdigit():
                    digit_count += 1
                    if digit_count >= 3:
                        has_product_id = True
                        break
                else:
                    digit_count = 0
            
            if has_product_id:
                categories['Prodotti'].append(row)
            else:
                categories['Categorie'].append(row)
            classified = True
        
        # SALESFORCE COMMERCE CLOUD
        elif '/s/' in path and '/p/' in path:
            categories['Prodotti'].append(row)
            classified = True
        elif '/s/' in path and '/c/' in path:
            categories['Categorie'].append(row)
            classified = True
        
        # Generic product patterns
        elif any(x in path for x in ['/item/', '/items/', '/articolo/', '/sku-']):
            categories['Prodotti'].append(row)
            classified = True
        
        # Generic category patterns
        elif any(x in path for x in ['/categor', '/c/', '/cat/']):
            categories['Categorie'].append(row)
            classified = True
        
        # Fallback: if contains many digits at end -> product, else -> category
        if not classified:
            if any(c.isdigit() for c in path[-15:]):
                digit_density = sum(1 for c in path[-15:] if c.isdigit()) / min(15, len(path))
                if digit_density > 0.2:  # More than 20% digits
                    categories['Prodotti'].append(row)
                else:
                    categories['Categorie'].append(row)
            else:
                categories['Categorie'].append(row)
    
    return {k: pd.DataFrame(v) if v else pd.DataFrame() for k, v in categories.items()}

# ============================================
# FILTRO FESTIVITÀ
# ============================================
def filter_by_holiday(date_df, holiday_name):
    """Filtra dati per festività"""
    holiday = next((h for h in HOLIDAYS if h['name'] == holiday_name), None)
    if not holiday or date_df.empty:
        return date_df
    
    date_df['Date'] = pd.to_datetime(date_df['Date'])
    min_year = date_df['Date'].dt.year.min()
    max_year = date_df['Date'].dt.year.max()
    
    holiday_dates = []
    
    for year in range(min_year, max_year + 1):
        if holiday['start'].startswith('12') and holiday['end'].startswith('01'):
            start_date = pd.to_datetime(f"{year}-{holiday['start']}")
            end_date = pd.to_datetime(f"{year+1}-{holiday['end']}")
        else:
            start_date = pd.to_datetime(f"{year}-{holiday['start']}")
            end_date = pd.to_datetime(f"{year}-{holiday['end']}")
        
        date_range = pd.date_range(start=start_date, end=end_date)
        holiday_dates.extend(date_range)
    
    # Assicura sempre un DataFrame come return
    if not holiday_dates:
        return pd.DataFrame(columns=date_df.columns)
    
    filtered = date_df[date_df['Date'].isin(holiday_dates)]
    return filtered if not filtered.empty else pd.DataFrame(columns=date_df.columns)
# ============================================
# INIZIALIZZAZIONE SESSION STATE
# ============================================
if 'date_data' not in st.session_state:
    st.session_state.date_data = None
if 'countries_data' not in st.session_state:
    st.session_state.countries_data = None
if 'queries_data' not in st.session_state:
    st.session_state.queries_data = None
if 'pages_data' not in st.session_state:
    st.session_state.pages_data = None
if 'devices_data' not in st.session_state:
    st.session_state.devices_data = None
if 'brand_keyword' not in st.session_state:
    st.session_state.brand_keyword = ""
if 'active_holiday' not in st.session_state:
    st.session_state.active_holiday = None
# ============================================
# HEADER
# ============================================
st.markdown("""
<div class="main-header">
    <h1 class="main-title">SEO Mixed Fry</h1>
    <p class="subtitle">Made with ❤️ by Maria Paloschi</p>
</div>
""", unsafe_allow_html=True)

# ============================================
# SIDEBAR
# ============================================
with st.sidebar:
    st.markdown("## 📁 Carica File CSV")
    
    brand_keyword = st.text_input(
        "🏷️ Keyword Brand",
        value=st.session_state.brand_keyword,
        placeholder="es: elisabetta franchi"
    )
    st.session_state.brand_keyword = brand_keyword.lower().strip()
    
    st.markdown("---")
    
    date_file = st.file_uploader("📅 Date.csv", type=['csv'], key='date')
    countries_file = st.file_uploader("🌍 Paesi.csv", type=['csv'], key='countries')
    queries_file = st.file_uploader("🔍 Query.csv", type=['csv'], key='queries')
    pages_file = st.file_uploader("📄 Pagine.csv", type=['csv'], key='pages')
    devices_file = st.file_uploader("📱 Dispositivi.csv", type=['csv'], key='devices')
    
    if date_file:
        st.session_state.date_data = parse_csv_robust(date_file)
        if st.session_state.date_data is not None:
            st.success(f"✅ Date ({len(st.session_state.date_data)} righe)")
    
    if countries_file:
        st.session_state.countries_data = parse_csv_robust(countries_file)
        if st.session_state.countries_data is not None:
            if 'CTR' not in st.session_state.countries_data.columns:
                st.session_state.countries_data['CTR'] = (
                    st.session_state.countries_data['Clicks'] / 
                    st.session_state.countries_data['Impressions'] * 100
                ).round(2)
            st.success(f"✅ Paesi ({len(st.session_state.countries_data)} righe)")
    
    if queries_file:
        st.session_state.queries_data = parse_csv_robust(queries_file)
        if st.session_state.queries_data is not None:
            st.success(f"✅ Query ({len(st.session_state.queries_data)} righe)")
    
    if pages_file:
        st.session_state.pages_data = parse_csv_robust(pages_file)
        if st.session_state.pages_data is not None:
            st.success(f"✅ Pagine ({len(st.session_state.pages_data)} righe)")
    
    if devices_file:
        st.session_state.devices_data = parse_csv_robust(devices_file)
        if st.session_state.devices_data is not None:
            st.success(f"✅ Dispositivi ({len(st.session_state.devices_data)} righe)")
    
# Check files
all_files_loaded = all([
    st.session_state.date_data is not None,
    st.session_state.countries_data is not None,
    st.session_state.queries_data is not None,
    st.session_state.pages_data is not None,
    st.session_state.devices_data is not None
])

if not all_files_loaded:
    st.info("👆 Carica tutti i 5 file CSV dalla sidebar per iniziare")
    st.stop()

# ============================================
# 4 TAB PRINCIPALI
# ============================================
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 TREND ANALYSIS",
    "🗺️ GEOGRAPHIC",
    "🎯 INTENT",
    "💡 BUSINESS"
])

# ============================================
# TAB 1: TREND ANALYSIS - STAGIONALITÀ ORIGINALE
# ============================================
with tab1:
    st.markdown("### 📈 Analisi Picchi e Cali Performance")
    st.markdown("*Identifica automaticamente i giorni con variazioni significative nel traffico*")
    
    if st.session_state.date_data is not None:
        date_df = st.session_state.date_data.copy()
        date_df['Date'] = pd.to_datetime(date_df['Date'])
        date_df = date_df.sort_values('Date')
        
        events = []
        for i in range(1, len(date_df) - 1):
            current = date_df.iloc[i]
            prev = date_df.iloc[i-1]
            next_row = date_df.iloc[i+1]
            
            if current['Clicks'] > prev['Clicks'] * 1.5 and current['Clicks'] > next_row['Clicks'] * 1.2:
                events.append({'date': current['Date'].strftime('%Y-%m-%d'), 'type': 'peak', 'value': current['Clicks']})
            elif current['Clicks'] < prev['Clicks'] * 0.7 and current['Clicks'] < next_row['Clicks'] * 0.8:
                events.append({'date': current['Date'].strftime('%Y-%m-%d'), 'type': 'drop', 'value': current['Clicks']})
        
        if events:
            cols = st.columns(min(len(events[:5]), 5))
            for idx, event in enumerate(events[:5]):
                with cols[idx]:
                    icon = "📈" if event['type'] == 'peak' else "📉"
                    label = "PICCO" if event['type'] == 'peak' else "CALO"
                    color = COLOR_PALETTE['success'] if event['type'] == 'peak' else COLOR_PALETTE['danger']
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, {color}22, {color}11); border: 2px solid {color}; border-radius: 12px; padding: 15px; text-align: center;">
                        <div style="font-size: 2.5rem; margin-bottom: 5px;">{icon}</div>
                        <div style="font-weight: 700; color: {color}; font-size: 0.85rem; margin-bottom: 5px;">{label}</div>
                        <div style="font-weight: 600; color: #e0e7ff; margin: 5px 0;">{event['date']}</div>
                        <div style="color: #cbd5e1; font-size: 1.1rem; font-weight: 600;">{event['value']:,} clic</div>
                    </div>
                    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🎄 Analisi Festività")
    
    # FIX 2: STAGIONALITÀ ORIGINALE - NON MODIFICATA
    cols = st.columns([1, 1, 1, 1, 1])
    
    if cols[0].button("🔄 Mostra Tutto", use_container_width=True, key='reset_holiday'):
        st.session_state.active_holiday = None
        st.rerun()
    
    holiday_cols = st.columns(5)
    for idx, holiday in enumerate(HOLIDAYS):
        col_idx = idx % 5
        if holiday_cols[col_idx].button(
            f"{holiday['emoji']} {holiday['name']}", 
            key=f"holiday_{holiday['name']}", 
            use_container_width=True
        ):
            st.session_state.active_holiday = holiday['name']
            st.rerun()
    
    if st.session_state.active_holiday and st.session_state.date_data is not None:
        filtered_df = filter_by_holiday(st.session_state.date_data.copy(), st.session_state.active_holiday)
        
        if not filtered_df.empty:
            total_clicks = filtered_df['Clicks'].sum()
            total_impressions = filtered_df['Impressions'].sum()
            avg_ctr = (total_clicks / total_impressions * 100) if total_impressions > 0 else 0
            avg_position = filtered_df['Position'].mean()
            
            st.markdown(f"#### 📊 {st.session_state.active_holiday}")
            
            cols = st.columns(4)
            cols[0].metric("Clic Totali", f"{total_clicks:,}")
            cols[1].metric("Impressioni", f"{total_impressions:,}")
            cols[2].metric("CTR Medio", f"{avg_ctr:.2f}%")
            cols[3].metric("Posizione", f"{avg_position:.1f}")
    
    st.markdown("---")
    st.markdown("### 📈 Trend Temporale")
    
    if st.session_state.active_holiday:
        plot_df = filter_by_holiday(st.session_state.date_data.copy(), st.session_state.active_holiday)
    else:
        plot_df = st.session_state.date_data.copy()
    
    plot_df['Date'] = pd.to_datetime(plot_df['Date'])
    plot_df = plot_df.sort_values('Date')
    
    cols = st.columns(3)
    with cols[0]:
        start_date = st.date_input("Data Inizio", value=plot_df['Date'].min().date())
    with cols[1]:
        end_date = st.date_input("Data Fine", value=plot_df['Date'].max().date())
    with cols[2]:
        metric = st.selectbox("Metrica", ['Clicks', 'Impressions', 'CTR', 'Position'])
    
    plot_df = plot_df[(plot_df['Date'] >= pd.to_datetime(start_date)) & (plot_df['Date'] <= pd.to_datetime(end_date))]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=plot_df['Date'],
        y=plot_df[metric],
        mode='lines+markers',
        name=metric,
        line=dict(color=COLOR_PALETTE['primary'], width=3),
        marker=dict(size=6, color=COLOR_PALETTE['secondary']),
        fill='tozeroy',
        fillcolor='rgba(0, 212, 255, 0.1)'
    ))
    
    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor='#16213e',
        paper_bgcolor='#16213e',
        font=dict(color='#e0e7ff'),
        hovermode='x unified',
        height=450,
        xaxis_title="Data",
        yaxis_title=metric
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 📊 Statistiche Stagionalità")
    
    date_stats_df = st.session_state.date_data.copy()
    date_stats_df['Date'] = pd.to_datetime(date_stats_df['Date'])
    date_stats_df['DayOfWeek'] = date_stats_df['Date'].dt.dayofweek
    
    weekend_clicks = date_stats_df[date_stats_df['DayOfWeek'].isin([5, 6])]['Clicks'].sum()
    weekend_impressions = date_stats_df[date_stats_df['DayOfWeek'].isin([5, 6])]['Impressions'].sum()
    weekend_days = len(date_stats_df[date_stats_df['DayOfWeek'].isin([5, 6])])
    
    weekday_clicks = date_stats_df[~date_stats_df['DayOfWeek'].isin([5, 6])]['Clicks'].sum()
    weekday_impressions = date_stats_df[~date_stats_df['DayOfWeek'].isin([5, 6])]['Impressions'].sum()
    weekday_days = len(date_stats_df[~date_stats_df['DayOfWeek'].isin([5, 6])])
    
    weekend_avg_clicks = weekend_clicks / weekend_days if weekend_days > 0 else 0
    weekday_avg_clicks = weekday_clicks / weekday_days if weekday_days > 0 else 0
    
    weekend_avg_impressions = weekend_impressions / weekend_days if weekend_days > 0 else 0
    weekday_avg_impressions = weekday_impressions / weekday_days if weekday_days > 0 else 0
    
    peak_days = len(date_stats_df[date_stats_df['Clicks'] > date_stats_df['Clicks'].quantile(0.75)])
    
    mean_clicks = date_stats_df['Clicks'].mean()
    std_clicks = date_stats_df['Clicks'].std()
    cv = (std_clicks / mean_clicks * 100) if mean_clicks > 0 else 0
    
    cols = st.columns(3)
    cols[0].metric("Score Stagionalità", f"{cv:.1f}%", help="Coefficiente di variazione")
    cols[1].metric("Giorni di Picco", f"{peak_days}", help="Giorni sopra Q3")
    cols[2].metric("Weekend vs Weekday", f"{(weekend_avg_clicks/weekday_avg_clicks*100):.0f}%", help="Rapporto medio")
    
    st.markdown("#### 📊 Confronto Weekend vs Settimana")
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Clic Medi',
        x=['Weekend', 'Settimana'],
        y=[weekend_avg_clicks, weekday_avg_clicks],
        marker_color=COLOR_PALETTE['primary'],
        text=[f"{weekend_avg_clicks:.0f}", f"{weekday_avg_clicks:.0f}"],
        textposition='outside'
    ))
    
    fig.add_trace(go.Bar(
        name='Impressioni Medie',
        x=['Weekend', 'Settimana'],
        y=[weekend_avg_impressions, weekday_avg_impressions],
        marker_color=COLOR_PALETTE['secondary'],
        text=[f"{weekend_avg_impressions:.0f}", f"{weekday_avg_impressions:.0f}"],
        textposition='outside'
    ))
    
    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor='#16213e',
        paper_bgcolor='#16213e',
        font=dict(color='#e0e7ff'),
        barmode='group',
        height=400,
        xaxis_title="Periodo",
        yaxis_title="Media Giornaliera"
    )
    
    st.plotly_chart(fig, use_container_width=True)

# ============================================
# TAB 2: GEOGRAPHIC
# ============================================
with tab2:
    st.markdown("### 🗺️ Performance Geografica")
    
    if st.session_state.countries_data is not None:
        countries_df = st.session_state.countries_data.copy()
        
        cols = st.columns(3)
        with cols[0]:
            map_metric = st.selectbox("Metrica", ['Clicks', 'Impressions', 'CTR'], key='map_metric')
        with cols[1]:
            country_filter = st.selectbox("Filtro", ['Tutti', 'Top 10', 'Europa', 'Americhe'])
        with cols[2]:
            min_perf = st.number_input("Min Performance", min_value=0, value=100, step=100)
        
        if map_metric in ['Clicks', 'Impressions']:
            filtered = countries_df[countries_df[map_metric] >= min_perf]
        else:
            filtered = countries_df.copy()
        
        if country_filter == 'Top 10':
            filtered = filtered.nlargest(10, map_metric)
        elif country_filter == 'Europa':
            euro = ['Italia', 'Germania', 'Francia', 'Spagna', 'Regno Unito', 'Paesi Bassi', 'Belgio', 'Austria', 'Svizzera']
            filtered = filtered[filtered['Country'].isin(euro)]
        elif country_filter == 'Americhe':
            americas = ['Stati Uniti', 'Canada', 'Messico', 'Brasile', 'Argentina']
            filtered = filtered[filtered['Country'].isin(americas)]
        
        top_15 = filtered.nlargest(15, map_metric).sort_values(map_metric, ascending=True)
        
        if not top_15.empty:
            fig = go.Figure()
            
            fig.add_trace(go.Bar(
                y=top_15['Country'],
                x=top_15[map_metric],
                orientation='h',
                marker=dict(
                    color=top_15[map_metric],
                    colorscale=[[0, COLOR_PALETTE['chart_colors'][6]], [0.5, COLOR_PALETTE['primary']], [1, COLOR_PALETTE['accent']]],
                    line=dict(width=0)
                ),
                text=top_15[map_metric],
                texttemplate='%{text:,.0f}',
                textposition='auto',
                hovertemplate='<b>%{y}</b><br>' + map_metric + ': %{x:,.0f}<extra></extra>'
            ))
            
            fig.update_layout(
                template="plotly_dark",
                plot_bgcolor='#16213e',
                paper_bgcolor='#16213e',
                font=dict(color='#e0e7ff'),
                height=600,
                xaxis_title=map_metric,
                yaxis_title="",
                showlegend=False
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        st.markdown("### 💎 Mercati con Opportunità")
        
        opportunity_markets = countries_df[
            (countries_df['Impressions'] > 10000) &
            (countries_df['CTR'] < 2)
        ].sort_values('Impressions', ascending=False)
        
        if not opportunity_markets.empty:
            st.markdown(f"**🌍 {len(opportunity_markets)} mercati identificati**")
            
            opp_display = opportunity_markets[['Country', 'Impressions', 'Clicks', 'CTR', 'Position']].head(10)
            opp_display['Potenziale +Clic'] = ((opp_display['Impressions'] * 0.03) - opp_display['Clicks']).astype(int)
            
            st.dataframe(
                opp_display.style.format({
                    'Impressions': '{:,.0f}',
                    'Clicks': '{:,.0f}',
                    'CTR': '{:.2f}%',
                    'Position': '{:.1f}',
                    'Potenziale +Clic': '{:+,.0f}'
                }),
                use_container_width=True,
                height=400
            )
            
            fig = go.Figure()
            
            top_opp = opportunity_markets.head(15)
            
            # Normalize bubble sizes
            max_clicks = top_opp['Clicks'].max()
            min_clicks = top_opp['Clicks'].min()
            sizes = top_opp['Clicks'].apply(lambda x: 20 + (x - min_clicks) / (max_clicks - min_clicks) * 60)
            
            # Gradient colors based on CTR
            colors = top_opp['CTR'].values
            
            fig.add_trace(go.Scatter(
                x=top_opp['Impressions'],
                y=top_opp['CTR'],
                mode='markers+text',
                marker=dict(
                    size=sizes,
                    color=colors,
                    colorscale=[
                        [0, '#ef4444'],      # Red for low CTR
                        [0.5, '#f59e0b'],    # Orange
                        [1, '#10b981']       # Green for high CTR
                    ],
                    line=dict(width=2, color='white'),
                    opacity=0.8,
                    colorbar=dict(
                        title=dict(text="CTR %", side="right"),
                        tickmode="linear",
                        tick0=0,
                        dtick=0.5
                    )
                ),
                text=top_opp['Country'],
                textposition='top center',
                textfont=dict(size=11, color='white', family='Inter'),
                hovertemplate='<b style="font-size:14px">%{text}</b><br><br>' +
                             'Impressioni: %{x:,.0f}<br>' +
                             'CTR: %{y:.2f}%<br>' +
                             'Clic: ' + top_opp['Clicks'].apply(lambda x: f'{x:,.0f}').values + '<br>' +
                             '<extra></extra>'
            ))
            
            fig.update_layout(
                template="plotly_dark",
                plot_bgcolor='#16213e',
                paper_bgcolor='#16213e',
                font=dict(color='#e0e7ff', family='Inter'),
                height=550,
                xaxis=dict(
                    title="Impressioni",
                    gridcolor='#1f4068',
                    type='log'
                ),
                yaxis=dict(
                    title="CTR %",
                    gridcolor='#1f4068'
                ),
                title={
                    'text': "Dimensione bubble = Volume Clic | Colore = CTR Performance",
                    'x': 0.5,
                    'xanchor': 'center',
                    'font': {'size': 13, 'color': '#94a3b8'}
                }
            )
            
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Nessun mercato opportunità trovato")

# ============================================
# TAB 3: INTENT - CON DOWNLOAD CSV
# ============================================
with tab3:
    st.markdown("### 🎯 Classificazione Intenti Query")
    
    if st.session_state.queries_data is not None:
        queries_df = st.session_state.queries_data.copy()
        
        brand_filter = st.selectbox("Filtro Brand", ['Tutte', 'Solo Brand', 'Solo Non-Brand'])
        
        if brand_filter == 'Solo Brand' and st.session_state.brand_keyword:
            queries_df = queries_df[queries_df['Query'].str.lower().str.contains(st.session_state.brand_keyword, na=False)]
        elif brand_filter == 'Solo Non-Brand' and st.session_state.brand_keyword:
            queries_df = queries_df[~queries_df['Query'].str.lower().str.contains(st.session_state.brand_keyword, na=False)]
        
        intents = classify_query_intents_improved(queries_df)
        
        total_queries = len(queries_df)
        
        comm_pct = (len(intents['commercial']) / total_queries * 100) if total_queries > 0 else 0
        info_pct = (len(intents['informational']) / total_queries * 100) if total_queries > 0 else 0
        trans_pct = (len(intents['transactional']) / total_queries * 100) if total_queries > 0 else 0
        nav_pct = (len(intents['navigational']) / total_queries * 100) if total_queries > 0 else 0
        
        st.info(f"📊 **Query totali**: {total_queries:,} | Commerciali: {len(intents['commercial'])} ({comm_pct:.1f}%) | "
                f"Informazionali: {len(intents['informational'])} ({info_pct:.1f}%) | "
                f"Transazionali: {len(intents['transactional'])} ({trans_pct:.1f}%) | "
                f"Navigazionali: {len(intents['navigational'])} ({nav_pct:.1f}%)")
        
        st.markdown("---")
        
        # DOWNLOAD CSV TUTTE LE QUERY
        st.markdown("### 📥 Download Query Classificate")
        
        all_classified = []
        for intent_type, intent_df in intents.items():
            if not intent_df.empty:
                temp_df = intent_df.copy()
                temp_df['Intent'] = intent_type.upper()
                all_classified.append(temp_df)
        
        if all_classified:
            full_classified_df = pd.concat(all_classified, ignore_index=True)
            full_classified_df = full_classified_df.sort_values('Clicks', ascending=False)
            
            csv_data = full_classified_df.to_csv(index=False, encoding='utf-8-sig')
            st.download_button(
                label=f"📥 Scarica CSV con {len(full_classified_df):,} Query Classificate",
                data=csv_data,
                file_name="query_classificate_per_intent.csv",
                mime="text/csv",
                use_container_width=True
            )
            
            st.success(f"✅ TUTTE le {len(full_classified_df):,} query sono state classificate!")
        
        st.markdown("---")
        
        # CIAMBELLA
        st.markdown("#### 📊 Distribuzione Intenti")
        
        fig = go.Figure(data=[go.Pie(
            labels=['🛒 Commerciale', 'ℹ️ Informazionale', '💳 Transazionale', '🧭 Navigazionale'],
            values=[len(intents['commercial']), len(intents['informational']), 
                   len(intents['transactional']), len(intents['navigational'])],
            hole=0.5,
            marker=dict(colors=[COLOR_PALETTE['chart_colors'][0], COLOR_PALETTE['chart_colors'][1], 
                               COLOR_PALETTE['chart_colors'][2], COLOR_PALETTE['chart_colors'][3]]),
            textinfo='label+percent',
            textfont=dict(size=14, color='white'),
            hovertemplate='<b>%{label}</b><br>Query: %{value}<br>Percentuale: %{percent}<extra></extra>'
        )])
        
        fig.update_layout(
            template="plotly_dark",
            plot_bgcolor='#16213e',
            paper_bgcolor='#16213e',
            font=dict(color='#e0e7ff'),
            height=500,
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        
        # PREVIEW TOP 5
        st.markdown("### 📋 Preview Query per Intento (Top 5)")
        st.markdown("*Mostrando le prime 5 query per categoria. Scarica il CSV per vedere tutte.*")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🛒 Commerciale")
            if not intents['commercial'].empty:
                top_comm = intents['commercial'].nlargest(5, 'Clicks')
                st.markdown(f"*Top 5 di {len(intents['commercial'])} query totali*")
                
                for idx, row in top_comm.iterrows():
                    st.markdown(f"**{row['Query']}**")
                    st.caption(f"Clic: {row['Clicks']:,} | CTR: {row['CTR']:.2f}% | Pos: {row['Position']:.1f}")
            else:
                st.info("Nessuna query commerciale")
        
        with col2:
            st.markdown("#### ℹ️ Informazionale")
            if not intents['informational'].empty:
                top_info = intents['informational'].nlargest(5, 'Clicks')
                st.markdown(f"*Top 5 di {len(intents['informational'])} query totali*")
                
                for idx, row in top_info.iterrows():
                    st.markdown(f"**{row['Query']}**")
                    st.caption(f"Clic: {row['Clicks']:,} | CTR: {row['CTR']:.2f}% | Pos: {row['Position']:.1f}")
            else:
                st.info("Nessuna query informazionale")
        
        col3, col4 = st.columns(2)
        
        with col3:
            st.markdown("#### 💳 Transazionale")
            if not intents['transactional'].empty:
                top_trans = intents['transactional'].nlargest(5, 'Clicks')
                st.markdown(f"*Top 5 di {len(intents['transactional'])} query totali*")
                
                for idx, row in top_trans.iterrows():
                    st.markdown(f"**{row['Query']}**")
                    st.caption(f"Clic: {row['Clicks']:,} | CTR: {row['CTR']:.2f}% | Pos: {row['Position']:.1f}")
            else:
                st.info("Nessuna query transazionale")
        
        with col4:
            st.markdown("#### 🧭 Navigazionale")
            if not intents['navigational'].empty:
                top_nav = intents['navigational'].nlargest(5, 'Clicks')
                st.markdown(f"*Top 5 di {len(intents['navigational'])} query totali*")
                
                for idx, row in top_nav.iterrows():
                    st.markdown(f"**{row['Query']}**")
                    st.caption(f"Clic: {row['Clicks']:,} | CTR: {row['CTR']:.2f}% | Pos: {row['Position']:.1f}")
            else:
                st.info("Nessuna query navigazionale")

# ============================================
# TAB 4: BUSINESS
# ============================================
with tab4:
    st.markdown("### 🏢 Performance Categorie URL")
    
    if st.session_state.pages_data is not None:
        pages_df = st.session_state.pages_data.copy()
        
        cols = st.columns(2)
        with cols[0]:
            cat_metric = st.selectbox("Metrica", ['Clicks', 'Impressions'], key='cat_metric')
        with cols[1]:
            exclude = st.selectbox("Escludi", ['Nessuna', 'Homepage'])
        
        categories = categorize_urls_advanced(pages_df)
        
        category_data = {}
        for cat_name, cat_df in categories.items():
            if not cat_df.empty:
                category_data[cat_name] = cat_df[cat_metric].sum()
        
        if exclude == 'Homepage' and 'Homepage' in category_data:
            del category_data['Homepage']
        
        if category_data:
            fig = go.Figure(data=[go.Pie(
                labels=list(category_data.keys()),
                values=list(category_data.values()),
                hole=0.5,
                marker=dict(colors=COLOR_PALETTE['chart_colors'][:len(category_data)]),
                textinfo='label+percent',
                textfont=dict(size=14, color='white')
            )])
            
            fig.update_layout(
                template="plotly_dark",
                plot_bgcolor='#16213e',
                paper_bgcolor='#16213e',
                font=dict(color='#e0e7ff'),
                height=450
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        st.markdown("### 💎 Opportunità SEO Premium")
        
        if st.session_state.queries_data is not None:
            opp_df = st.session_state.queries_data.copy()
            
            cols = st.columns(3)
            with cols[0]:
                opp_brand = st.selectbox("Filtro", ['Tutte', 'Solo Non-Brand'], key='opp_brand')
            with cols[1]:
                min_imp = st.number_input("Min Impressioni", min_value=0, value=1000, step=100)
            with cols[2]:
                max_ctr = st.number_input("Max CTR (%)", min_value=0.0, value=3.0, step=0.1)
            
            if opp_brand == 'Solo Non-Brand' and st.session_state.brand_keyword:
                opp_df = opp_df[~opp_df['Query'].str.lower().str.contains(st.session_state.brand_keyword, na=False)]
            
            opportunities = opp_df[
                (opp_df['Impressions'] >= min_imp) &
                (opp_df['CTR'] <= max_ctr)
            ].nlargest(15, 'Impressions')
            
            if not opportunities.empty:
                for _, opp in opportunities.iterrows():
                    position = opp['Position']
                    current_ctr = opp['CTR']
                    
                    # CTR baseline realistici da studi Backlinko/Sistrix
                    ctr_benchmarks = {
                        1: 28.5, 2: 15.7, 3: 11.0, 4: 8.0, 5: 7.2,
                        6: 5.1, 7: 4.0, 8: 3.2, 9: 2.8, 10: 2.5
                    }
                    
                    # Calcola baseline per posizione
                    if position <= 1:
                        baseline = ctr_benchmarks[1]
                    elif position <= 10:
                        baseline = ctr_benchmarks[int(position)]
                    elif position <= 20:
                        baseline = 1.5
                    elif position <= 30:
                        baseline = 0.8
                    else:
                        baseline = 0.5
                    
                    # Se CTR attuale è vicino al baseline, target conservativo
                    if current_ctr >= baseline * 0.85:
                        target_ctr = current_ctr * 1.15  # +15% improvement
                    else:
                        # Calcola target intermedio tra CTR attuale e baseline
                        gap = baseline - current_ctr
                        target_ctr = current_ctr + (gap * 0.6)  # 60% del gap
                    
                    # Cap massimo realistico
                    max_realistic_ctr = baseline * 1.3
                    target_ctr = min(target_ctr, max_realistic_ctr)
                    target_ctr = round(target_ctr, 2)
                    
                    potential_clicks = int((opp['Impressions'] * target_ctr / 100) - opp['Clicks'])
                    improvement = ((target_ctr - current_ctr) / current_ctr * 100) if current_ctr > 0 else 100
                    
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, rgba(0, 212, 255, 0.1), rgba(78, 205, 196, 0.1)); 
                         border: 2px solid {COLOR_PALETTE['primary']}; border-radius: 15px; padding: 20px; margin-bottom: 15px;">
                        <div style="font-size: 1.3rem; font-weight: 600; color: {COLOR_PALETTE['primary']}; margin-bottom: 10px;">
                            💎 {opp['Query']}
                        </div>
                        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; margin-bottom: 15px;">
                            <div style="text-align: center;">
                                <div style="font-size: 1.5rem; font-weight: 700; color: {COLOR_PALETTE['primary']};">{opp['Impressions']:,}</div>
                                <div style="color: #e0e7ff; font-size: 0.9rem;">Impressioni</div>
                            </div>
                            <div style="text-align: center;">
                                <div style="font-size: 1.5rem; font-weight: 700; color: {COLOR_PALETTE['primary']};">{opp['Clicks']:,}</div>
                                <div style="color: #e0e7ff; font-size: 0.9rem;">Clic</div>
                            </div>
                            <div style="text-align: center;">
                                <div style="font-size: 1.5rem; font-weight: 700; color: {COLOR_PALETTE['primary']};">{current_ctr:.2f}%</div>
                                <div style="color: #e0e7ff; font-size: 0.9rem;">CTR</div>
                            </div>
                            <div style="text-align: center;">
                                <div style="font-size: 1.5rem; font-weight: 700; color: {COLOR_PALETTE['primary']};">{opp['Position']:.1f}</div>
                                <div style="color: #e0e7ff; font-size: 0.9rem;">Posizione</div>
                            </div>
                        </div>
                        <div style="background: rgba(78, 205, 196, 0.2); padding: 15px; border-radius: 10px; border-left: 4px solid {COLOR_PALETTE['secondary']};">
                            <div style="color: {COLOR_PALETTE['secondary']}; font-weight: 600; font-size: 1rem;">
                                🚀 CTR Target: {target_ctr:.1f}% (+{improvement:.0f}%)
                            </div>
                            <div style="color: white; font-size: 1.2rem; font-weight: 700; margin-top: 8px;">
                                Potenziale: +{potential_clicks if potential_clicks > 0 else 0:,} clic
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("Nessuna opportunità trovata")

# ============================================
# FOOTER
# ============================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #94a3b8; font-style: italic;">
    Fatto con amore per la SEO 💖 | Made by Maria Paloschi
</div>
""", unsafe_allow_html=True)
