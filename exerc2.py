def verificar_letra_a(string):
    string_lower = string.lower()
    contador = string_lower.count('a')
    if contador > 0:
        print(f"A letra 'a' aparece {contador} vez(es) na string.")
    else:
        print("A letra 'a' não foi encontrada na string.")
texto_predefinido = "Exemplo de string com a letra A."
texto_usuario = input("Informe uma string: ")
verificar_letra_a(texto_usuario)
