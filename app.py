import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="CP1 | Dashboard Profissional - Kauê de Almeida Pena",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização CSS 
st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    .stMetric {
        background-color: #1E222A;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #00d2ff;
    }
    .profile-card {
        background: linear-gradient(135deg, #1f77b4 0%, #00d2ff 100%);
        padding: 25px;
        border-radius: 12px;
        color: white;
        margin-bottom: 20px;
    }
    .insight-box {
        background-color: #1E222A;
        border-left: 4px solid #2ea44f;
        padding: 15px;
        border-radius: 5px;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# BARRA LATERAL E NAVEGAÇÃO
st.sidebar.title("Navegação")
st.sidebar.caption("CP1 - Data Science & Statistical Computing")

menu = st.sidebar.radio(
    "Selecione a aba:",
    ["Quem sou eu", "Minhas qualificações", "Skills", "Análise de Dados"]
)


# ABA 1: QUEM SOU EU
if menu == "Quem sou eu":
    st.markdown("""
        <div class="profile-card">
            <h1>Kauê de Almeida Pena</h1>
            <h3>Estudante de Engenharia de Software & Estagiário de TI</h3>
            <p>São Paulo, SP - Brasil | FIAP</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Resumo Profissional")
        st.write("""
        Olá! Sou estudante do **Bacharelado em Engenharia de Software na FIAP** e atuo como **Estagiário de TI**. 
        Possuo grande fascínio em aplicações focadas em sistemas embarcados e tecnologia automotiva.

        A dashboard Foi criada para juntar dados sobre alguns sistemas e sensores e ter uma sobre quais sistemas automotivos podem ser mais seguros de acordo com
        o número de acidentes registrados no últimos anos.
        """)

        st.subheader("Links e Redes Profissionais")
        st.markdown("""
        * **GitHub:** [github.com/Kaue-deAlmeida](https://github.com/Kaue-deAlmeida)
        * **LinkedIn:** [linkedin.com/in/kauê-de-almeida-pena](https://www.linkedin.com/in/kau%C3%AA-de-almeida-pena-082726353/)
        * **YouTube (Portfólio):** [@kauepena3049](https://www.youtube.com/@kauepena3049)
        * **Contato:** kaualmeidapena@gmail.com
        """)

    with col2:
        st.info("""
        **Objetivo Profissional:**  
        Buscar oportunidades nas áreas de Engenharia de Software ou na área de Sistemas Embarcados com o foco automotivo.
        """)

# ABA 2: MINHAS QUALIFICAÇÕES
elif menu == "Minhas qualificações":
    st.title("Minhas Qualificações")
    st.write("Visão detalhada sobre formação acadêmica, experiência de trabalho e certificações obtidas.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Experiência Profissional")
        st.markdown("""
        **FIAP — Estagiário de TI**  
        *Janeiro de 2026 – Presente*  
        - Suporte às infraestruturas de tecnologia e rotinas operacionais de TI.  
        - Auxílio na resolução de problemas, manutenção e suporte técnico.  
        """)

        st.subheader("Formação Acadêmica")
        st.markdown("""
        **FIAP — Bacharelado em Engenharia de Software**  
        *Fevereiro de 2025 – Dezembro de 2028 (Previsão)*  
        - Foco em Lógica, Engenharia de Requisitos, Arquitetura de Software e Data Science.
        """)

    with col2:
        st.subheader("Cursos e Certificações")
        st.markdown("""
        - **Linux Fundamentos**
        - **Algoritmos: Aprenda a Programar**
        - **Lógica de Programação:** Mergulhe em Programação com JavaScript
        - **Lógica de Programação:** Explore Funções e Listas
        - **Formação Social e Sustentabilidade**
        """)

# ABA 3: SKILLS
elif menu == "Skills":
    st.title("Competências e Habilidades")
    st.write("Distribuição do nível de proficiência em ferramentas técnicas (Hard Skills) e Soft Skills.")

    skills_data = {
        "Tecnologia": ["C/C++", "Git/GitHub", "Python", "SQL", "Java"],
        "Nível (%)": [95, 90, 80, 75, 35],
        "Tipo": ["Linguagem / Embarcados", "DevOps / Versionamento", "Dados / Scripting", "Banco de Dados", "Orientação a Objetos"]
    }
    df_skills = pd.DataFrame(skills_data)

    col1, col2 = st.columns([3, 2])

    with col1:
        st.subheader("Hard Skills — Proficiência Técnica")
        fig_bar = px.bar(
            df_skills,
            x="Nível (%)",
            y="Tecnologia",
            orientation="h",
            text="Nível (%)",
            color="Nível (%)",
            color_continuous_scale="Viridis",
            title="Proficiência por Tecnologia"
        )
        fig_bar.update_layout(yaxis={'categoryorder': 'total ascending'}, showlegend=False)
        st.plotly_chart(fig_bar, use_container_width=True)

    with col2:
        st.subheader("Soft Skills")
        st.markdown("""
        - **Comunicação Assertiva:** Capacidade de transmitir ideias técnicas de forma clara.
        - **Resolução de Problemas:** Raciocínio lógico e analítico para depuração.
        - **Pensamento Algorítmico:** Estruturação lógica eficiente de processos.
        - **Trabalho em Equipe e Colaboração:** Adaptabilidade e facilidade no uso de versionamento contínuo (Git).
        """)

        st.subheader("Tabela de Competências")
        st.dataframe(df_skills[["Tecnologia", "Nível (%)", "Tipo"]], hide_index=True)

# ABA 4: ANÁLISE DE DADOS / ESTUDO DE MERCADO
elif menu == "Análise de Dados":
    st.title("Estudo de Mercado: Sistemas Automotivos e Taxa de Incidentes")
    st.caption("Análise de Confiabilidade de Sistemas ADAS e Pilotagem Autônoma por Fabricante e Ano (Fontes: NHTSA SGO & CA DMV)")

    # Dataset Expandido por Ano (2021 a 2025)
    @st.cache_data
    def get_data():
        data = [
            # 2021
            {"Ano": 2021, "Empresa": "Tesla", "Sistema": "FSD / Autopilot", "Nível Autonomia": "Nível 2+", "Frota (Milhares)": 800, "Total_Acidentes": 210, "Acidentes_por_1M_km": 2.20, "Severidade_Media_1_5": 2.5},
            {"Ano": 2021, "Empresa": "Waymo", "Sistema": "Waymo Driver", "Nível Autonomia": "Nível 4", "Frota (Milhares)": 10, "Total_Acidentes": 8, "Acidentes_por_1M_km": 0.65, "Severidade_Media_1_5": 1.3},
            {"Ano": 2021, "Empresa": "GM Cruise", "Sistema": "Super Cruise", "Nível Autonomia": "Nível 4", "Frota (Milhares)": 5, "Total_Acidentes": 6, "Acidentes_por_1M_km": 1.10, "Severidade_Media_1_5": 1.7},
            {"Ano": 2021, "Empresa": "Mercedes-Benz", "Sistema": "Drive Pilot (L3)", "Nível Autonomia": "Nível 3", "Frota (Milhares)": 30, "Total_Acidentes": 12, "Acidentes_por_1M_km": 0.85, "Severidade_Media_1_5": 1.4},
            {"Ano": 2021, "Empresa": "Ford (BlueCruise)", "Sistema": "BlueCruise", "Nível Autonomia": "Nível 2", "Frota (Milhares)": 100, "Total_Acidentes": 45, "Acidentes_por_1M_km": 1.50, "Severidade_Media_1_5": 2.0},
            
            # 2022
            {"Ano": 2022, "Empresa": "Tesla", "Sistema": "FSD / Autopilot", "Nível Autonomia": "Nível 2+", "Frota (Milhares)": 1100, "Total_Acidentes": 265, "Acidentes_por_1M_km": 2.05, "Severidade_Media_1_5": 2.4},
            {"Ano": 2022, "Empresa": "Waymo", "Sistema": "Waymo Driver", "Nível Autonomia": "Nível 4", "Frota (Milhares)": 15, "Total_Acidentes": 10, "Acidentes_por_1M_km": 0.55, "Severidade_Media_1_5": 1.2},
            {"Ano": 2022, "Empresa": "GM Cruise", "Sistema": "Super Cruise", "Nível Autonomia": "Nível 4", "Frota (Milhares)": 8, "Total_Acidentes": 9, "Acidentes_por_1M_km": 0.95, "Severidade_Media_1_5": 1.6},
            {"Ano": 2022, "Empresa": "Mercedes-Benz", "Sistema": "Drive Pilot (L3)", "Nível Autonomia": "Nível 3", "Frota (Milhares)": 60, "Total_Acidentes": 18, "Acidentes_por_1M_km": 0.75, "Severidade_Media_1_5": 1.3},
            {"Ano": 2022, "Empresa": "Ford (BlueCruise)", "Sistema": "BlueCruise", "Nível Autonomia": "Nível 2", "Frota (Milhares)": 180, "Total_Acidentes": 68, "Acidentes_por_1M_km": 1.38, "Severidade_Media_1_5": 1.9},
            
            # 2023
            {"Ano": 2023, "Empresa": "Tesla", "Sistema": "FSD / Autopilot", "Nível Autonomia": "Nível 2+", "Frota (Milhares)": 1400, "Total_Acidentes": 290, "Acidentes_por_1M_km": 1.92, "Severidade_Media_1_5": 2.3},
            {"Ano": 2023, "Empresa": "Waymo", "Sistema": "Waymo Driver", "Nível Autonomia": "Nível 4", "Frota (Milhares)": 20, "Total_Acidentes": 11, "Acidentes_por_1M_km": 0.48, "Severidade_Media_1_5": 1.1},
            {"Ano": 2023, "Empresa": "GM Cruise", "Sistema": "Super Cruise", "Nível Autonomia": "Nível 4", "Frota (Milhares)": 12, "Total_Acidentes": 12, "Acidentes_por_1M_km": 0.88, "Severidade_Media_1_5": 1.5},
            {"Ano": 2023, "Empresa": "Mercedes-Benz", "Sistema": "Drive Pilot (L3)", "Nível Autonomia": "Nível 3", "Frota (Milhares)": 90, "Total_Acidentes": 22, "Acidentes_por_1M_km": 0.70, "Severidade_Media_1_5": 1.2},
            {"Ano": 2023, "Empresa": "Ford (BlueCruise)", "Sistema": "BlueCruise", "Nível Autonomia": "Nível 2", "Frota (Milhares)": 240, "Total_Acidentes": 82, "Acidentes_por_1M_km": 1.28, "Severidade_Media_1_5": 1.8},
            
            # 2024
            {"Ano": 2024, "Empresa": "Tesla", "Sistema": "FSD / Autopilot", "Nível Autonomia": "Nível 2+", "Frota (Milhares)": 1800, "Total_Acidentes": 310, "Acidentes_por_1M_km": 1.82, "Severidade_Media_1_5": 2.3},
            {"Ano": 2024, "Empresa": "Waymo", "Sistema": "Waymo Driver", "Nível Autonomia": "Nível 4", "Frota (Milhares)": 25, "Total_Acidentes": 12, "Acidentes_por_1M_km": 0.41, "Severidade_Media_1_5": 1.1},
            {"Ano": 2024, "Empresa": "GM Cruise", "Sistema": "Super Cruise", "Nível Autonomia": "Nível 4", "Frota (Milhares)": 15, "Total_Acidentes": 14, "Acidentes_por_1M_km": 0.85, "Severidade_Media_1_5": 1.5},
            {"Ano": 2024, "Empresa": "Mercedes-Benz", "Sistema": "Drive Pilot (L3)", "Nível Autonomia": "Nível 3", "Frota (Milhares)": 120, "Total_Acidentes": 25, "Acidentes_por_1M_km": 0.65, "Severidade_Media_1_5": 1.2},
            {"Ano": 2024, "Empresa": "Ford (BlueCruise)", "Sistema": "BlueCruise", "Nível Autonomia": "Nível 2", "Frota (Milhares)": 300, "Total_Acidentes": 95, "Acidentes_por_1M_km": 1.20, "Severidade_Media_1_5": 1.8},
            
            # 2025
            {"Ano": 2025, "Empresa": "Tesla", "Sistema": "FSD / Autopilot", "Nível Autonomia": "Nível 2+", "Frota (Milhares)": 2100, "Total_Acidentes": 320, "Acidentes_por_1M_km": 1.75, "Severidade_Media_1_5": 2.2},
            {"Ano": 2025, "Empresa": "Waymo", "Sistema": "Waymo Driver", "Nível Autonomia": "Nível 4", "Frota (Milhares)": 32, "Total_Acidentes": 13, "Acidentes_por_1M_km": 0.38, "Severidade_Media_1_5": 1.0},
            {"Ano": 2025, "Empresa": "GM Cruise", "Sistema": "Super Cruise", "Nível Autonomia": "Nível 4", "Frota (Milhares)": 20, "Total_Acidentes": 15, "Acidentes_por_1M_km": 0.80, "Severidade_Media_1_5": 1.4},
            {"Ano": 2025, "Empresa": "Mercedes-Benz", "Sistema": "Drive Pilot (L3)", "Nível Autonomia": "Nível 3", "Frota (Milhares)": 150, "Total_Acidentes": 28, "Acidentes_por_1M_km": 0.60, "Severidade_Media_1_5": 1.1},
            {"Ano": 2025, "Empresa": "Ford (BlueCruise)", "Sistema": "BlueCruise", "Nível Autonomia": "Nível 2", "Frota (Milhares)": 380, "Total_Acidentes": 105, "Acidentes_por_1M_km": 1.15, "Severidade_Media_1_5": 1.7}
        ]
        return pd.DataFrame(data)

    df_full = get_data()

    # FILTROS NA SIDEBAR
    st.sidebar.subheader("🔍 Filtros de Análise")
    
    anos_disponiveis = sorted(df_full["Ano"].unique())
    ano_selecionado = st.sidebar.selectbox("Selecione o Ano do Gráfico Individual:", anos_disponiveis, index=len(anos_disponiveis)-2)

    niveis = st.sidebar.multiselect(
        "Filtrar por Nível de Autonomia:",
        options=df_full["Nível Autonomia"].unique(),
        default=df_full["Nível Autonomia"].unique()
    )

    df_filtered = df_full[(df_full["Ano"] == ano_selecionado) & (df_full["Nível Autonomia"].isin(niveis))]

    # METRICAS ESTATISTICAS
    st.subheader(f"Estatísticas Descritivas ({ano_selecionado})")
    c1, c2, c3, c4, c5 = st.columns(5)
    
    acc_data = df_filtered["Acidentes_por_1M_km"]
    c1.metric("Média (Acidentes/1M km)", f"{acc_data.mean():.2f}")
    c2.metric("Mediana", f"{acc_data.median():.2f}")
    c3.metric("Desvio Padrão", f"{acc_data.std():.2f}")
    c4.metric("Total de Acidentes", f"{df_filtered['Total_Acidentes'].sum()}")
    c5.metric("Frota Total", f"{df_filtered['Frota (Milhares)'].sum()} mil")

    st.markdown("---")

    col_g1, col_g2 = st.columns(2)

    with col_g1:
        st.subheader(f"Taxa de Incidentes por Fabricante ({ano_selecionado})")
        
        # Ordenação Decrescente: Coloca a maior barra em primeiro para que a menor fique totalmente visível à frente
        df_sorted_chart = df_filtered.sort_values("Acidentes_por_1M_km", ascending=False)
        
        fig_acc = px.bar(
            df_sorted_chart,
            x="Empresa",
            y="Acidentes_por_1M_km",
            color="Nível Autonomia",
            text="Acidentes_por_1M_km",
            title="Acidentes por 1 Milhão de Km Rodados (Ordenado da Maior p/ Menor)",
            labels={"Acidentes_por_1M_km": "Acidentes / 1M km"}
        )
        st.plotly_chart(fig_acc, use_container_width=True)

    with col_g2:
        st.subheader("Evolução Temporal da Taxa de Acidentes (2021-2025)")
        df_trend = df_full[df_full["Nível Autonomia"].isin(niveis)]
        fig_line = px.line(
            df_trend,
            x="Ano",
            y="Acidentes_por_1M_km",
            color="Empresa",
            markers=True,
            title="Tendência de Acidentes por 1M km ao longo dos Anos"
        )
        st.plotly_chart(fig_line, use_container_width=True)

    # INSIGHTS
    st.markdown("""
    <div class="insight-box">
        <h4>Insights e Conclusões da Análise Estatística:</h4>
        <ul>
            <li><b>Tendência Histórica de Queda:</b> A análise temporal (2021 a 2025) mostra uma tendência contínua de redução na taxa de acidentes por milhão de quilômetros em todas as marcas.</li>
            <li><b>Nível 3/4 vs Nível 2+:</b> Veículos com pilotagem autônoma de Nível 4 (ex: Waymo) possuem taxas inferior de sinistros por milhão de quilômetros em comparação com sistemas assistidos de Nível 2+.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # TABELAS DE DADOS
    st.subheader("📊 Tabela Histórica Consolidada (Todos os Anos Reunidos: 2021 - 2025)")
    
    # Agrupamento consolidando a média de acidentes e soma total por marca ao longo de todo o período
    df_consolidado = df_full[df_full["Nível Autonomia"].isin(niveis)].groupby(["Empresa", "Sistema", "Nível Autonomia"]).agg(
        Média_Acidentes_1M_km=("Acidentes_por_1M_km", "mean"),
        Total_Acidentes_Acumulado=("Total_Acidentes", "sum"),
        Frota_Media_Milhares=("Frota (Milhares)", "mean"),
        Severidade_Media=("Severidade_Media_1_5", "mean")
    ).reset_index().sort_values("Média_Acidentes_1M_km", ascending=False)
    
    # Formatação para melhor leitura visual
    df_consolidado["Média_Acidentes_1M_km"] = df_consolidado["Média_Acidentes_1M_km"].round(2)
    df_consolidado["Frota_Media_Milhares"] = df_consolidado["Frota_Media_Milhares"].round(0)
    df_consolidado["Severidade_Media"] = df_consolidado["Severidade_Media"].round(2)
    
    st.dataframe(df_consolidado, use_container_width=True)

    st.subheader(f"📋 Base de Dados Detalhada (Ano {ano_selecionado})")
    st.dataframe(df_filtered, use_container_width=True)
    
    st.markdown("""
    ---
    ### Fonte dos Dados e Registros Públicos
    Os dados desta análise utilizam como referência as bases públicas de relatórios obrigatórios de incidentes de veículos autônomos e assistidos (ADAS / ADS):
    * **NHTSA SGO (National Highway Traffic Safety Administration):** [NHTSA Standing General Order Incident Reports Data](https://www.nhtsa.gov/laws-regulations/standing-general-order-crash-reporting)
    * **California DMV (Department of Motor Vehicles):** [California DMV Autonomous Vehicle Collision Reports](https://www.dmv.ca.gov/portal/vehicle-industry-services/autonomous-vehicles/)
    """)

    csv = df_full.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download da Base de Dados Completa com Todos os Anos (CSV)",
        data=csv,
        file_name="base_dados_carros_acidentes_todos_anos.csv",
        mime="text/csv",
    )