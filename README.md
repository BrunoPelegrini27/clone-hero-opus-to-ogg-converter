# Conversor de .opus para .ogg para Clone Hero

**Problema comum:** Músicas baixadas do [Enchor.us](https://www.enchor.us) vêm em .opus, e o Clone Hero nem sempre toca direito (pula pro fim ou não carrega áudio). Este script converte pra .ogg (formato compatível) e substitui os arquivos originais.

## Como Usar (Windows)
1. **Instale o Python:** Baixe em [python.org](https://www.python.org/downloads/) (marque "Add to PATH").
2. **Instale o FFmpeg:** Baixe o ZIP em [gyan.dev/ffmpeg](https://www.gyan.dev/ffmpeg/builds/), extraia pra `C:\ffmpeg`, adicione `C:\ffmpeg\bin` ao PATH (Configurações > Sistema > Sobre > Configurações avançadas > Variáveis de ambiente).
3. **Baixe este script:** Clique no botão verde "Code > Download ZIP", extraia.
4. **Rode:** Abra o Prompt de Comando (Win+R > cmd), vá pra pasta do script (`cd Downloads\clone-hero-opus-to-ogg-converter-main`), digite `python converter_opus_para_ogg.py`.
5. **Selecione a pasta raiz** (ex: sua pasta "songs" com subpastas de músicas).
6. **Aguarde:** Ele processa subpasta por subpasta. Backup antes!

**Testado no Windows 11.** Se der erro, confira o PATH ou mande issue aqui.

## Créditos
Feito com ❤️ por BrunoPelegrini27 e Grok (xAI). Baseado em FFmpeg.
