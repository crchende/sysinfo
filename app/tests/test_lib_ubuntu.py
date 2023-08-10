import logging
logger = logging.getLogger(__name__)

import lib.ubuntu as ubuntu

def test_versiune_os():
    vos = ubuntu.gaseste_versiune_ubuntu()

    if "Ubuntu" in vos:
        logger.info(f"Sistemul de operare este Ubuntu: {vos}")
        assert True
    else:
        logger.error(f"Sistemul de operare NU este Ubuntu: {vos}")
        assert False

def test_informatii_memorie():
    mem_info = ubuntu.gaseste_informatii_memorie()

    if "Mem" in mem_info and "Swap" in mem_info:
        logger.info(f"Gasit informatii memorie:\n{mem_info}")
        assert True
    else:
        logger.error(f"Nu am gasit informatii despre memorie:\n{mem_info}")
        assert False 
