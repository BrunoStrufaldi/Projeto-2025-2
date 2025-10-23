# database_setup.py
import sqlite3
import os

DB_FILE = "deforestation_monitor.db"
IMAGE_DIR = "images"

def setup_database():
    """
    Cria o banco de dados e a tabela 'images' se eles não existirem.
    Cria também o diretório para armazenar as imagens.
    """
    # Cria o diretório para as imagens se ele não existir
    if not os.path.exists(IMAGE_DIR):
        print(f"Criando diretório para imagens em: '{IMAGE_DIR}/'")
        os.makedirs(IMAGE_DIR)

    # Conecta ao banco de dados (cria o arquivo se não existir)
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # SQL para criar a tabela com campos bem definidos
    # Adicionamos 'UNIQUE (file_path)' para garantir que não haja imagens duplicadas.
    # Adicionamos 'last_updated' para saber quando a IA rodou pela última vez na imagem.
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS images (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT NOT NULL,
        file_path TEXT NOT NULL UNIQUE,
        capture_date DATE,
        latitude REAL NOT NULL,
        longitude REAL NOT NULL,
        source TEXT, -- Fonte da imagem (ex: 'Drone', 'Sentinel-2', 'Landsat-8')
        
        -- Colunas que serão preenchidas pela IA
        analysis_status TEXT DEFAULT 'pending', -- pending, processing, success, error
        deforestation_percentage REAL DEFAULT 0.0,
        deforestation_area_sqm REAL DEFAULT 0.0, -- Área em metros quadrados, se aplicável
        confidence_score REAL DEFAULT 0.0, -- Pontuação de confiança da IA
        
        -- Metadados de controle
        added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_updated TIMESTAMP
    );
    """

    cursor.execute(create_table_sql)
    print("Banco de dados verificado. Tabela 'images' está pronta.")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()