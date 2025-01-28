import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_folder="logs", log_file="app.log", max_bytes=1048576, backup_count=5):
    """
    Configura o logger para salvar logs em um arquivo com rotação.

    :param log_folder: Pasta onde os logs serão salvos.
    :param log_file: Nome do arquivo de log.
    :param max_bytes: Tamanho máximo do arquivo de log antes de rotacionar (em bytes).
    :param backup_count: Número de arquivos de log antigos a serem mantidos.
    """
    # Cria a pasta de logs se não existir
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    # Caminho completo para o arquivo de log
    log_path = os.path.join(log_folder, log_file)

    # Configuração do logger
    logger = logging.getLogger("meu_app")
    logger.setLevel(logging.INFO)  # Define o nível de log

    # Formato das mensagens de log
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Handler para salvar logs em arquivo com rotação
    file_handler = RotatingFileHandler(
        log_path, maxBytes=max_bytes, backupCount=backup_count
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Handler para exibir logs no console (opcional)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

# Cria uma instância do logger para ser usada em todo o projeto
logger = setup_logger()