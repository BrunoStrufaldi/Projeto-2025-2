from database_manager import remove_image


# COLOQUE AQUI O ID DA IMAGEM QUE VOCÊ QUER REMOVER
# (Você encontra o ID olhando no SQLite Viewer)

id_para_deletar = 2 

print(f"Atenção! Tentando remover a imagem com ID: {id_para_deletar}")
resposta = input("Você tem certeza? (s/n): ")

if resposta.lower() == 's':
    remove_image(id_para_deletar)
    print("\nOperação concluída.")
else:
    print("\nOperação cancelada.")