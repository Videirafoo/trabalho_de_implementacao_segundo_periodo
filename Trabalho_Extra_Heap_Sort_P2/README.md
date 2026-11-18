# Trabalho Extra P2 - Heap Sort

Projeto em Python para gerar, importar, ordenar e salvar 100.000 números inteiros em arquivos TXT.

O Heap Sort foi mantido igual ao arquivo original do repositório Videirafoo/trabalho_de_implementacao_segundo_periodo.

## Arquivos

- heap_sort.py - algoritmo original, com as funções ajustar() e ordenar().
- trabalho_extra_p2.py - programa principal com menu.
- lista_desordenada.txt - 100.000 números fora de ordem.
- lista_ordenada.txt - os mesmos 100.000 números em ordem crescente.

Cada número ocupa uma linha do TXT.

## Executar

No VS Code, abra esta pasta no terminal e digite:

    python trabalho_extra_p2.py

Menu:

1. Gerar lista com 100.000 números
2. Ordenar lista com Heap Sort
3. Salvar lista desordenada em TXT
4. Salvar lista ordenada em TXT
5. Importar lista desordenada do TXT
6. Executar todo o processo
0. Sair

Use a opção 6 para fazer o processo completo. Os dois TXT estão incluídos; se já houver um arquivo de saída, o programa pergunta antes de substituir.

## Tratamento de arquivos

- Se o TXT de entrada não existir, a opção 6 cria 100.000 números automaticamente.
- Se o TXT de entrada já existir, a opção 6 lê os mesmos números sem alterá-los.
- Confere se há 100.000 valores inteiros válidos.
- Se o arquivo de saída já existir, pede autorização para substituir.
- Grava primeiro em um arquivo temporário para não truncar o arquivo anterior em caso de falha durante a escrita.
- Os caminhos são relativos à pasta do próprio script, independentemente do diretório aberto no terminal.

Bibliotecas: somente Python 3, sem dependências externas.
