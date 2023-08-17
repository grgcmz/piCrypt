import Enigma as enigma
import logging

def setupLogger():
    logging.basicConfig()
    logging.root.setLevel(logging.NOTSET)



def main():
    setupLogger()
    logger = logging.getLogger("main")
    logger.info("logger initialized")
    filepath = "/home/pi/Documents/piCrypt/test.txt"
    private_key, public_key = enigma.generate_private_key()
    enigma.encrypt_file(public_key, filepath)
    enigma.serialize_keys(private_key, public_key)


if __name__ == '__main__':
    main()