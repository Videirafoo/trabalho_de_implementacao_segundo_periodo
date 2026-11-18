import os
import random
import tempfile
import time
from pathlib import Path
from heap_sort import ordenar

PASTA = Path(__file__).resolve().parent
ENTRADA = PASTA / 'lista_desordenada.txt'
SAIDA = PASTA / 'lista_ordenada.txt'
QUANTIDADE = 100000


def gerar_lista():
    return [random.randint(0, 9999) for i in range(QUANTIDADE)]


def ler_lista(caminho):
    numeros = []
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            for linha, texto in enumerate(arquivo, 1):
                try:
                    numeros.append(int(texto.strip()))
                except ValueError:
                    print('Erro: valor inválido na linha', linha)
                    return None
                if len(numeros) > QUANTIDADE:
                    print('Erro: o arquivo tem mais de 100.000 números.')
                    return None
    except (OSError, UnicodeError) as erro:
        print('Erro ao abrir o arquivo:', erro)
        return None

    if len(numeros) != QUANTIDADE:
        print('Erro: o arquivo precisa ter 100.000 números. Encontrados:', len(numeros))
        return None
    return numeros


def salvar_lista(caminho, numeros):
    if caminho.exists():
        try:
            resposta = input('O arquivo já existe. Substituir? (s/n): ').strip().lower()
        except (EOFError, KeyboardInterrupt):
            print('Operação cancelada.')
            return False
        if resposta != 's':
            print('Arquivo existente preservado.')
            return False

    temporario = None
    try:
        with tempfile.NamedTemporaryFile('w', encoding='utf-8', dir=PASTA,
                                         suffix='.tmp', delete=False) as arquivo:
            temporario = Path(arquivo.name)
            for numero in numeros:
                arquivo.write(str(numero) + '\n')
        os.replace(temporario, caminho)
        print('Salvo:', caminho.name)
        return True
    except OSError as erro:
        print('Erro ao salvar o arquivo:', erro)
        return False
    finally:
        if temporario is not None:
            try:
                temporario.unlink(missing_ok=True)
            except OSError:
                pass


def ordenar_lista(numeros):
    inicio = time.perf_counter()
    resultado = ordenar(numeros)
    tempo = time.perf_counter() - inicio
    if any(resultado[i] > resultado[i + 1] for i in range(len(resultado) - 1)):
        print('Erro: a lista não foi ordenada.')
        return None
    print('Heap Sort concluído em', round(tempo, 3), 'segundos.')
    return resultado


def executar_tudo():
    if ENTRADA.exists():
        numeros = ler_lista(ENTRADA)
        if numeros is None:
            return
    else:
        numeros = gerar_lista()
        if not salvar_lista(ENTRADA, numeros):
            return
    resultado = ordenar_lista(numeros)
    if resultado is not None:
        salvar_lista(SAIDA, resultado)


def main():
    desordenada = []
    ordenada = []

    while True:
        print('\n' + '=' * 44)
        print('TRABALHO EXTRA P2 - HEAP SORT')
        print('=' * 44)
        print('1 - Gerar lista com 100.000 números')
        print('2 - Ordenar lista com Heap Sort')
        print('3 - Salvar lista desordenada em TXT')
        print('4 - Salvar lista ordenada em TXT')
        print('5 - Importar lista desordenada do TXT')
        print('6 - Executar todo o processo')
        print('0 - Sair')
        escolha = input('Escolha uma opção: ').strip()

        if escolha == '1':
            desordenada = gerar_lista()
            ordenada = []
            print('Lista gerada com 100.000 números.')
        elif escolha == '2':
            if not desordenada:
                print('Primeiro gere ou importe a lista.')
            else:
                ordenada = ordenar_lista(desordenada) or []
        elif escolha == '3':
            if desordenada:
                salvar_lista(ENTRADA, desordenada)
            else:
                print('Primeiro gere ou importe a lista.')
        elif escolha == '4':
            if ordenada:
                salvar_lista(SAIDA, ordenada)
            else:
                print('Primeiro ordene a lista.')
        elif escolha == '5':
            desordenada = ler_lista(ENTRADA) or []
            ordenada = []
            if desordenada:
                print('Lista importada com', len(desordenada), 'números.')
        elif escolha == '6':
            executar_tudo()
        elif escolha == '0':
            print('Programa encerrado.')
            break
        else:
            print('Opção inválida.')


if __name__ == '__main__':
    main()
