import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter import font as tkfont
import os
from pathlib import Path
from PyPDF2 import PdfMerger
import threading
import webbrowser

class PDFUnificador:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Unify")
        self.root.geometry("600x500")
        self.root.minsize(500, 400)
        
        # Lista para armazenar caminhos dos arquivos
        self.lista_arquivos = []
        
        # Configurar estilo
        self.configurar_estilo()
        
        # Criar interface
        self.criar_interface()
        
        # Configurar drag and drop (arrastar e soltar)
        self.configurar_drag_drop()

    
    
    def configurar_estilo(self):
        """Configura o estilo visual da aplicação"""
        self.root.configure(bg='#f0f0f0')
        self.fonte_padrao = tkfont.Font(family="Arial", size=10)
        self.fonte_titulo = tkfont.Font(family="Arial", size=12, weight="bold")
    
    def criar_interface(self):
        """Cria todos os elementos da interface"""
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Título
        titulo = tk.Label(main_frame, text="Unificador de PDFs",
                         font=self.fonte_titulo, bg='#f0f0f0')
        titulo.pack(pady=(0, 10))
        
        # Frame de botões superiores
        frame_botoes_sup = tk.Frame(main_frame, bg='#f0f0f0')
        frame_botoes_sup.pack(fill=tk.X, pady=(0, 10))
        
        # Botões principais
        btn_selecionar = tk.Button(
            frame_botoes_sup, 
            text="➕ Adicionar PDFs", 
            command=self.selecionar_pdfs,
            bg='#4CAF50', 
            fg='white',
            font=self.fonte_padrao,
            padx=15, 
            pady=5,
            cursor='hand2'
        )
        btn_selecionar.pack(side=tk.LEFT, padx=5)
        
        btn_limpar = tk.Button(
            frame_botoes_sup, 
            text="🗑️ Limpar Lista", 
            command=self.limpar_lista,
            bg='#f44336', 
            fg='white',
            font=self.fonte_padrao,
            padx=15, 
            pady=5,
            cursor='hand2'
        )
        btn_limpar.pack(side=tk.LEFT, padx=5)
        
        # Frame da lista
        frame_lista = tk.Frame(main_frame, bg='#f0f0f0')
        frame_lista.pack(fill=tk.BOTH, expand=True)
        
        # Label informativo
        info_label = tk.Label(
            frame_lista, 
            text="Arquivos selecionados (arraste para reordenar):",
            font=self.fonte_padrao,
            bg='#f0f0f0'
        )
        info_label.pack(anchor=tk.W)
        
        # Frame para listbox e scrollbar
        list_frame = tk.Frame(frame_lista)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        
        # Scrollbar
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox
        self.listbox = tk.Listbox(
            list_frame,
            yscrollcommand=scrollbar.set,
            font=self.fonte_padrao,
            selectmode=tk.SINGLE,
            height=10
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox.yview)
        
        # Bind para drag and drop na listbox
        self.listbox.bind('<Button-1>', self.on_click)
        self.listbox.bind('<B1-Motion>', self.on_drag)
        self.listbox.bind('<ButtonRelease-1>', self.on_release)
        self.listbox.bind('<Double-Button-1>', self.remover_item)
        
        # Frame de botões inferiores
        frame_botoes_inf = tk.Frame(main_frame, bg='#f0f0f0')
        frame_botoes_inf.pack(fill=tk.X, pady=(10, 0))
        
        # Botões de ação na lista
        btn_subir = tk.Button(
            frame_botoes_inf,
            text="⬆️ Subir",
            command=self.mover_para_cima,
            font=self.fonte_padrao,
            padx=10,
            cursor='hand2'
        )
        btn_subir.pack(side=tk.LEFT, padx=5)
        
        btn_descer = tk.Button(
            frame_botoes_inf,
            text="⬇️ Descer",
            command=self.mover_para_baixo,
            font=self.fonte_padrao,
            padx=10,
            cursor='hand2'
        )
        btn_descer.pack(side=tk.LEFT, padx=5)
        
        btn_remover = tk.Button(
            frame_botoes_inf,
            text="❌ Remover Selecionado",
            command=self.remover_selecionado,
            font=self.fonte_padrao,
            padx=10,
            cursor='hand2'
        )
        btn_remover.pack(side=tk.LEFT, padx=5)
        
        # Botão de salvar
        btn_salvar = tk.Button(
            main_frame,
            text="💾 Unificar e Salvar PDF",
            command=self.salvar_pdf,
            bg='#2196F3',
            fg='white',
            font=tkfont.Font(family="Arial", size=12, weight="bold"),
            padx=20,
            pady=10,
            cursor='hand2'
        )
        btn_salvar.pack(pady=(15, 0))
        
        # Barra de progresso (inicialmente oculta)
        self.progress = ttk.Progressbar(
            main_frame,
            mode='indeterminate',
            length=300
        )
        
        # Status label
        self.status_label = tk.Label(
            main_frame,
            text="Pronto para unificar PDFs",
            font=self.fonte_padrao,
            bg='#f0f0f0',
            fg='#666'
        )
        self.status_label.pack(pady=(5, 0))

        # Rodapé com créditos
        rodape = tk.Label(
            self.root,
            text="PDF Unifier v1.0",  # Substituído por versão genérica
            font=("Arial", 8),
            fg="#888888",
            bg='#f0f0f0'
        )
        rodape.pack(side=tk.BOTTOM, anchor=tk.E, padx=10, pady=5)
    
    def configurar_drag_drop(self):
        """Configura o drag and drop de arquivos"""
        self.drag_start_index = None
    
    def on_click(self, event):
        """Captura o clique inicial para drag and drop"""
        self.drag_start_index = self.listbox.nearest(event.y)
    
    def on_drag(self, event):
        """Atualiza a posição durante o arraste"""
        i = self.listbox.nearest(event.y)
        if i < self.drag_start_index:
            x = self.listbox.get(i)
            self.listbox.delete(i)
            self.listbox.insert(i+1, x)
            self.drag_start_index = i
        elif i > self.drag_start_index:
            x = self.listbox.get(i)
            self.listbox.delete(i)
            self.listbox.insert(i-1, x)
            self.drag_start_index = i
    
    def on_release(self, event):
        """Finaliza o drag and drop e atualiza a lista"""
        self.atualizar_lista_arquivos()
    
    def selecionar_pdfs(self):
        """Abre diálogo para selecionar arquivos PDF"""
        arquivos = filedialog.askopenfilenames(
            title="Selecione os PDFs",
            filetypes=[("Arquivos PDF", "*.pdf"), ("Todos os arquivos", "*.*")]
        )
        
        if arquivos:
            # Adicionar apenas arquivos que ainda não estão na lista
            novos_arquivos = [arq for arq in arquivos if arq not in self.lista_arquivos]
            self.lista_arquivos.extend(novos_arquivos)
            self.atualizar_lista()
            
            if novos_arquivos:
                self.status_label.config(
                    text=f"{len(novos_arquivos)} arquivo(s) adicionado(s)",
                    fg='green'
                )
            else:
                self.status_label.config(
                    text="Arquivos já estavam na lista",
                    fg='orange'
                )
    
    def atualizar_lista(self):
        """Atualiza a exibição da lista de arquivos"""
        self.listbox.delete(0, tk.END)
        for i, arquivo in enumerate(self.lista_arquivos, 1):
            nome = os.path.basename(arquivo)
            self.listbox.insert(tk.END, f"{i}. {nome}")
    
    def atualizar_lista_arquivos(self):
        """Atualiza a lista interna baseada na ordem da listbox"""
        nova_lista = []
        for i in range(self.listbox.size()):
            # Extrai o índice original do nome do arquivo
            item = self.listbox.get(i)
            # Remove o número e o ponto do início
            nome_arquivo = item.split('. ', 1)[1]
            # Encontra o caminho completo correspondente
            for arquivo in self.lista_arquivos:
                if os.path.basename(arquivo) == nome_arquivo:
                    nova_lista.append(arquivo)
                    break
        self.lista_arquivos = nova_lista
    
    def mover_para_cima(self):
        """Move o item selecionado para cima"""
        try:
            index = self.listbox.curselection()[0]
            if index > 0:
                item = self.lista_arquivos.pop(index)
                self.lista_arquivos.insert(index - 1, item)
                self.atualizar_lista()
                self.listbox.selection_set(index - 1)
        except IndexError:
            self.status_label.config(text="Selecione um arquivo para mover", fg='red')
    
    def mover_para_baixo(self):
        """Move o item selecionado para baixo"""
        try:
            index = self.listbox.curselection()[0]
            if index < len(self.lista_arquivos) - 1:
                item = self.lista_arquivos.pop(index)
                self.lista_arquivos.insert(index + 1, item)
                self.atualizar_lista()
                self.listbox.selection_set(index + 1)
        except IndexError:
            self.status_label.config(text="Selecione um arquivo para mover", fg='red')
    
    def remover_selecionado(self):
        """Remove o item selecionado da lista"""
        try:
            index = self.listbox.curselection()[0]
            self.lista_arquivos.pop(index)
            self.atualizar_lista()
            self.status_label.config(text="Arquivo removido", fg='orange')
        except IndexError:
            self.status_label.config(text="Selecione um arquivo para remover", fg='red')
    
    def remover_item(self, event):
        """Remove item com duplo clique"""
        self.remover_selecionado()
    
    def limpar_lista(self):
        """Limpa toda a lista de arquivos"""
        if self.lista_arquivos:
            resposta = messagebox.askyesno(
                "Confirmar",
                "Deseja realmente limpar toda a lista?"
            )
            if resposta:
                self.lista_arquivos.clear()
                self.atualizar_lista()
                self.status_label.config(text="Lista limpa", fg='orange')
    
    def salvar_pdf(self):
        """Unifica e salva os PDFs em um arquivo"""
        if not self.lista_arquivos:
            messagebox.showwarning("Aviso", "Nenhum PDF selecionado!")
            return
        
        # Verificar se todos os arquivos ainda existem
        arquivos_faltando = []
        for arquivo in self.lista_arquivos:
            if not os.path.exists(arquivo):
                arquivos_faltando.append(os.path.basename(arquivo))
        
        if arquivos_faltando:
            messagebox.showerror(
                "Erro",
                f"Os seguintes arquivos não foram encontrados:\n" + 
                "\n".join(arquivos_faltando)
            )
            return
        
        caminho_saida = filedialog.asksaveasfilename(
            title="Salvar PDF Unificado",
            defaultextension=".pdf",
            filetypes=[("Arquivos PDF", "*.pdf")]
        )
        
        if caminho_saida:
            # Executar em thread separada para não travar a interface
            threading.Thread(
                target=self.processar_pdf,
                args=(caminho_saida,),
                daemon=True
            ).start()
    
    def processar_pdf(self, caminho_saida):
        """Processa a unificação dos PDFs em thread separada"""
        try:
            # Mostrar progresso
            self.root.after(0, self.mostrar_progresso)
            
            merger = PdfMerger()
            
            for i, pdf in enumerate(self.lista_arquivos):
                try:
                    merger.append(pdf)
                    # Atualizar status
                    self.root.after(0, self.atualizar_status, 
                                  f"Processando {i+1} de {len(self.lista_arquivos)}...")
                except Exception as e:
                    self.root.after(0, self.esconder_progresso)
                    self.root.after(0, messagebox.showerror, "Erro", 
                                  f"Erro ao processar {os.path.basename(pdf)}: {str(e)}")
                    return
            
            # Salvar o arquivo
            with open(caminho_saida, 'wb') as output_file:
                merger.write(output_file)
            
            merger.close()
            
            # Esconder progresso e mostrar sucesso
            self.root.after(0, self.esconder_progresso)
            self.root.after(0, self.atualizar_status, 
                          f"PDF salvo com sucesso!",
                          'green')
            self.root.after(0, messagebox.showinfo, "Sucesso", 
                          f"PDF unificado salvo em:\n{caminho_saida}")
            
        except Exception as e:
            self.root.after(0, self.esconder_progresso)
            self.root.after(0, messagebox.showerror, "Erro", 
                          f"Erro ao salvar o PDF:\n{str(e)}")
        finally:
            try:
                merger.close()
            except:
                pass
    
    def mostrar_progresso(self):
        """Mostra a barra de progresso"""
        self.progress.pack(pady=5)
        self.progress.start(10)
    
    def esconder_progresso(self):
        """Esconde a barra de progresso"""
        self.progress.stop()
        self.progress.pack_forget()
    
    def atualizar_status(self, texto, cor='#666'):
        """Atualiza o texto de status"""
        self.status_label.config(text=texto, fg=cor)


# Função principal
def main():
    root = tk.Tk()
    app = PDFUnificador(root)
    root.mainloop()


if __name__ == "__main__":
    main()