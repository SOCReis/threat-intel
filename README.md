# Threat Intel 🔎

Ferramenta de **Threat Intelligence** desenvolvida em Python para auxiliar na investigação de endereços IP, reunindo informações de rede, geolocalização e reputação para apoiar análises de segurança cibernética.

## 🎯 Objetivo

Desenvolver uma ferramenta que facilite a investigação inicial de indicadores de rede (IoCs), integrando diferentes fontes de inteligência para identificar endereços IP potencialmente suspeitos.

O projeto também tem como objetivo desenvolver habilidades práticas em Python, consumo de APIs, análise de ameaças e automação de tarefas de segurança.

## ⚙️ Funcionalidades

- ✅ Validar endereços IPv4 e IPv6.
- ✅ Consultar informações de geolocalização aproximada.
- ✅ Identificar a organização e o provedor de rede associados ao IP.
- ✅ Consultar a reputação do IP por meio da API do AbuseIPDB.
- ✅ Obter o Abuse Confidence Score, pontuação de 0 a 100.
- ✅ Gerar relatórios com os resultados da investigação.

As funcionalidades devem ser marcadas como concluídas somente quando estiverem implementadas e testadas no código.

## 🛡️ Análise de reputação e risco

A ferramenta utiliza o AbuseIPDB para consultar informações sobre denúncias de abuso associadas a um endereço IP.

| Pontuação | Classificação indicativa |
|---|---|
| 0% | Sem abuso indicado pela pontuação |
| 1–24% | Suspeita baixa |
| 25–49% | Suspeita moderada |
| 50–74% | Suspeita alta |
| 75–100% | Suspeita muito alta |

Essas faixas são critérios internos do projeto, não uma classificação oficial universal. A pontuação deve ser analisada junto de outros indicadores, pois não comprova isoladamente uma atividade maliciosa.

## 🚀 Melhorias planejadas

### 1. Classificação automática de risco
- Classificar IPs por faixas de pontuação.
- Destacar resultados que merecem investigação prioritária.
- Exibir uma justificativa para cada classificação.

### 2. Relatórios mais completos
- Incluir data e hora da consulta.
- Registrar a pontuação do AbuseIPDB.
- Organizar informações de geolocalização, organização e reputação.
- Exportar os resultados para JSON ou CSV.

### 3. Histórico de consultas
- Armazenar os IPs consultados.
- Comparar resultados entre consultas.
- Identificar alterações na reputação de um endereço IP.

### 4. Tratamento de erros
- Detectar falhas de conexão e tempo limite.
- Tratar respostas inválidas das APIs.
- Identificar limites de requisições e erros de autenticação.
- Evitar que uma falha em uma fonte interrompa toda a investigação.

### 5. Dashboard de investigação
- Apresentar os resultados em uma interface visual.
- Utilizar indicadores e gráficos para facilitar a interpretação.
- Destacar pontuações elevadas.
- Permitir consultar o histórico e filtrar resultados.

### 6. Segurança e qualidade do código
- Proteger chaves de API por meio de variáveis de ambiente.
- Impedir o envio de credenciais ao GitHub.
- Separar responsabilidades em módulos.
- Adicionar testes automatizados para validação de IP e tratamento de respostas.
- Documentar a instalação e o funcionamento de cada módulo.

## 🛠️ Tecnologias

- Python
- Requests
- python-dotenv
- AbuseIPDB API
- API de geolocalização e informações de rede
- Git e GitHub

## 📁 Estrutura do projeto

- `main.py` — coordena a execução.
- `validator.py` — valida endereços IP.
- `geolocation.py` — consulta informações geográficas e de rede.
- `abuseipdb.py` — consulta a reputação do endereço IP.
- `report.py` — organiza e apresenta os resultados.
- `requirements.txt` — lista as dependências.
- `.env` — armazena variáveis de ambiente locais.
- `.gitignore` — exclui arquivos que não devem ser versionados.

A estrutura deve ser ajustada conforme os arquivos existentes no repositório.

## 🚀 Como executar

### 1. Clonar o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
cd Threat-Intel
```

### 2. Criar o ambiente virtual

```bash
py -m venv venv
```

### 3. Ativar o ambiente no Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências

```bash
py -m pip install -r requirements.txt
```

### 5. Configurar a chave da API

Crie um arquivo `.env` na raiz:

```env
ABUSEIPDB_API_KEY=sua_chave_aqui
```

Não compartilhe sua chave e mantenha o arquivo `.env` no `.gitignore`.

### 6. Executar

```bash
py main.py
```

## 🔐 Uso responsável

Este projeto possui finalidade educacional e de defesa cibernética.

- Os resultados dependem das fontes consultadas e podem estar incompletos ou desatualizados.
- A geolocalização de um IP é aproximada.
- Uma pontuação elevada não comprova, por si só, um ataque.
- As consultas devem respeitar os termos de uso e os limites das APIs utilizadas.
- Credenciais e dados sensíveis não devem ser publicados no repositório.

## 📚 Aprendizados

O projeto permite desenvolver conhecimentos em:

- Python e programação modular.
- Validação de IPv4 e IPv6.
- Consumo de APIs REST e interpretação de JSON.
- Gerenciamento de variáveis de ambiente.
- Threat Intelligence e análise de IoCs.
- Avaliação de reputação e classificação indicativa de risco.
- Tratamento de erros e testes automatizados.
- Documentação técnica e desenvolvimento de portfólio.

## 📌 Status

**Em desenvolvimento.**

O projeto está sendo aprimorado gradualmente, com foco em confiabilidade das consultas, apresentação dos resultados e recursos úteis para investigações iniciais de segurança cibernética.
