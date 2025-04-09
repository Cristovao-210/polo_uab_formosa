import streamlit as st
import pandas as pd
import base64


# Página inicial
def pagina_inicio():
    # st.title("Polo UAB Formosa - GO")
    # st.markdown("### Vídeo de Apresentação")

    # Carrega e codifica o vídeo em base64
    video_file = open("img/Polo-uab-formosa.mp4", "rb")
    video_bytes = video_file.read()
    video_base64 = base64.b64encode(video_bytes).decode()

    # HTML customizado com largura ajustada (ex: 1000px)
    video_html = f"""
        <h1 style:"text-align: center;">Polo UAB Formosa - GO</h1>
        <h4>Vídeo de Apresentação</h4>
        <video width="1000" height="450" controls autoplay loop >
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
            Seu navegador não suporta o vídeo.
        </video>
    """# muted

    # Renderiza o HTML com vídeo customizado
    st.markdown(video_html, unsafe_allow_html=True)    

def exibir_pdf(caminho_pdf, descricao, altura=600):
    st.markdown(f"### {descricao}")
    with open(caminho_pdf, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="{altura}" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)


# Função auxiliar para bloco de curso
def bloco_curso(nome, duracao, modalidade, instituicao, descricao, mais_informacoes):
    with st.expander(nome):
        col1, col2 = st.columns([3,1])
        with col1:
            st.markdown(f"**Duração:** {duracao}")
            st.markdown(f"**Modalidade:** {modalidade}")
            st.markdown(f"**Mais informações:** {mais_informacoes}")
        with col2:
            st.markdown(f"**Instituição:** {instituicao}")
        st.markdown("----")
        st.write(descricao)

# Página de cursos de graduação
def pagina_graduacao():
    st.title("Cursos de Graduação")

    cursos_grad = [
        ("Licenciatura em Ciências Biológicas", "Mínimo 4 anos e Máximo 6 anos", "EAD", "UEG", "Forma professores para atuarem na educação básica, com foco em ecologia, genética, microbiologia e ensino de ciências.", "https://www.ueg.br/cear/conteudo/23819_curso_de_licenciatura_em_ciencias_biologicas"),
        ("Licenciatura em Pedagogia", "4 anos (8 semestres)", "EAD", "IFGoiano", "Capacita profissionais para atuação na educação infantil e nos anos iniciais do ensino fundamental.", "https://ifgoiano.edu.br/home/index.php/curso-superior/22857-licenciatura-em-pedagogia.html"),
        ("Licenciatura em Pedagogia", "Mínimo 4 anos e Máximo 7 anos", "EAD", "UnB", "Curso oferecido com foco em práticas pedagógicas inovadoras e políticas públicas educacionais.", "https://ead.unb.br/cursos/graduacao-ead/2-publicacoes/93-pedagogia"),
        ("Licenciatura em Letras/Inglês", "4 anos", "EAD", "IFB", "Habilita professores de inglês para educação básica, com foco em linguística, literatura e ensino de idiomas.", "https://www.ifb.edu.br/reitori/36237-letras-ingles-uab-licenciatura-na-modalidade-de-educacao-a-distancia"),
        ("Licenciatura em Matemática", "4 anos", "EAD", "IFB", " Formar professores com amplo domínio do conhecimento matemático e responsabilidade social, capaz de problematizar, interferir e construir o conhecimento coletivamente.", "https://ifb.edu.br/reitori/36238-matematica-uab-licenciatura-na-modalidade-de-educacao-a-distancia"),
        ("Tecnólogo em Gestão do Agronegócio", "3 anos", "EAD", "UFCAT", "Forma profissionais para atuar na cadeia produtiva do agronegócio com foco em gestão e logística.", "https://cgen.ufcat.edu.br/sobre-agr"),
        ("Tecnologia em Gestão Comercial", "2 anos e meio", "EAD", "IFG", "O curso de Tecnologia em Gestão Comercial na modalidade de educação a distância tem como objetivo geral formar profissionais com conhecimento e aptidão para a utilização das ferramentas de gestão estratégica e comercial, da logística empresarial, da tecnologia da informação, do marketing e da gestão de projetos, que complementam e viabilizam as estratégias de gestão específicas que impactam nas relações comerciais", "https://www.ifg.edu.br/ultimas-noticias-campus-uruacu/37222-gestao-comercial-ead"),
        ("Tecnologia em Sistemas para Internet", "3 anos", "EAD", "IFMT", "O Tecnólogo em Sistemas para Internet estará apto a desenvolver atividades de análise, projeto, desenvolvimento e implementação de Websites, enfocando áreas de marketing, design e execução de projetos em Internet, atuando também em aplicação de recursos e implementação de computadores e servidores Web.", "https://cread.ifmt.edu.br/conteudo/pagina/curso-de-tecnologia-em-sistemas-para-internet/")
    ]

    for curso in cursos_grad:
        bloco_curso(*curso)

# Página de cursos de especialização
def pagina_especializacao():
    st.title("Cursos de Especialização")

    cursos_esp = [
        ("Educação Inclusiva com Ênfase na Educação de Surdos", "18 meses", "EAD", "IFMT", "Capacita profissionais da educação para inclusão de surdos no ambiente escolar, com foco em LIBRAS e práticas pedagógicas inclusivas.", "https://cread.ifmt.edu.br/conteudo/pagina/esp-educ-inclusiva-enfase-educ-surdos/"),
        ("Educação, Meio Ambiente e Sustentabilidade", "12 meses", "EAD", "IFG", "Tem o objetivo de capacitar docentes e profissionais das mais diversas áreas de formação para desenvolver atividades ligadas à educação, meio ambiente e sustentabilidade, visando a valorização e sustentabilidade de nossos ecossistemas, considerando as demandas sociais atuais.", "https://www.ifg.edu.br/ultimas-noticias/33927-inscricoesmeioambiente"),
        ("Geoprocessamento", "12 meses", "EAD", "UFABC", "Qualificar recursos humanos, especialmente na formação para o desenvolvimento econômico e social local/regional, para uso das tecnologias de geoprocessamento, bem como capacitar profissionais no conhecimento e uso de técnicas de geoprocessamento e suas aplicações nas diversas áreas do conhecimento.", "https://sig.ufabc.edu.br/sigaa/public/curso/portal.jsf?lc=pt_BR&id=2456623"),
        ("Análises Químicas Ambientais", "12 meses", "EAD", "UFCAT", "Capacitar os interessados em desenvolver e aplicar inovações tecnológicas nos setores ligados ao meio ambiente, compatíveis com os conhecimentos e as perspectivas do desenvolvimento sustentável, levando sempre em consideração aspectos técnicos, socioeconômicos, ambientais, culturais e éticos.", "https://quimica.ufcat.edu.br/especializacao-em-analises-quimicas-ambientais"),
        ("Alfabetização e Letramento", "12 meses", "EAD", "IFG", "Destina-se aos portadores de diploma de graduação em Pedagogia ou Letras, que estejam em efetivo exercício como professores de disciplinas relacionadas à alfabetização e letramento nos anos iniciais da Educação Básica pública.", "http://selecao.ifg.edu.br/downloads/cod2481/edital%2034%20-2024%20-%20selecao%20de%20estudantes%20para%20os%20cursos%20de%20especializacao%20ead%202025-1.pdf")
    ]

    for curso in cursos_esp:
        bloco_curso(*curso)

# Página de contatos
def pagina_contatos():
    st.title("**Contatos**")
    st.write("📱 **Instagram:** https://www.instagram.com/uabpolo/")
    st.write("🌐 **Facebook:** Polo UAB Formosa")
    st.write("📞 **Telefone:** (61) 9 9988-8422")
    st.write("📍 **Endereço:** Pça 21 de Abril, nº 60. Bairro Abreu. Formosa - GO. CEP: 73803-025.")
    st.write("👤 **Coordenador:** Dione Antônio de Castro Reis")
    st.write("✉️ **E-mail:** polouabformosa@hotmail.com ou dionecastro1@hotmail.com")

    st.markdown("---")
    st.subheader("📬 Fale Conosco")

    with st.form("formulario_contato", clear_on_submit=True):
        nome = st.text_input("Nome completo")
        email = st.text_input("E-mail")
        assunto = st.text_input("Assunto")
        mensagem = st.text_area("Mensagem")

        enviado = st.form_submit_button("Enviar")

        if enviado:
            st.success("✅ Sua mensagem foi enviada com sucesso!")
            # poderia armazenar ou enviar os dados via API/email


def mostrar_resumo_uab():
    resumo = """
# Universidade Aberta do Brasil (UAB)

A **Universidade Aberta do Brasil (UAB)** é um sistema público criado pelo governo federal brasileiro em 2006 com o objetivo de expandir e democratizar o acesso ao ensino superior, especialmente para as regiões mais afastadas ou com pouca oferta de universidades presenciais.

Ela funciona por meio da **educação a distância (EaD)**, em parceria com instituições públicas de ensino superior (como universidades federais e estaduais), e utiliza polos de apoio presencial espalhados pelo país. Esses polos oferecem estrutura física, orientação acadêmica e suporte tecnológico para os alunos.

### Principais objetivos da UAB:
- Ampliar o acesso ao ensino superior público e gratuito.
- Formar e capacitar professores para a educação básica.
- Promover a inclusão social por meio da educação.

### Público-alvo:
- Pessoas que vivem longe dos grandes centros urbanos.
- Profissionais da educação que buscam formação ou atualização.
- Todos que buscam ensino superior de qualidade, mas com flexibilidade de tempo e local.
    """
    st.markdown(resumo)
    


def mostrar_cursos_graduacao():
    cursos = [
        ("01", "Licenciatura em Artes Visuais", "50/51/25", "UAB/UFG", "2007-2011", "Concluído"),
        ("02", "Licenciatura em Ciências Biológicas - Turma I", "50/51/22", "UAB/UEG", "2009-2013", "Concluído"),
        ("03", "Licenciatura em Educação Física", "35/35/18", "UAB/UFG", "2010-2013", "Concluído"),
        ("04", "Bacharelado em Administração Pública", "50/50/37", "UAB/UEG", "2010-2013", "Concluído"),
        ("05", "Licenciatura em Educação Física", "50/29/12", "PARFOR/UFG", "2011-2015", "Concluído"),
        ("06", "Licenciatura em Artes Visuais", "50/26/10", "PARFOR/UFG", "2011-2015", "Concluído"),
        ("07", "Bacharelado em Administração Pública", "60/59/18", "UAB/UEG", "2017-2020", "Concluído"),
        ("08", "Licenciatura em Ciências Biológicas - Turma II", "50/50/18", "UAB/UEG", "2017-2020", "Concluído"),
        ("09", "Licenciatura em Computação", "90/45/16", "UAB/UEG", "2017-2020", "Concluído"),
        ("10", "Licenciatura em Ciências Biológicas - Turma III", "40/40/8 (4 ainda cursando 2025)", "UAB/UEG", "2019-2023", "Concluído"),
        ("11", "Tecnólogo em Gestão do Agronegócio", "20/12/-", "UAB/UFCAT", "2023-2025", "Ativo"),
        ("12", "Licenciatura em Letras/Inglês", "60/48/-", "UAB/IFB", "2023-2027", "Ativo"),
        ("13", "Licenciatura em Matemática", "60/26/-", "UAB/IFB", "2023-2027", "Ativo"),
        ("14", "Licenciatura em Pedagogia EPT", "50/59/-", "UAB/IFGOIANO", "2023-2027", "Ativo"),
        ("15", "Licenciatura em Pedagogia", "33/31/-", "UAB/UnB", "2023-2026", "Ativo"),
        ("16", "Licenciatura em Ciências Biológicas - Turma IV", "40/32/-", "UAB/UEG", "2024-2027", "Ativo"),
        ("17", "Tecnologia em Gestão Comercial", "30/32/-", "UAB/IFG", "2024-2026", "Ativo"),
        ("18", "Tecnologia em Sistemas para Internet", "25/27/-", "UAB/IFMT", "2025-2027", "Ativo"),
        ("19", "Bacharelado em Administração Pública", "20/20/-", "UAB/UFG", "2025-2028", "Ativo"),
        ("20", "Bacharelado em Biblioteconomia", "50/50/-", "UAB/UFG", "2025-2028", "Ativo"),
    ]

    df = pd.DataFrame(cursos, columns=[
        "Nº", "Curso", "Vagas / Matrículas / Concluídos",
        "Instituição", "Período", "Situação"
    ])

    st.subheader("📚 Visão geral dos cursos de graduação ofertados no Polo de Formosa")
    st.table(df)
