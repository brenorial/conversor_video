# Conversor de Vídeos MOV para MP4

Este é um conversor de vídeos simples para transformar arquivos de vídeo no formato MOV para o formato MP4. O aplicativo foi desenvolvido em Python usando as bibliotecas `moviepy`, `customtkinter`, e `tkinter`, e permite ao usuário selecionar um arquivo MOV, visualizar o progresso da conversão e salvar o arquivo convertido no formato MP4.

## Tecnologias Utilizadas

- Python 3.x
- `moviepy`: biblioteca para edição e manipulação de vídeos.
- `customtkinter`: framework para criar interfaces gráficas com Tkinter, que permite personalizar o estilo e aparência dos componentes.
- `tkinter`: biblioteca de interface gráfica padrão do Python.
- `threading`: para executar a conversão em uma thread separada, evitando bloqueios na interface gráfica.

## Funcionalidades

- **Selecionar e Converter**: O usuário escolhe um arquivo MOV para converter.
- **Progresso da Conversão**: O progresso da conversão é exibido como uma porcentagem (0% a 100%).
- **Mensagem de Status**: A interface gráfica informa o status da conversão, incluindo mensagens de sucesso ou erro.
- **Salvamento do Arquivo**: O usuário pode escolher onde salvar o arquivo MP4 gerado.

## Como Usar

1. **Instalar Dependências**:
   Certifique-se de ter o Python instalado no seu computador. Instale as dependências utilizando `pip`:

   ```bash
   pip install moviepy customtkinter
   ```

2. **Executar o Script**:
   Para executar o script, basta rodar o arquivo `mov_to_mp4_converter.py`:

   ```bash
   python mov_to_mp4_converter.py
   ```

3. **Passos para Conversão**:
   - Clique no botão **"Selecionar e Converter"** para escolher o arquivo MOV.
   - Selecione um local para salvar o arquivo convertido.
   - O progresso será mostrado, e ao final da conversão, você verá a mensagem **"Conversão concluída com sucesso!"**.

## Funcionalidade de Progresso

O progresso da conversão é calculado com base no número de quadros processados, atualizando a porcentagem da conversão conforme a conversão de cada quadro ocorre.

## Exemplo de Interface

A interface gráfica inclui:

- Um botão para iniciar a conversão.
- Uma barra de progresso (porcentagem).
- Um campo de status que indica se a conversão foi bem-sucedida ou se ocorreu um erro.

## Exemplo de Saída

Ao concluir a conversão, a interface mostra:

- **Progresso**: De 0% a 100%, dependendo da quantidade de quadros processados.
- **Mensagem de Status**: Se a conversão foi bem-sucedida ou se ocorreu um erro durante o processo.
