import hashlib
from loguru import logger


def vocabulary_tool_encryption(encrypt_content):
    logger.info('vocabulary_tool_encryption running...')
    try:
        if encrypt_content is None or len(encrypt_content) == 0:
            logger.error('content is none ...')
            return

        transmit_content = encrypt_content.encode('utf-8')
        encrypted_content = hashlib.sha256(transmit_content).hexdigest()
        return encrypted_content

    except Exception as e:
        logger.error(e)

