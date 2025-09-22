PDF Unifier

Uma ferramenta desktop simples e segura para unificar arquivos PDF, desenvolvida em Python com interface gráfica Tkinter.

Inclui um fluxo de "autenticação" via Microsoft Forms para registro de acessos corporativos, garantindo rastreamento de uso e estatísticas de adesão.

Criado para otimizar fluxos de trabalho em ambientes corporativos, permitindo unificar múltiplos PDFs de forma rápida, gratuita e local (sem depender de serviços externos).

Funcionalidades

Unificação de PDFs: selecione múltiplos arquivos, reordene via drag-and-drop e salve o resultado em um único PDF.

Registro de Acessos: tela inicial com integração ao Microsoft Forms para coletar e-mail corporativo (com validação de domínio).

Delay no Botão de Continuar: botão “Continuar para o APP” só aparece após 5 segundos.

Interface Intuitiva: barra de progresso, status em tempo real e suporte a threads (UI não trava).

Segurança: processamento 100% local, sem envio de arquivos para servidores externos.

Requisitos

Sistema Operacional: Windows 10/11 (testado). Compatível com macOS/Linux com ajustes.

Python: versão 3.8+ (instale em python.org
).

Bibliotecas necessárias:

pip install PyPDF2

Principais dependências

tkinter (nativo) – interface gráfica

PyPDF2 – manipulação de PDFs

threading (nativo) – processamento assíncrono

logging, datetime (nativos) – logs de acesso

os, pathlib (nativos) – gerenciamento de arquivos

webbrowser (nativo) – abertura do Microsoft Forms

filedialog, messagebox, ttk (submódulos tkinter) – diálogos e progresso

Instalação

Clone o repositório:

git clone https://github.com/seuusuario/PDF-Unifier.git
cd PDF-Unifier


Instale as bibliotecas (se necessário):

pip install -r requirements.txt


Execute o app:

python main.py

Criar executável (.exe) com PyInstaller
pip install pyinstaller
pyinstaller --onefile --windowed main.py


O .exe gerado ficará em dist/.

Como Usar

Abra o app → aparece a tela inicial com instruções.

Clique em “Abrir Formulário de Login” → abre o Microsoft Forms no navegador.

Preencha o Forms (validação de domínio obrigatória, ex.: @suaempresa.com).

Após 5 segundos, o botão “Continuar para o APP” aparece → clique.

Na tela principal:

Adicione PDFs (botão ou drag-and-drop).

Reordene, remova ou limpe a lista.

Clique em “Unificar e Salvar PDF” → escolha o destino do arquivo.

Observação: O registro via Forms serve apenas para estatísticas internas de adesão.

Configurações

Microsoft Forms: altere no código (abrir_forms) a URL do seu formulário:

forms_url = "https://forms.office.com/r/SeuFormID"


Validação de domínio: configure o Forms com regex:

^[a-zA-Z0-9_.+-]+@suaempresa\.com$


Delay do botão: ajuste o tempo em:

self.root.after(5000, ...)  # 5000 ms = 5 segundos


Logs: acessos registrados em access_log.txt.

Contribuições

Contribuições são bem-vindas!

Faça um fork do repositório.

Crie uma branch (git checkout -b feature/minha-feature).

Commit suas alterações (git commit -m 'Minha contribuição').

Envie um pull request.

Licença

Este projeto está sob a licença MIT.
Sinta-se livre para usar, modificar e distribuir.

Contato

Desenvolvido por Marcus Nunes.

E-mail: seuemail@suaempresa.com
LinkedIn: [Seu LinkedIn aqui]
