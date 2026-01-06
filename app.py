import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Termos de Uso e Privacidade - São Luís",
    page_icon="🛡️",
    layout="centered"
)

# Estilização CSS para melhorar a leitura
st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
    }
    .stMarkdown {
        text-align: justify;
        line-height: 1.6;
    }
    h1, h2, h3 {
        color: #1E3A8A; /* Azul institucional */
    }
    .footer {
        font-size: 12px;
        color: gray;
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        border-top: 1px solid #eee;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Cabeçalho
    st.title("Termos de Uso & Política de Privacidade")
    st.subheader("Prefeitura Municipal de São Luís")
    
    st.divider()

    # Conteúdo
    st.markdown("""
    ### Termos e Condições de Uso
    Os presentes Termos e Condições de Uso visam regular a utilização por você, usuário, de nossos serviços pelos sites institucionais e mobile.
    O Portal Institucional tem caráter gratuito. Porém, a utilização de alguns serviços e canais somente poderá ser feita mediante o registro do usuário.
    Não nos responsabilizamos por danos a terceiros que decorram de falhas de acesso, transmissão, difusão ou disponibilização de conteúdo e de serviços do portal.
    A oferta de serviços e/ou conteúdo desse portal obedecem a critérios de acessibilidade.

    ### Termo de Aceitação
    Ao utilizar os nossos Serviços, o usuário aceita e concorda com todos os termos e condições expostas que se encontram vigentes na data.
    Estes Termos e Condições de Uso poderão ser modificados a qualquer momento, em virtude de alterações na legislação, nos Serviços ou na adoção de novas ferramentas tecnológicas.
    A utilização dos Serviços online disponibilizados pela Instituição implicará em expressa aceitação destes Termos e Condições de Uso.

    ### Princípios Gerais de Proteção e Minimização de Dados
    A Instituição adota o princípio da minimização de dados, coletando apenas as informações estritamente necessárias para a prestação dos serviços públicos disponibilizados.
    Os dados coletados não são vinculados à identificação direta do usuário, salvo quando explicitamente necessário para o funcionamento do serviço, cumprimento de obrigação legal ou garantia da segurança da informação.
    A Instituição não comercializa, não vende, não aluga e não compartilha dados pessoais para fins publicitários.
    Não são utilizados anúncios comerciais, publicidade direcionada ou mecanismos de monetização baseados em dados pessoais.

    ### Tratamento de Informações
    A privacidade e o sigilo das informações dos usuários são prioridades institucionais. São adotadas medidas técnicas e administrativas adequadas para proteger os dados pessoais.
    Os dados cadastrados neste portal são criptografados e protegidos contra acessos não autorizados, fraudes, danos, sabotagens e roubos.
    Ao realizar cadastro ou entrar em contato, o usuário autoriza comunicações institucionais, podendo revogar o consentimento a qualquer momento, ciente de que alguns serviços podem ser impactados.
    As informações pessoais não são divulgadas sem consentimento expresso, exceto quando exigido por lei.

    ### Tipos de Dados Coletados
    * Informações técnicas do dispositivo e da conexão (IP, navegador, sistema operacional);
    * Dados de uso e interação com os sistemas;
    * Registros técnicos necessários à segurança, auditoria e melhoria dos serviços.

    #### Registros de Log
    Em caso de erros ou falhas técnicas, poderão ser coletados registros de log contendo dados como IP, data, hora, configuração do sistema e estatísticas de uso, exclusivamente para fins técnicos.

    ### Uso de Cookies
    O portal utiliza cookies estritamente necessários ao funcionamento dos serviços e à melhoria da experiência do usuário.
    Não são utilizados cookies para fins publicitários. Cookies de terceiros podem ser utilizados por bibliotecas técnicas integradas.
    O usuário pode gerenciar ou desativar cookies nas configurações do navegador, ciente de possíveis limitações de funcionalidades.

    ### Acesso a Conteúdo Restrito
    Alguns serviços exigem cadastro prévio e autenticação por login e senha ou certificação digital (e-CPF ou e-CNPJ).
    O usuário é responsável pela veracidade das informações fornecidas e pela guarda de suas credenciais de acesso.
    A Instituição poderá suspender ou cancelar acessos, a qualquer tempo, respeitada a legislação aplicável.

    ### Prestadores de Serviço e Terceiros
    A Instituição poderá contratar terceiros para hospedagem, manutenção, suporte técnico e análise estatística.
    Esses prestadores terão acesso limitado aos dados, exclusivamente para execução das atividades contratadas, sendo obrigados a manter sigilo e segurança.

    ### Retenção e Eliminação de Dados
    Os dados pessoais são armazenados apenas pelo tempo necessário ao cumprimento de suas finalidades legais, institucionais ou judiciais.
    Registros técnicos podem ser eliminados automaticamente após períodos definidos em normas internas.

    ### Segurança da Informação
    São adotadas boas práticas de segurança da informação. Contudo, nenhum sistema é absolutamente seguro, não sendo possível garantir risco zero.

    ### Proteção de Dados de Crianças e Adolescentes
    Os serviços não são destinados a menores de 13 anos, salvo quando vinculados a políticas públicas específicas e com base legal adequada.
    Dados coletados indevidamente serão eliminados imediatamente.

    ### Relacionamento com Terceiros
    O portal pode conter links para sites de terceiros, cujas práticas de privacidade não são de responsabilidade da Instituição.

    ### Conteúdos Jornalísticos
    Os conteúdos publicados na área de notícias possuem caráter jornalístico e são regidos pela legislação vigente, sendo permitida a reprodução não comercial, sem alterações que prejudiquem seu sentido original.

    ### Responsabilidades do Usuário
    O usuário compromete-se a utilizar o portal de forma lícita, ética e responsável, sendo vedadas práticas ilegais, ofensivas ou que comprometam a segurança dos sistemas.

    ### Alterações desta Política
    Esta Política poderá ser atualizada periodicamente. As alterações entram em vigor a partir de sua publicação oficial.

    ### Lei Geral de Proteção de Dados (LGPD)
    Lei nº 13.709/2018 – Esta política observa os princípios, direitos e deveres estabelecidos pela LGPD.

    ---
    ### Contato do Encarregado de Proteção de Dados
    **E-mail:** lgpd@semit.saoluis.ma.gov.br  
    **Endereço:** Avenida do Vale, nº 13 – Renascença II – Edifício Zircônio – Salas 102 a 110  
    **Data de vigência:** 10/12/2024
    """)

    # Rodapé
    st.markdown('<div class="footer">© 2026 Prefeitura de São Luís - Secretaria Municipal de Informação e Tecnologia (SEMIT)</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()