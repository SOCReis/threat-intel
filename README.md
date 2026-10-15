# Threat Intel 🔎

Ferramenta de Threat Intelligence desenvolvida em Python para auxiliar na investigação de endereços IP.

## 🎯 Objetivo

O objetivo do projeto é reunir informações sobre um endereço IP, permitindo analisar dados de rede e consultar fontes públicas para apoiar investigações de segurança cibernética.

## ⚙️ Funcionalidades

- [x] Validar endereços IPv4 e IPv6.
- [x] Consultar informações de geolocalização aproximada.
- [x] Identificar organização e provedor de rede.
- [ ] Consultar reputação do IP em fontes de inteligência.
- [ ] Gerar relatórios organizados da investigação.

As funcionalidades serão implementadas gradualmente.

## 🛠️ Tecnologias

- Python
- Requests
- APIs de inteligência de ameaças
- Git e GitHub

## 📁 Estrutura do projeto

- `main.py`: coordena a execução.
- `validator.py`: valida os endereços IP.
- `geolocation.py`: consulta informações geográficas e de rede.
- `report.py`: organiza e exibe os resultados.
- `requirements.txt`: lista as dependências do projeto.

## 🚀 Como executar

1. Clone o repositório.
2. Entre na pasta do projeto.
3. Instale as dependências:

```bash
py -m pip install -r requirements.txt
```

4. Execute o programa:

```bash
py main.py
```

## 🔐 Uso responsável

Este projeto tem finalidade educacional e de defesa cibernética.

Os resultados das consultas são indicativos, não provas definitivas de atividade maliciosa. Informações de geolocalização podem ser aproximadas e variar conforme a fonte utilizada.

## 📚 Aprendizados

O projeto busca desenvolver conhecimentos em Python, APIs, validação de dados, análise de indicadores de comprometimento (IoCs) e investigação de segurança.

## 📌 Status

Em desenvolvimento.
