import os
import subprocess
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

def converter_arquivo(arquivo_opus, pasta_atual):
    """
    Converte um arquivo .opus para .ogg usando ffmpeg.
    Retorna True se sucesso, False se erro.
    """
    if not arquivo_opus.lower().endswith('.opus'):
        print(f"Ignorando {arquivo_opus}: não é .opus")
        return False
    
    caminho_completo_opus = os.path.join(pasta_atual, arquivo_opus)
    arquivo_ogg = arquivo_opus.replace('.opus', '.ogg')
    caminho_completo_ogg = os.path.join(pasta_atual, arquivo_ogg)
    arquivo_temp = caminho_completo_ogg + '.tmp'
    
    # Comando ffmpeg: converte opus para ogg vorbis, com formato explícito
    comando = [
        'ffmpeg', '-i', caminho_completo_opus,
        '-c:a', 'libvorbis',  # Codec Vorbis para Ogg
        '-f', 'ogg',         # Força o formato Ogg
        '-y',  # Sobrescreve sem perguntar
        arquivo_temp
    ]
    
    try:
        resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
        print(f"  -> Conversão OK: {arquivo_opus} -> {arquivo_temp}")
        
        # Verifica se o temp foi criado e tem tamanho > 0
        if os.path.exists(arquivo_temp) and os.path.getsize(arquivo_temp) > 0:
            # Move o temp para o nome final .ogg
            os.rename(arquivo_temp, caminho_completo_ogg)
            # Remove o .opus original
            os.remove(caminho_completo_opus)
            print(f"  -> Substituído: {caminho_completo_ogg} (original removido)")
            return True
        else:
            if os.path.exists(arquivo_temp):
                os.remove(arquivo_temp)
            print(f"  -> Erro: Arquivo temp inválido para {arquivo_opus}")
            return False
    
    except subprocess.CalledProcessError as e:
        print(f"  -> Erro no ffmpeg para {arquivo_opus}: {e.stderr}")
        if os.path.exists(arquivo_temp):
            os.remove(arquivo_temp)
        return False
    except Exception as e:
        print(f"  -> Erro inesperado para {arquivo_opus}: {e}")
        if os.path.exists(arquivo_temp):
            os.remove(arquivo_temp)
        return False

def processar_subpasta(subpasta_nome, pasta_raiz, num_subpastas, indice):
    """
    Processa todos os .opus em uma subpasta específica.
    """
    caminho_subpasta = os.path.join(pasta_raiz, subpasta_nome)
    print(f"\nProcessando subpasta {indice}/{num_subpastas}: {subpasta_nome}")
    
    # Lista arquivos .opus na subpasta
    arquivos_opus = [f for f in os.listdir(caminho_subpasta) if f.lower().endswith('.opus')]
    
    if not arquivos_opus:
        print(f"  Nenhum .opus encontrado em {subpasta_nome}.")
        return 0
    
    print(f"  Encontrados {len(arquivos_opus)} .opus. Iniciando conversão...")
    
    sucessos = 0
    for arquivo in arquivos_opus:
        if converter_arquivo(arquivo, caminho_subpasta):
            sucessos += 1
    
    print(f"  Concluído nesta subpasta: {sucessos}/{len(arquivos_opus)} sucesso(s).")
    return sucessos

def selecionar_pasta():
    """
    Abre diálogo para selecionar pasta raiz.
    """
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    pasta = filedialog.askdirectory(title="Selecione a pasta RAIZ com subpastas de músicas (.opus)")
    root.destroy()
    return pasta

def main():
    # Seleciona a pasta raiz
    pasta_raiz = selecionar_pasta()
    if not pasta_raiz:
        print("Nenhuma pasta selecionada. Saindo.")
        return
    
    print(f"Pasta raiz selecionada: {pasta_raiz}")
    
    # Lista subpastas (diretórios dentro da raiz)
    subpastas = [d for d in os.listdir(pasta_raiz) if os.path.isdir(os.path.join(pasta_raiz, d))]
    
    if not subpastas:
        messagebox.showinfo("Info", "Nenhuma subpasta encontrada na pasta raiz selecionada.")
        return
    
    print(f"Subpastas encontradas: {len(subpastas)}")
    
    total_sucessos = 0
    for i, subpasta in enumerate(subpastas, 1):
        sucessos_sub = processar_subpasta(subpasta, pasta_raiz, len(subpastas), i)
        total_sucessos += sucessos_sub
    
    resumo = f"Processo concluído! Total: {total_sucessos} arquivos convertidos em {len(subpastas)} subpastas."
    print(resumo)
    messagebox.showinfo("Concluído", resumo)

if __name__ == "__main__":
    main()