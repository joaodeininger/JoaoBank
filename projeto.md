# 📚 Roteiro Completo: Tutorial Interativo de Streamlit

## 📋 Índice
1. [Introdução](#introdução)
2. [Estrutura Geral](#estrutura-geral)
3. [Seção por Seção](#seção-por-seção)
4. [Conceitos-Chave](#conceitos-chave)
5. [Como Ensinar](#como-ensinar)
6. [Extensões Propostas](#extensões-propostas)

---

## 🎯 Introdução

Este projeto é um **aplicativo Streamlit interativo** desenvolvido para ensinar os conceitos fundamentais da biblioteca de forma prática e envolvente. O app utiliza:
- Menu lateral para navegação
- Exemplos práticos e funcionais
- Componentes visuais atraentes
- Interatividade em tempo real

**Público-alvo:** Iniciantes em Streamlit (não requer conhecimento prévio de web)

---

## 🏗️ Estrutura Geral

### Importações e Configuração Inicial

```python
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

**O que cada uma faz:**
- `streamlit`: A biblioteca principal para criar a web app
- `pandas`: Manipulação de dados tabulares (DataFrames)
- `numpy`: Cálculos numéricos e arrays
- `matplotlib`: Criação de gráficos

### Configuração da Página

```python
st.set_page_config(
    page_title="Tutorial Streamlit",
    page_icon="🎓",
    layout="wide"
)
```

**Explicação:**
- `page_title`: Nome que aparece na aba do navegador
- `page_icon`: Emoji que aparece na aba (muito legal visualmente!)
- `layout="wide"`: Usa toda a largura da tela (não deixa margem grande)

---

## 📖 Seção por Seção

### 1️⃣ PÁGINA: INÍCIO

#### Propósito
Dar boas-vindas e explicar o que é Streamlit de forma acessível.

#### Código Explicado

```python
st.title("🎓 Tutorial Interativo de Streamlit")
st.write("Aprenda os conceitos básicos de Streamlit de forma prática!")
```

**Função:** `st.title()` cria um título grande (h1 em HTML)
**Função:** `st.write()` escreve texto simples (substitui print em web apps)

#### Barra Lateral e Navegação

```python
st.sidebar.title("Menu")
opcao = st.sidebar.radio(
    "Escolha um tópico:",
    [
        "Início",
        "Widgets Básicos",
        "Texto e Formatação",
        "Dados e Tabelas",
        "Gráficos",
        "Interatividade"
    ]
)
```

**O que faz:**
- `st.sidebar`: Cria um menu na barra lateral (esquerda)
- `st.sidebar.radio()`: Botões de seleção (radio button) - escolhe 1 de vários
- Retorna a opção selecionada em `opcao`

#### Colunas (Layout)

```python
col1, col2 = st.columns(2)

with col1:
    st.write("""...""")

with col2:
    st.write("""...""")
```

**O que faz:**
- `st.columns(2)`: Divide a tela em 2 colunas de tamanho igual
- `with col1:` e `with col2:`: Coloca conteúdo em cada coluna
- Resultado: conteúdo lado a lado (responsivo)

#### Divisores e Dicas

```python
st.divider()  # Linha horizontal
st.info("💡 Dica: Use a barra lateral para navegar entre os exemplos!")
```

---

### 2️⃣ PÁGINA: WIDGETS BÁSICOS

#### Propósito
Ensinar os componentes interativos mais comuns do Streamlit.

#### Widget 1: Botões

```python
if st.button("Clique em mim!", key="btn1"):
    st.balloons()
    st.success("Você clicou no botão! 🎉")
```

**Explicação:**
- `st.button()`: Cria um botão clicável
- Retorna `True` quando clicado
- `key="btn1"`: Identificador único (importante se tiver múltiplos botões)
- `st.balloons()`: Animação festiva (confetes caem da tela!)
- `st.success()`: Caixa verde de sucesso

**Ensino:** "Quando o usuário clica, o código dentro do `if` executa"

#### Widget 2: Entrada de Texto

```python
nome = st.text_input("Digite seu nome:", placeholder="João")
if nome:
    st.write(f"Olá, **{nome}**! 👋")
```

**Explicação:**
- `st.text_input()`: Campo de texto (igual input HTML)
- Retorna o texto digitado
- `placeholder`: Texto cinzento que desaparece ao digitar
- `if nome:`: Só mostra resposta se tiver texto
- `**{nome}**`: Markdown para deixar em negrito

**Ensino:** "A resposta aparece em tempo real conforme o usuário digita"

#### Widget 3: Seleção (Selectbox)

```python
fruta = st.selectbox(
    "Qual é sua fruta favorita?",
    ["Maçã", "Banana", "Laranja", "Morango"]
)
st.write(f"Você escolheu: {fruta} 🍎")
```

**Explicação:**
- `st.selectbox()`: Dropdown (lista suspensa)
- Primeiro argumento: rótulo da pergunta
- Segunda argumento: lista de opções
- Retorna a opção selecionada

**Ensino:** "Use quando há poucas opções (até ~10)"

#### Widget 4: Múltipla Seleção

```python
linguagens = st.multiselect(
    "Qual linguagens você conhece?",
    ["Python", "JavaScript", "Java", "C++", "R"],
    default=["Python"]
)
st.write(f"Você selecionou: {', '.join(linguagens)}")
```

**Explicação:**
- `st.multiselect()`: Permite escolher VÁRIOS items
- `default=["Python"]`: Começa com Python pré-selecionado
- Retorna uma LISTA de seleções
- `', '.join()`: Transforma lista em string separada por vírgulas

**Ensino:** "Diferença: selectbox = 1 escolha, multiselect = várias"

#### Widget 5: Slider

```python
idade = st.slider("Qual é sua idade?", 0, 100, 25)
st.write(f"Sua idade: {idade} anos")
```

**Explicação:**
- `st.slider()`: Controle deslizante
- Argumentos: (rótulo, min, max, valor_inicial)
- Retorna um número inteiro

**Variações:**
```python
# Float (decimal)
valor = st.slider("Valor:", 0.0, 10.0, 5.5)

# Com step (incremento)
temp = st.slider("Temperatura:", -50, 50, 20, step=5)
```

#### Widget 6: Números

```python
numero = st.number_input("Digite um inteiro:", value=10)
decimal = st.number_input("Digite um decimal:", value=3.14, format="%.2f")
```

**Explicação:**
- `st.number_input()`: Campo numérico com spinner (setas)
- `value`: Valor inicial
- `format="%.2f"`: Formata com 2 casas decimais
- Melhor que `text_input` porque valida números

---

### 3️⃣ PÁGINA: TEXTO E FORMATAÇÃO

#### Propósito
Mostrar como estilizar conteúdo e melhorar a apresentação.

#### Caixas de Mensagem

```python
st.success("✅ Mensagem de sucesso!")      # Verde
st.warning("⚠️ Aviso importante!")          # Amarelo
st.error("❌ Erro detectado!")              # Vermelho
st.info("ℹ️ Informação útil")               # Azul
```

**Uso prático:**
- Verde: Operação bem-sucedida
- Amarelo: Cuidado, validação
- Vermelho: Erro, problema
- Azul: Dica, informação

#### Formatação Markdown

```python
st.markdown("""
**Negrito** | *Itálico* | ~~Tachado~~

`Código inline`

```python
# Código em bloco
def hello():
    print("Olá, Streamlit!")
```
""")
```

**Explicação:**
- Markdown é texto formatado (mesma sintaxe do GitHub)
- `**texto**`: Negrito
- `*texto*`: Itálico
- `` `texto` ``: Código inline
- ` ```python ... ``` `: Bloco de código com destaque

#### Expandir/Collapse (Expander)

```python
with st.expander("Clique para expandir"):
    st.write("Este conteúdo fica oculto até você clicar!")
    st.image("https://via.placeholder.com/300")
```

**O que faz:**
- Conteúdo começa recolhido/fechado
- Clique para expandir/mostrar
- Ótimo para não poluir a interface
- Economiza espaço na tela

**Uso:** FAQs, detalhes técnicos, código de exemplo

---

### 4️⃣ PÁGINA: DADOS E TABELAS

#### Propósito
Trabalhar com dados estruturados (principal uso do Streamlit em análise de dados).

#### Criando um DataFrame

```python
df = pd.DataFrame({
    "Produto": ["Python", "Pandas", "Streamlit", "NumPy"],
    "Categoria": ["Linguagem", "Biblioteca", "Framework", "Biblioteca"],
    "Popularidade": [95, 90, 85, 92],
    "Ano": [1991, 2008, 2019, 2005]
})

st.dataframe(df)
```

**Explicação:**
- Cria um dicionário de colunas
- `pd.DataFrame()`: Transforma em tabela
- `st.dataframe()`: Mostra a tabela interativa no Streamlit
- Usuário pode: ordenar, pesquisar, ver mais linhas

**Alternativa:**
```python
st.table(df)  # Tabela estática (mais rápida, menos interativa)
```

#### Filtrando Dados

```python
min_pop = st.slider("Popularidade mínima:", 0, 100, 80)
df_filtrado = df[df["Popularidade"] >= min_pop]
st.dataframe(df_filtrado)
```

**O que faz:**
- Slider controla o filtro
- `df[df["Popularidade"] >= min_pop]`: Filtra linhas
- Tabela atualiza em TEMPO REAL conforme mexe o slider
- Isso é o poder do Streamlit!

**Sintaxe pandas:**
```python
# Filtro simples
df[df["Coluna"] >= 50]

# Múltiplos filtros
df[(df["Coluna1"] > 10) & (df["Coluna2"] == "A")]

# Valores específicos
df[df["Categoria"].isin(["A", "B"])]
```

#### Estatísticas

```python
st.dataframe(df.describe())
```

**O que mostra:**
- count: Número de valores
- mean: Média
- std: Desvio padrão
- min, 25%, 50%, 75%, max: Quartis

---

### 5️⃣ PÁGINA: GRÁFICOS

#### Propósito
Visualizar dados com matplotlib integrado ao Streamlit.

#### Configuração Básica

```python
fig, ax = plt.subplots()
ax.plot(dados["Mês"], dados["Vendas"], marker='o', linewidth=2)
ax.set_xlabel("Mês")
ax.set_ylabel("Vendas (R$)")
ax.set_title("Vendas por Mês")
ax.grid(True, alpha=0.3)
st.pyplot(fig)
```

**Explicação:**
- `plt.subplots()`: Cria figura e eixos
- `ax.plot()`: Desenha linha
  - `marker='o'`: Adiciona bolinhas nos pontos
  - `linewidth=2`: Espessura da linha
- `ax.set_xlabel/ylabel/title`: Rótulos
- `ax.grid()`: Linhas de grade
  - `alpha=0.3`: Transparência (0-1)
- `st.pyplot(fig)`: Mostra o gráfico

#### Gráfico de Barras

```python
fig, ax = plt.subplots()
ax.bar(
    dados_barras["Tecnologia"], 
    dados_barras["Desenvolvedores"],
    color=['#3776ab', '#f7df1e', '#007396', '#239120']
)
ax.set_ylabel("Número de Desenvolvedores")
st.pyplot(fig)
```

**Cores hexadecimais:**
- `#3776ab`: Azul (Python)
- `#f7df1e`: Amarelo (JavaScript)
- `#007396`: Azul (Java)
- `#239120`: Verde (C#)

#### Gráfico de Dispersão

```python
x = np.random.randn(100)  # 100 valores aleatórios
y = x + np.random.randn(100) * 0.5  # Com ruído

fig, ax = plt.subplots()
ax.scatter(x, y, alpha=0.6, s=100)
ax.set_xlabel("Variável X")
ax.set_ylabel("Variável Y")
st.pyplot(fig)
```

**Parâmetros scatter:**
- `alpha=0.6`: Transparência dos pontos
- `s=100`: Tamanho dos pontos
- `c="red"`: Cor (opcional)

#### Alternativa: Gráficos Rápidos

```python
st.line_chart(data)  # Gráfico de linha simples
st.bar_chart(data)   # Gráfico de barras simples
st.area_chart(data)  # Área
```

**Vantagem:** Menos código, mais rápido
**Desvantagem:** Menos controle sobre aparência

---

### 6️⃣ PÁGINA: INTERATIVIDADE

#### Propósito
Demonstrar como criar aplicações dinâmicas que respondem a inputs do usuário.

#### Calculadora Simples

```python
col1, col2, col3 = st.columns(3)

with col1:
    num1 = st.number_input("Número 1:", value=10)

with col2:
    operacao = st.selectbox("Operação:", ["+", "-", "*", "/"])

with col3:
    num2 = st.number_input("Número 2:", value=5)

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2 if num2 != 0 else 0

st.success(f"Resultado: {num1} {operacao} {num2} = {resultado}")
```

**Ensino:**
- Inputs lado a lado com `columns(3)`
- Lógica simples com `if/elif`
- Proteção contra divisão por zero
- Exibe resultado formatado

#### Gerador de Dados

```python
num_linhas = st.slider("Quantas linhas?", 5, 100, 20)

if st.button("Gerar Dados"):
    df_aleatorio = pd.DataFrame({
        "ID": range(1, num_linhas + 1),
        "Valor": np.random.randint(0, 1000, num_linhas),
        "Categoria": np.random.choice(["A", "B", "C"], num_linhas)
    })
    st.dataframe(df_aleatorio)
    st.bar_chart(df_aleatorio.set_index("ID")["Valor"])
```

**Explicação:**
- `np.random.randint(0, 1000, num_linhas)`: Números aleatórios entre 0-1000
- `np.random.choice()`: Escolhe aleatoriamente de uma lista
- Gera dados dinâmicos baseado no input
- Mostra tabela + gráfico juntos

#### Session State (Memória da Sessão)

```python
if "contador" not in st.session_state:
    st.session_state.contador = 0

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("➕ Incrementar"):
        st.session_state.contador += 1

with col2:
    if st.button("➖ Decrementar"):
        st.session_state.contador -= 1

with col3:
    if st.button("🔄 Resetar"):
        st.session_state.contador = 0

with col4:
    st.metric("Contador:", st.session_state.contador)
```

**Conceito-chave: Session State**

**Problema:** Streamlit reexecuta o script inteiro cada vez que há interação
**Solução:** `st.session_state` armazena dados entre execuções

**Explicação:**
- `if "contador" not in st.session_state:`: Cria variável se não existir
- `st.session_state.contador`: Acessa a variável persistente
- Quando clica o botão, incrementa/decrementa e mantém o valor
- `st.metric()`: Mostra um número/métrica destaque

**Sem session state:**
```python
contador = 0
if st.button("Incrementar"):
    contador += 1  # Reseta para 0 a cada re-run!
```

**Com session state:**
```python
if "contador" not in st.session_state:
    st.session_state.contador = 0
if st.button("Incrementar"):
    st.session_state.contador += 1  # Persiste entre re-runs
```

---

## 🧠 Conceitos-Chave

### 1. Como Streamlit Funciona

```
┌─────────────────────────────────────────┐
│ Usuário interage (clica botão, digita) │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│ Script inteiro é reexecutado do topo    │
│ (reruns)                                │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│ Interface é atualizada na tela          │
└─────────────────────────────────────────┘
```

**Implicação:** Use `st.session_state` para manter estado entre reruns

### 2. Ordem de Execução

O script executa de cima para baixo. Variáveis definidas aparecem na tela naquela ordem:

```python
st.write("Isso aparece primeiro")
st.write("Isso aparece segundo")
st.write("Isso aparece terceiro")
```

### 3. Reatividade

Streamlit é "reativo" = muda automaticamente quando inputs mudam:

```python
valor = st.slider("Escolha:", 0, 100)
resultado = valor * 2
st.write(f"Resultado: {resultado}")  # Atualiza automaticamente
```

### 4. Chaves Únicas (Keys)

Quando tem múltiplos widgets do mesmo tipo, use `key` para diferenciar:

```python
st.button("Botão 1", key="btn1")
st.button("Botão 2", key="btn2")
st.slider("Slider 1", key="slider1")
st.slider("Slider 2", key="slider2")
```

---

## 📚 Como Ensinar

### Sequência Recomendada

**Aula 1 - Básicos (30 min)**
1. Mostrar a página "Início"
2. Explicar: `st.title()`, `st.write()`, `st.header()`
3. Navegar até "Widgets Básicos"
4. Demonstrar: `st.button()`, `st.text_input()`, `st.slider()`
5. Exercício: "Crie um formulário que pede nome e idade"

**Aula 2 - Estrutura e Layout (30 min)**
1. Explicar: `st.columns()`, `st.sidebar`, `st.divider()`
2. Mostrar página "Texto e Formatação"
3. Explicar: Markdown, `st.success()`, `st.expander()`
4. Exercício: "Crie uma página com 3 colunas e expanders"

**Aula 3 - Dados (40 min)**
1. Mostrar página "Dados e Tabelas"
2. Explicar: `st.dataframe()`, filtragem com pandas
3. Demonstrar interatividade: slider + filtro
4. Exercício: "Crie um filtro para um DataFrame com 3 colunas"

**Aula 4 - Gráficos (40 min)**
1. Mostrar página "Gráficos"
2. Explicar: `st.pyplot()`, matplotlib básico
3. Demonstrar: linha, barras, dispersão
4. Exercício: "Crie um gráfico interativo (slider controla dados)"

**Aula 5 - Interatividade Avançada (40 min)**
1. Mostrar página "Interatividade"
2. Explicar: Session State (conceito crucial!)
3. Explicar: Re-runs e reatividade
4. Exercício: "Crie um contador persistente com botões"

### Dicas de Ensino

- **Mostre o código e a saída juntos** - Use `st.code()` para mostrar código:
  ```python
  st.code("""
  df = pd.DataFrame({"A": [1,2,3]})
  st.dataframe(df)
  """, language="python")
  ```

- **Use exemplos do mundo real** - Mostre casos de uso:
  - Dashboard de vendas
  - Análise de dados climáticos
  - Simuladores
  - Ferramentas internas

- **Deixe erros acontecerem** - Mostre que Streamlit avisa:
  - Divisão por zero
  - Colunas inexistentes
  - Tipos de dados errados

- **Incentive experimentação** - "Tente mudar este número... E este cor... E este texto"

---

## 🚀 Extensões Propostas

### Extensão 1: Upload de Arquivos

```python
st.subheader("Upload de Arquivo")
arquivo = st.file_uploader("Escolha um CSV:", type="csv")

if arquivo:
    df = pd.read_csv(arquivo)
    st.dataframe(df)
    st.bar_chart(df.set_index(df.columns[0]))
```

### Extensão 2: Download de Dados

```python
df = pd.DataFrame({"A": [1,2,3], "B": [4,5,6]})

csv = df.to_csv(index=False)
st.download_button(
    label="Baixar CSV",
    data=csv,
    file_name="dados.csv"
)
```

### Extensão 3: Formulário

```python
with st.form("meu_formulario"):
    nome = st.text_input("Nome:")
    email = st.text_input("Email:")
    idade = st.slider("Idade:", 0, 100)
    
    if st.form_submit_button("Enviar"):
        st.success(f"Obrigado, {nome}!")
```

### Extensão 4: Cache para Performance

```python
@st.cache_data
def carregar_dados():
    # Isso executa apenas UMA VEZ
    # Não reexecuta a cada re-run
    return pd.read_csv("arquivo_grande.csv")

df = carregar_dados()
st.dataframe(df)
```

### Extensão 5: Tema Escuro

No arquivo `~/.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#1a1a1a"
secondaryBackgroundColor = "#262626"
textColor = "#FFFFFF"
font = "sans serif"
```

### Extensão 6: Múltiplas Páginas

Criar pastas:
```
projeto/
├── app.py (arquivo principal)
└── pages/
    ├── pagina1.py
    ├── pagina2.py
    └── pagina3.py
```

Cada arquivo em `pages/` vira uma aba automaticamente!

---

## 🔗 Recursos Adicionais

- **Documentação oficial:** https://docs.streamlit.io
- **Gallery:** https://streamlit.io/gallery
- **Cheat Sheet:** https://docs.streamlit.io/library/cheatsheet
- **Comunidade:** https://discuss.streamlit.io

---

**Desenvolvido com ❤️ para fins educacionais**