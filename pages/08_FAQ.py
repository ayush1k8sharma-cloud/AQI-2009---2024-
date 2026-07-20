import streamlit as st
from Theme import get_theme, inject_theme_css, render_sidebar, render_footer

st.set_page_config(page_title="FAQ — India AQI Dashboard", page_icon="❓", layout="wide")
t = get_theme(); inject_theme_css(t)

# Sidebar without year filter for FAQ
with st.sidebar:
    st.markdown(f"<h2 style='color:{t['TEXT']};margin:0'>🌿 India AQI</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:{t['SUBTEXT']};margin:0 0 12px 0'>Dashboard</p>", unsafe_allow_html=True)
    st.markdown("---")
    if st.button(
        "☀️ Switch to Light Mode" if t['is_dark'] else "🌙 Switch to Dark Mode",
        use_container_width=True
    ):
        st.session_state.theme = 'light' if t['is_dark'] else 'dark'
        st.rerun()
    st.markdown("---")
    st.markdown(
        f"<div style='font-size:0.75rem;color:{t['SUBTEXT']};text-align:center'>"
        "Made by <b>Ayush Sharma</b><br>"
        "DAVIET • Roll: 2513533<br>CSE AI/ML</div>",
        unsafe_allow_html=True
    )

# Header
st.markdown(f"""
<div style='margin-bottom:24px;'>
    <p style='color:{t['ACCENT']};font-size:0.85rem;font-weight:700;letter-spacing:4px;margin-bottom:4px;'>HELP & INFORMATION</p>
    <h1 style='font-family:Poppins;font-size:2.2rem;font-weight:700;color:{t['TEXT']};margin:0;'>❓ Frequently Asked Questions</h1>
    <p style='color:{t['SUBTEXT']};font-size:0.95rem;margin-top:8px;'>Everything you need to know about AQI, this dashboard, the dataset and the analysis methodology.</p>
</div>""", unsafe_allow_html=True)
st.markdown("---")

# Helper
def faq_card(question, answer, color=None):
    border = color if color else t['ACCENT']
    with st.expander(f"  {question}"):
        st.markdown(f"""
        <div style='background:{"#0A0F1E" if t['is_dark'] else "#F8FAFC"};
                    border-left:4px solid {border};border-radius:8px;
                    padding:16px 20px;font-size:0.92rem;color:{t['SUBTEXT']};line-height:1.8;'>
            {answer}
        </div>""", unsafe_allow_html=True)

# ── ABOUT AQI ─────────────────────────────────
st.markdown("<div class='section-title'>🌿 About AQI</div>", unsafe_allow_html=True)

faq_card("What is AQI (Air Quality Index)?",
f"""The <b style='color:{t['TEXT']}'>Air Quality Index (AQI)</b> is a standardized scale from
<b style='color:{t['TEXT']}'>0 to 500</b> used by governments to measure and communicate air
pollution levels to the public.<br><br>
Just like a thermometer measures temperature, AQI measures how clean or polluted the air is
and what health effects might be a concern.<br><br>
<b style='color:{t['TEXT']}'>Scale:</b><br>
🟢 0–50 → Good &nbsp;&nbsp;
🟡 51–100 → Satisfactory &nbsp;&nbsp;
🟡 101–200 → Moderate<br>
🟠 201–300 → Poor &nbsp;&nbsp;
🔴 301–400 → Very Poor &nbsp;&nbsp;
🟤 401–500 → Severe""")

faq_card("How is AQI calculated in this dashboard?",
f"""Since our dataset contains raw pollutant concentrations but no pre-calculated AQI,
we calculate AQI from <b style='color:{t['TEXT']}'>PM2.5</b> using the standard
<b style='color:{t['TEXT']}'>US EPA (Environmental Protection Agency) formula</b>.<br><br>
We chose PM2.5 because:<br>
• Its correlation with AQI is <b style='color:{t['TEXT']}'>0.95</b> — near perfect<br>
• It is the most health-impactful pollutant in India<br>
• It is available across all 483 monitoring stations<br><br>
The formula maps PM2.5 concentration ranges to AQI ranges using linear interpolation
between breakpoints — the same method used by CPCB and US EPA officially.""")

faq_card("What is the difference between PM2.5 and PM10?",
f"""Both are <b style='color:{t['TEXT']}'>particulate matter</b> — tiny solid or liquid
particles suspended in air. The number refers to size:<br><br>
<b style='color:{t['TEXT']}'>PM2.5</b> → particles smaller than 2.5 micrometres (30x thinner than human hair)<br>
• Can enter the bloodstream directly<br>
• Causes heart attacks, strokes, lung cancer<br>
• WHO safe limit: 5 µg/m³ — India avg is <b style='color:#E63946'>11x over limit</b><br><br>
<b style='color:{t['TEXT']}'>PM10</b> → particles smaller than 10 micrometres<br>
• Gets trapped in nose and upper airways<br>
• Causes asthma, respiratory infections<br>
• WHO safe limit: 15 µg/m³ — India avg is <b style='color:#E63946'>8x over limit</b>""")

faq_card("Why is PM2.5 the primary pollutant used?",
f"""PM2.5 is the <b style='color:{t['TEXT']}'>primary driver of AQI in India</b> because:<br><br>
• Correlation with AQI: <b style='color:{t['TEXT']}'>0.95</b> — strongest of all pollutants<br>
• PM10 correlation is 0.79 (second strongest)<br>
• Gases like SO2 (0.12), CO (0.11), Ozone (0.13) are weakly correlated<br><br>
In simpler terms — when PM2.5 goes up, AQI goes up almost exactly proportionally.
No other pollutant shows this strength of relationship in our dataset.""")

st.markdown("<br>", unsafe_allow_html=True)

# ── ABOUT DATASET ─────────────────────────────
st.markdown("<div class='section-title'>📁 About the Dataset</div>", unsafe_allow_html=True)

faq_card("Where does the data come from?",
f"""The data is sourced from the <b style='color:{t['TEXT']}'>Central Pollution Control Board (CPCB)</b>
of India — the official government body responsible for monitoring air quality.<br><br>
It was accessed via <b style='color:{t['TEXT']}'>Kaggle</b> (dataset by omsandeeppatil:
indian-aqi-stations) and covers:<br>
• <b style='color:{t['TEXT']}'>483 monitoring stations</b> across India<br>
• <b style='color:{t['TEXT']}'>240 cities</b> in 20 states<br>
• <b style='color:{t['TEXT']}'>2009 to 2024</b> — 15 years of hourly readings<br>
• <b style='color:{t['TEXT']}'>7,38,097</b> daily readings after processing""")

faq_card("How was the raw data processed?",
f"""The dataset came as <b style='color:{t['TEXT']}'>546 separate CSV files</b>
— one per monitoring station — organized in 20 state folders.<br><br>
Processing steps:<br>
1️⃣ Loaded all 546 files using <b style='color:{t['TEXT']}'>glob</b> and <b style='color:{t['TEXT']}'>pandas</b><br>
2️⃣ Selected only 8 essential columns to save memory (PM2.5, PM10, NO2, SO2, CO, Ozone, NH3, timestamp)<br>
3️⃣ Converted hourly readings to <b style='color:{t['TEXT']}'>daily averages</b> using resample('D').mean()<br>
4️⃣ Merged all 546 files into one master dataframe using pd.concat()<br>
5️⃣ Merged with stations.csv to add city, state and GPS coordinates<br>
6️⃣ Calculated AQI from PM2.5 using US EPA formula<br>
7️⃣ Saved as <b style='color:{t['TEXT']}'>Parquet format</b> for fast loading""")

faq_card("What does PCBA mean in the dataset?",
f"""<b style='color:{t['TEXT']}'>PCBA stands for Pollution Control Board Area</b> —
it is not a city name but a <b style='color:{t['TEXT']}'>monitoring zone classification</b>
used by CPCB.<br><br>
A PCBA station is placed directly next to a heavily polluting industrial cluster
(steel plant, chemical factory, thermal power station) to track point-source industrial emissions.<br><br>
This is why PCBA (station UN82) shows the highest AQI of ~197 —
it measures worst-case industrial zone air, not residential city air.
It should be interpreted separately from city-level comparisons.""")

faq_card("Why do some stations have less data than others?",
f"""Different stations came online at different times.<br><br>
• Early stations (2009–2014): Limited to major cities like Delhi, Mumbai<br>
• 2015 onwards: Massive expansion under <b style='color:{t['TEXT']}'>NCAP (National Clean Air Programme)</b><br>
• Some stations had equipment failures or maintenance gaps<br>
• Maharashtra stations (MH21–MH53) had corrupted files and were skipped<br><br>
This is why the 2009–2014 box plots appear flatter — less data from fewer stations,
mostly in polluted urban areas.""")

st.markdown("<br>", unsafe_allow_html=True)

# ── ABOUT FINDINGS ────────────────────────────
st.markdown("<div class='section-title'>📊 About the Findings</div>", unsafe_allow_html=True)

faq_card("Why is North India more polluted than South India?",
f"""Three main factors create the North-South pollution divide:<br><br>
<b style='color:{t['TEXT']}'>1. Geography</b><br>
The Indo-Gangetic Plain (Delhi, Punjab, UP, Bihar) is a flat bowl-shaped geography where
pollutants cannot disperse. The Himalayas block northward airflow, trapping pollution at ground level.<br><br>
<b style='color:{t['TEXT']}'>2. Agriculture</b><br>
Punjab and Haryana burn 30+ million tonnes of crop stubble every October–November,
releasing massive PM2.5 that spreads across the entire North India belt.<br><br>
<b style='color:{t['TEXT']}'>3. Industrialization</b><br>
Heavy industries (steel, coal, fertilizers, brick kilns) are concentrated in North India.
Southern states have cleaner industries (IT, textiles, tourism).""")

faq_card("Why did AQI drop in 2020?",
f"""The <b style='color:{t['TEXT']}'>COVID-19 lockdown (March–June 2020)</b> caused an
unprecedented shutdown of:<br><br>
• All factories and industrial activity<br>
• Vehicle movement (roads were empty for weeks)<br>
• Construction activity<br>
• Domestic flights and railways<br><br>
This reduced India's national average AQI by approximately
<b style='color:{t['TEXT']}'>15%</b> within weeks — definitively proving that human
industrial and vehicular activity is the primary driver of air pollution.<br><br>
The 2020 dip is visible in every chart in this dashboard.""")

faq_card("Why is November always the worst month?",
f"""November combines two pollution sources simultaneously:<br><br>
<b style='color:{t['TEXT']}'>1. Paddy Stubble Burning 🌾</b><br>
After rice harvest in October–November, farmers in Punjab and Haryana burn crop residue
to quickly clear fields. This releases massive PM2.5, PM10, CO and NH3 across North India.<br><br>
<b style='color:{t['TEXT']}'>2. Temperature Inversion ❄️</b><br>
In winter, cold dense air near the ground gets trapped under warmer air above —
like a lid on a pot. This prevents pollutants from rising and dispersing,
concentrating everything at breathing level.<br><br>
When crop burning smoke meets temperature inversion in November,
AQI spikes to dangerous levels across the entire North India belt.""")

faq_card("Is India's air quality actually improving?",
f"""The data shows <b style='color:{t['TEXT']}'>cautious optimism</b>:<br><br>
✅ Overall AQI declined from ~120 (2009) to ~113 (2024) — a 7-point improvement<br>
✅ NO2 levels declined by 44% over 15 years — biggest improvement<br>
✅ Satisfactory category days increased from 0% to 38% since 2015<br>
✅ Good category days increased from 0% to 8% by 2024<br><br>
❌ PM2.5 is still 11x above WHO safe limit<br>
❌ PM10 is still 8x above WHO safe limit<br>
❌ Punjab's November spike continues unabated every year<br>
❌ 57.5% of days are still in the Moderate category<br><br>
<b style='color:{t['TEXT']}'>Verdict:</b> Slow but real improvement — but India still has
decades of work ahead to reach WHO safe levels.""")

st.markdown("<br>", unsafe_allow_html=True)

# ── ABOUT PROJECT ─────────────────────────────
st.markdown("<div class='section-title'>🎓 About This Project</div>", unsafe_allow_html=True)

faq_card("What tools and technologies were used?",
f"""<b style='color:{t['TEXT']}'>Programming Language:</b> Python 3<br><br>
<b style='color:{t['TEXT']}'>Data Processing:</b><br>
• Pandas — data loading, cleaning, merging 546 CSV files<br>
• NumPy — numerical computations and AQI calculations<br>
• Glob / OS — recursive file loading from 20 state folders<br><br>
<b style='color:{t['TEXT']}'>Visualization:</b><br>
• Plotly — all interactive charts and maps<br>
• Seaborn + Matplotlib — static charts in Jupyter analysis<br><br>
<b style='color:{t['TEXT']}'>Dashboard:</b><br>
• Streamlit — web app framework<br>
• Custom CSS — dark/light theme, Google Fonts (Poppins, Inter, Orbitron)<br><br>
<b style='color:{t['TEXT']}'>Storage:</b><br>
• Parquet format — for fast data loading (546 CSVs → 1 parquet file)""")

faq_card("What analysis phases were completed?",
f"""The project was structured into <b style='color:{t['TEXT']}'>8 analysis phases</b>:<br><br>
📌 Phase 1 — Data Loading (546 CSV files across 20 state folders)<br>
📌 Phase 2 — Data Cleaning (missing values, AQI calculation, feature engineering)<br>
📌 Phase 3 — National AQI Trend (2009–2024 yearly analysis)<br>
📌 Phase 4 — State & City Analysis (20 states, 240 cities compared)<br>
📌 Phase 5 — Station Deep Dive (483 individual stations analyzed)<br>
📌 Phase 6 — Seasonal Patterns (monthly, seasonal, year×month heatmap)<br>
📌 Phase 7 — Pollutant Analysis (7 pollutants, correlations, trends)<br>
📌 Phase 8 — AQI Categories (Good to Severe distribution analysis)<br><br>
Total: <b style='color:{t['TEXT']}'>21 charts</b> generated across all phases.""")

faq_card("What are the limitations of this project?",
f"""<b style='color:{t['TEXT']}'>Data Limitations:</b><br>
• AQI is calculated from PM2.5 only — official CPCB uses multiple pollutants<br>
• Maharashtra stations (MH21–MH53) had corrupted files and were excluded<br>
• Some stations have gaps in data especially before 2015<br>
• Data is historical (up to 2024) — not real-time<br><br>
<b style='color:{t['TEXT']}'>Future Improvements:</b><br>
• Connect to CPCB API for real-time AQI updates<br>
• Add ML model to predict next-day AQI<br>
• Include choropleth state map with GeoJSON boundaries<br>
• Add weather data (temperature, humidity, wind) as additional features""")

st.markdown("<br>", unsafe_allow_html=True)


render_footer(t)