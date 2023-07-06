import streamlit as st
import streamlit.components.v1 as components


st.title("Welcome to my portfolio")

# você pode conferir o código fonte desse projeto no github pelo link

# No menu lateral você pode acessar os projetos e seus respectivos códigos.


# MAIS SOBRE MIM

# Olá, me chamo Lucas, tenho 29 anos 
# e moro em Brasilia no Brasil
# (colocar mapa com localização???)
 
# Venho da área da química
# trabalhei com biologia molecular e com tratamento de efluente
# comecei a usar programação na faculdade
# acabei migrando de carreira
# comecei a estudar para ser um cientista de dados
# atualmente trabalho na cromai com inteligência artificial



# components.html(
#     """
#     <a 
#         href="https://github.com/lucasiqueiira/portfolio_dashboard">
#         <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="Open repository"
#         style="width:50px;height:60px;"
#     /></a>
#     """
# )

# st.markdown("No menu lateral ao lado, você pode acessar alguns dos meu projetos pessoais")

# st.subheader("Quem sou eu?")
# st.markdown(
#     """Me chamo Lucas Siqueira Rodrigues, tenho 29 anos e moro em Brasília-DF, etcetcetc
#     """
# )


# Esse portifólio é para demonstrar meus projetos pessoais
# você pode navegar entre os projetos no menu lateral
# segue logo abaixo uma descrição de cada projeto

# Project 1
# Esse projeto é sobre bla bla bla


# Project 2
# Esse projeto é de bla bla bla

# Project 3

# The last page is my resume

st.markdown("""
# Lucas Siqueira Rodrigues

Idade: 29 anos\n
Número: (61)981473189\n
Localização: Brasília - DF\n
E-mail: siqueiraq@gmail.com\n
Linkedin: linkedin.com/in/lucasiqueiira\n
Github: github.com/lucasiqueiira

### SOBRE MIM
Estou cursando Big Data e Inteligência Analítica no IESB e estou no último semestre de Química. Atualmente estou trabalhando na Cromai como estagiário de inteligência artificial. Tive experiências anteriores na área da química, com tratamento de efluentes e com biologia molecular.


### HABILIDADES
* Python e bibliotecas para ciência de dados e aprendizado de máquina
* Metodologia ágil Kanban, Metodologia de gestão OKR
* Sistemas de versionamento (Git e Github)
* AWS (EC2, Sagemaker, Elastic Beanstalk)
* GCP (Cloud Storage)
* PostgreSQL
* Inglês intermediário

### EXPERIÊNCIAS PROFISSIONAIS	

#### Estagiário de Inteligência Artificial
Cromai - Setembro 2022 - Atualmente
A Cromai atua no campo da agricultura de precisão, ela usa inteligência artificial para identificação georreferenciada de grupos de daninhas no canavial e para identificação e controle de qualidade da cana que chega em usinas. Permite que os clientes tomem decisões baseadas em dados.

Atividades:
	Teste e implementação de diferentes estratégias para limpeza de datasets
	Teste e implementação de técnicas de redução de datasets
Implementação do módulo de limpeza e redução de dataset na nossa esteira de aquisição de dados
	Treinamento e avaliação de modelos de visão computacional
Gerar relatórios com gráficos e dados dos resultados obtidos
	
Tecnologias:
Python, Tensorflow, OpenCV, Onnx, Numpy, Pandas, AWS

#### Operador de ETE
Veolia - Dezembro 2021 - Setembro 2022
A Veolia é uma multinacional francesa cuja atividade se desenvolve principalmente em quatro áreas: fornecimento e gestão de águas, gestão de resíduos, energia e serviços de transportes.

Atividades realizadas:
	Operação do processo de tratamento de efluente industrial
	Realizar análises para avaliar a qualidade do processo
	Preenchimento de relatórios

#### Técnico em patologia clínica
Universidade Católica de Brasília - Julho 2015 - Maio 2020
A UCB é uma das maiores universidades particulares do centro-oeste, conta com vários cursos de graduação e pós-graduação. Possui um programa de mestrado e doutorado em ciências genômicas e biotecnologia, que é conceito 7 na capes.

Atividades realizadas:
	Análise e sequenciamento de DNA e RNA
	Operação de fermentadores
	Técnicas rotineiras de biotecnologia


### EDUCAÇÃO
##### Big Data e Inteligência Analítica
> Centro Universitário IESB

> Julho 2022 - Dezembro 2024

##### Bacharelado em Química
> Universidade de Brasília

> Janeiro 2018 - Julho 2023

""")