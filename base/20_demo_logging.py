import os
import platform
import logging

def tempmethod():
    if platform.platform().startswith('Windows'):
        logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
    else:
        logging_file = os.path.join(os.getenv('HOME'), 'test.log')

    print("Logging to", logging_file)
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s : %(levelname)s : %(message)s',
        filename=logging_file,
        filemode='w'
    )

    logging.debug("start of the program")
    logging.info("Doing something")
    logging.warning("Dying now")

if __name__ == '__main__':
    tempmethod()