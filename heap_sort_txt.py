import os
import random
import time
import tempfile

# Vantagem: tem bom desempenho em listas grandes.
# Desvantagem: é mais difícil de entender.
def ajustar(numeros, tamanho, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2
    if esquerda < tamanho and numeros[esquerda] > numeros[maior]:
        maior = esquerda
    if direita < tamanho and numeros[direita] > numeros[maior]:
        maior = direita
    if maior != i:
        numeros[i], numeros[maior] = numeros[maior], numeros[i]
        ajustar(numeros, tamanho, maior)


def ordenar(lista):
    numeros = lista.copy()
    tamanho = len(numeros)
    for i in range(tamanho // 2 - 1, -1, -1):
        ajustar(numeros, tamanho, i)
    for i in range(tamanho - 1, 0, -1):
        numeros[0], numeros[i] = numeros[i], numeros[0]
        ajustar(numeros, i, 0)
    return numeros


QUANTIDADE = 100000


def criar_arquivo(caminho):
    try:
        with open(caminho, "x", encoding="utf-8") as arquivo:
            for i in range(QUANTIDADE):
                arquivo.write(str(random.randint(0, 9999)) + "\n")
        print("Arquivo de entrada criado com 100.000 numeros.")
        return True
    except FileExistsError:
        print("O arquivo de entrada ja existe e sera utilizado.")
        return True
    except OSError as erro:
        print("Erro ao criar arquivo de entrada:", erro)
        return False


def ler_arquivo(caminho):
    numeros = []
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha_numero, linha in enumerate(arquivo, start=1):
                try:
                    numero = int(linha.strip())
                except ValueError:
                    print("Numero invalido na linha", linha_numero)
                    return None
                numeros.append(numero)
                if len(numeros) > QUANTIDADE:
                    print("Erro: o arquivo possui mais de 100.000 numeros.")
                    return None
    except (OSError, UnicodeError) as erro:
        print("Erro ao ler arquivo de entrada:", erro)
        return None

    if len(numeros) != QUANTIDADE:
        print("Erro: o arquivo possui", len(numeros), "numeros. Sao necessarios 100.000.")
        return None
    return numeros


def salvar_arquivo(caminho, numeros):
    if os.path.exists(caminho):
        try:
            resposta = input("O arquivo de saida ja existe. Deseja substituir? (s/n): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("Sem confirmacao. O arquivo existente foi preservado.")
            return False
        if resposta != "s":
            print("Operacao cancelada. O arquivo existente foi preservado.")
            return False

    temporario = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8",
                                         dir=os.path.dirname(caminho),
                                         suffix=".tmp", delete=False) as arquivo:
            temporario = arquivo.name
            for numero in numeros:
                arquivo.write(str(numero) + "\n")
        os.replace(temporario, caminho)
    except OSError as erro:
        print("Erro ao salvar arquivo ordenado:", erro)
        return False
    finally:
        if temporario is not None and os.path.exists(temporario):
            os.remove(temporario)

    print("Arquivo de saida salvo com 100.000 numeros ordenados.")
    return True


def executar():
    pasta = os.path.dirname(os.path.abspath(__file__))
    entrada = os.path.join(pasta, "numeros.txt")
    saida = os.path.join(pasta, "numeros_ordenados.txt")

    if not os.path.exists(entrada):
        if not criar_arquivo(entrada):
            return
    else:
        print("O arquivo de entrada ja existe e sera utilizado.")

    numeros = ler_arquivo(entrada)
    if numeros is None:
        return

    inicio = time.time()
    ordenados = ordenar(numeros)
    segundos = round(time.time() - inicio, 3)

    for i in range(1, len(ordenados)):
        if ordenados[i] < ordenados[i - 1]:
            print("Erro: a lista nao foi ordenada corretamente.")
            return

    print("Heap Sort finalizado em", segundos, "segundos.")
    salvar_arquivo(saida, ordenados)


if __name__ == "__main__":
    executar()
