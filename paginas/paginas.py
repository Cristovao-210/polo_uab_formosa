import streamlit as st

# Página inicial
def pagina_inicio():
    st.title("Polo UAB Formosa - GO")
    st.markdown("### Vídeo de Apresentação")
    st.video("https://www.youtube.com/embed/I17fKqbyLF8?si=dLo106rf1HgbkBq4")

# Função auxiliar para bloco de curso
def bloco_curso(nome, duracao, modalidade, instituicao, descricao):
    with st.expander(nome):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**Duração:** {duracao}")
            st.markdown(f"**Modalidade:** {modalidade}")
        with col2:
            st.markdown(f"**Instituição:** {instituicao}")
        st.markdown("----")
        st.write(descricao)

# Página de cursos de graduação
def pagina_graduacao():
    st.title("Cursos de Graduação")

    cursos_grad = [
        ("Licenciatura em Ciências Biológicas", "4 anos", "EAD", "UEG", "Forma professores para atuarem na educação básica, com foco em ecologia, genética, microbiologia e ensino de ciências."),
        ("Licenciatura em Pedagogia", "4 anos", "EAD", "IFGoiano", "Capacita profissionais para atuação na educação infantil e nos anos iniciais do ensino fundamental."),
        ("Licenciatura em Pedagogia", "4 anos", "EAD", "UnB", "Curso oferecido com foco em práticas pedagógicas inovadoras e políticas públicas educacionais."),
        ("Licenciatura em Letras/Inglês", "4 anos", "EAD", "IFB", "Habilita professores de inglês para educação básica, com foco em linguística, literatura e ensino de idiomas."),
        ("Licenciatura em Matemática", "4 anos", "EAD", "IFB", "Voltado para a formação de professores de matemática com ênfase em didática e raciocínio lógico."),
        ("Tecnólogo em Gestão do Agronegócio", "3 anos", "EAD", "UFCAT", "Forma profissionais para atuar na cadeia produtiva do agronegócio com foco em gestão e logística."),
        ("Tecnologia em Gestão Comercial", "3 anos", "EAD", "IFG", "Desenvolve habilidades em administração, vendas, marketing e gestão empresarial."),
        ("Tecnologia em Sistemas para Internet", "3 anos", "EAD", "IFMT", "Foca no desenvolvimento de aplicações web, segurança da informação e bancos de dados.")
    ]

    for curso in cursos_grad:
        bloco_curso(*curso)

# Página de cursos de especialização
def pagina_especializacao():
    st.title("Cursos de Especialização")

    cursos_esp = [
        ("Educação Inclusiva com Ênfase na Educação de Surdos", "18 meses", "EAD", "IFMT", "Capacita profissionais da educação para inclusão de surdos no ambiente escolar, com foco em LIBRAS e práticas pedagógicas inclusivas."),
        ("Educação, Meio Ambiente e Sustentabilidade", "18 meses", "EAD", "IFG", "Promove formação crítica e interdisciplinar sobre sustentabilidade, políticas ambientais e educação ambiental."),
        ("Geoprocessamento", "18 meses", "EAD", "UFABC", "Qualifica profissionais para o uso de ferramentas e técnicas de geoprocessamento aplicadas ao planejamento e à análise espacial."),
        ("Análises Químicas Ambientais", "18 meses", "EAD", "UFCAT", "Curso voltado para profissionais interessados em controle ambiental, com foco em técnicas laboratoriais e legislação ambiental."),
        ("Alfabetização e Letramento", "18 meses", "EAD", "IFG", "Oferece base teórica e metodológica para práticas de alfabetização nos anos iniciais do ensino fundamental.")
    ]

    for curso in cursos_esp:
        bloco_curso(*curso)

# Página de contatos
def pagina_contatos():
    st.title("Contatos")
    st.write("📱 Redes Sociais: @uabpolo")
    st.write("🌐 Facebook: Polo UAB Formosa")
    st.write("📞 Telefone: (61) 9 9988-8422")

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
