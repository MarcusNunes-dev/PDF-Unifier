# PDF Unifier

Uma ferramenta **desktop simples e segura** para unificar arquivos PDF, desenvolvida em **Python** com interface gráfica **Tkinter**.

Inclui um fluxo de *"autenticação"* via **Microsoft Forms** para registro de acessos corporativos, garantindo rastreamento de uso e estatísticas de adesão.

> Criado para otimizar fluxos de trabalho em ambientes corporativos, permitindo unificar múltiplos PDFs de forma rápida, segura, gratuita e **local** (sem depender de serviços externos).

---

## Funcionalidades

-   **Unificação de PDFs**: Selecione múltiplos arquivos, reordene via drag-and-drop e salve o resultado em um único PDF.
-   **Registro de Acessos**: Tela inicial com integração ao Microsoft Forms para coletar e-mail corporativo (com validação de domínio).
-   **Delay no Botão de Continuar**: O botão *“Continuar para o APP”* só aparece após 5 segundos.
-   **Interface Intuitiva**: Barra de progresso, status em tempo real e suporte a threads (UI não trava).
-   **Segurança**: Processamento 100% local, sem envio de arquivos para servidores externos.

---

## Requisitos

-   **Sistema Operacional**: Windows 10/11 (testado). Compatível com macOS/Linux com ajustes.
-   **Python**: Versão **3.8+** (instale em [python.org](https://www.python.org/)).
-   **Bibliotecas necessárias**:
    ```bash
    pip install PyPDF2
    ```

### Principais dependências

-   `tkinter` (nativo) – Interface gráfica.
-   `PyPDF2` – Manipulação de PDFs.
-   `threading` (nativo) – Processamento assíncrono.
-   `os`, `pathlib` (nativos) – Gerenciamento de arquivos.
-   `webbrowser` (nativo) – Abertura do Microsoft Forms.
-   `filedialog`, `messagebox`, `ttk` (submódulos `tkinter`) – Diálogos e progresso.

### Instalação

1.  Clone o repositório:
    ```bash
    git clone https://github.com/seuusuario/PDF-Unifier.git
    cd PDF-Unifier
    ```
2.  Instale as bibliotecas (se necessário):
    ```bash
    pip install -r requirements.txt
    ```
3.  Execute o app:
    ```bash
    python main.py
    ```

### Criar executável (`.exe`) com PyInstaller

1.  Instale o PyInstaller:
    ```bash
    pip install pyinstaller
    ```
2.  Gere o executável:
    ```bash
    pyinstaller --onefile --windowed main.py
    ```
    *O arquivo `.exe` gerado ficará no diretório `dist/`.*

---

## Como Usar

1.  Abra o app → aparecerá a tela inicial com instruções.
2.  Clique em **“Abrir Formulário de Login”** → o Microsoft Forms será aberto no navegador.
3.  Preencha o Forms (validação de domínio obrigatória, ex.: `@suaempresa.com`).
4.  Após 5 segundos, o botão **“Continuar para o APP”** aparecerá → clique nele.
5.  Na tela principal:
    -   Adicione PDFs usando o botão ou arrastando e soltando (drag-and-drop).
    -   Reordene, remova arquivos ou limpe a lista.
    -   Clique em **“Unificar e Salvar PDF”** e escolha o destino do novo arquivo.

*Observação: O registro via Forms serve apenas para estatísticas internas de adesão.*

---

## Configurações

-   **Microsoft Forms**: Altere a URL do seu formulário no código (função `abrir_forms`):
    ```python
    forms_url = "https://forms.office.com/r/SeuFormID"
    ```

-   **Delay do botão**: Ajuste o tempo de espera (em milissegundos) na linha:
    ```python
    self.root.after(5000, ...)  # 5000 ms = 5 segundos
    ```

-   **Logs**: Os acessos são registrados no forms criado, via dados estruturados da ferramenta da microsoft`.

---

## Contribuições

Contribuições são bem-vindas!

1.  Faça um *fork* do repositório.
2.  Crie uma nova *branch* (`git checkout -b feature/minha-feature`).
3.  Faça o *commit* de suas alterações (`git commit -m 'Adiciona minha contribuição'`).
4.  Envie um *pull request*.

---

## Contato

-   **Desenvolvido por**: Marcus Nunes
-   **LinkedIn**: `https://www.linkedin.com/in/marcus-vinicius-nunes/`
