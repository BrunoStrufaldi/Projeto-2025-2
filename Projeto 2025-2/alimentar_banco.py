# alimentar_banco.py
from database_manager import add_image

# --- COLOQUE AQUI AS INFORMAÇÕES DAS SUAS IMAGENS REAIS ---
# Exemplo de como adicionar uma imagem ao banco de dados

add_image(
    filename="foto_do_drone_01.jpg",
    file_path="images/foto_do_drone_01.jpg",
    capture_date="2025-07-15",
    latitude=-12.365,
    longitude=-55.688,
    source="UFLA - Universidade Federal de Lavras"
)

add_image(
    filename="RTEmagicC_desmate-ibama_04.jpg.jpg", 
    file_path="images/RTEmagicC_desmate-ibama_04.jpg",
    capture_date="2023-07-20",
    latitude=-3.4653,
    longitude=-62.2159,
    source="Ibama"
)
# Adicione quantas imagens precisar...
print("\nProcesso de adição de imagens concluído.")