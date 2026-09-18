# Estudo LangChain

Projeto de estudos sobre LangChain, LangGraph e integrações com LLMs.

## Requisitos

- Python 3.14.5
- Chaves de API (Anthropic, Groq, Google, Qdrant)

## Inicialização

### Opção 1: Windows com pyenv-win

1. **Instalar pyenv-win** (se ainda não tiver):
   ```powershell
   Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"
   & "./install-pyenv-win.ps1"
   ```

2. **Instalar Python 3.14.5**:
   ```powershell
   pyenv install 3.14.5
   pyenv local 3.14.5
   ```

3. **Criar ambiente virtual**:
   ```powershell
   python -m venv venv
   ```

4. **Ativar ambiente virtual**:
   ```powershell
   .\venv\Scripts\activate
   ```

5. **Instalar dependências**:
   ```powershell
   pip install -r requirements.txt
   ```

6. **Configurar variáveis de ambiente**:
   - Copie `.env.exemplo` para `.env`
   - Preencha as chaves de API no arquivo `.env`

7. **Testar instalação**:
   ```powershell
   python teste_instalacao.py
   ```

### Opção 2: WSL com pyenv

1. **Instalar pyenv** (se ainda não tiver):
   ```bash
   curl https://pyenv.run | bash
   ```

2. **Adicionar ao ~/.bashrc ou ~/.zshrc**:
   ```bash
   export PATH="$HOME/.pyenv/bin:$PATH"
   eval "$(pyenv init -)"
   ```

3. **Recarregar o shell**:
   ```bash
   source ~/.bashrc  # ou source ~/.zshrc
   ```

4. **Instalar dependências do pyenv**:
   ```bash
   sudo apt update
   sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git
   ```

5. **Instalar Python 3.14.5**:
   ```bash
   pyenv install 3.14.5
   pyenv local 3.14.5
   ```

6. **Criar ambiente virtual**:
   ```bash
   python -m venv venv
   ```

7. **Ativar ambiente virtual**:
   ```bash
   source venv/bin/activate
   ```

8. **Instalar dependências**:
   ```bash
   pip install -r requirements.txt
   ```

9. **Configurar variáveis de ambiente**:
   - Copie `.env.exemplo` para `.env`
   - Preencha as chaves de API no arquivo `.env`

10. **Testar instalação**:
    ```bash
    python teste_instalacao.py
    ```

### Opção 3: WSL sem pyenv (usando venv padrão)

1. **Verificar/instalar Python 3.14.5**:
   ```bash
   python3 --version
   # Se não tiver a versão correta, instale via apt:
   sudo apt update
   sudo apt install python3.14 python3.14-venv
   ```

2. **Criar ambiente virtual**:
   ```bash
   python3 -m venv venv
   ```

3. **Ativar ambiente virtual**:
   ```bash
   source venv/bin/activate
   ```

4. **Instalar dependências**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Configurar variáveis de ambiente**:
   - Copie `.env.exemplo` para `.env`
   - Preencha as chaves de API no arquivo `.env`

6. **Testar instalação**:
   ```bash
   python teste_instalacao.py
   ```

## Estrutura do Projeto

- `aula03/` - Exemplos da aula 3
- `aula04/` - Exemplos da aula 4
- `aula05/` - Exemplos da aula 5 (Prompt Templates)
- `aula06/` - Exemplos da aula 6 (Output Parsers)
- `aula07-08/` - Exemplos das aulas 7 e 8 (Chains: Básica, Sequencial, Paralela e Branch)
- `aula09/` - Exemplos da aula 9 (Document Loaders: PDF, TXT, Web, CSV)
- `requirements.txt` - Dependências do projeto
- `teste_instalacao.py` - Script para testar a instalação

## Notas

- O projeto utiliza LangChain, LangGraph e integrações com Groq, Anthropic e Google
- Certifique-se de ter as chaves de API necessárias configuradas no arquivo `.env`
