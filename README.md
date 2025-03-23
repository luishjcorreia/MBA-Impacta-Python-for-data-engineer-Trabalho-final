# Projeto Python- Transformação e Execução do dataset de voo

# Autores
👥 2403458 - Glauco Chagas Bertolaccini
👥 2402809 - Guilherme Dias
👥 2404289 - Luis Correia

Nome do Aluno - Desenvolvimento e Implementação

Carolina Zambelli Kamada - Orientação 

## 📂 Estrutura do Projeto
```
📁 projeto_python
│-- 📄 main.py          # Script principal para executar o pipeline de dados
│-- 📄 dataclean.py     # Módulo responsável pela limpeza dos dados
│-- 📄 transform.py     # Módulo responsável pelas transformações dos dados
│-- 📄 requirements.txt # Instalação das bibliotecas usadas no projeto
│-- 📄 base_tratada.csv # Arquivo CSV gerado com os dados processados
│-- 📄 README.md        # Documento explicativo do projeto
```

## 🔧 Principais Bibliotecas Utilizadas
- Python 3
- Pandas
- NumPy
- Regex

## 🚀 Funcionalidades
- **Leitura de Dados**: Carregamento do dataset a partir de um arquivo CSV remoto(Github).
- **Limpeza de Dados**: Remoção de valores nulos e padronização de colunas utilizando o módulo `dataclean.py`.
- **Transformação de Dados**:
  - Conversão do tempo de voo de minutos para horas.
  - Classificação dos voos de acordo com o turno (manhã, tarde, noite).
- **Exportação de Dados**: Salvar os dados tratados em um novo arquivo CSV.

## 📥 Instalação e Execução
1. Acesse o diretório do projeto:
   ```sh
   cd projeto_python
   ```
2. Instale as bibliotecas necessárias:
   ```sh
   pip install pandas numpy
   ```
3. Execute o script principal:
   ```sh
   python main.py
   ```

## 📌 Explicação dos Módulos
### `dataclean.py`
Este módulo contém a função `retira_vazio()`, que realiza:
- Filtragem de colunas essenciais.
- Remoção de valores ausentes.
- Conversão de colunas para os tipos corretos.
- Padronização de strings para remover caracteres especiais.

### `transform.py`
Este módulo contém funções para:
- `calc_horas(df, coluna)`: Converte minutos de voo para horas.
- `classifica_turno(data_hora)`: Classifica o voo de acordo com o período do dia (manhã, tarde, noite).


