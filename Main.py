import Enigma as enigma
import logging




def main():
    logger = logging.getLogger("root")
    filepath = "/home/pi/Documents/piCrypt/test.txt"
    private_key, public_key = enigma.generate_private_key()
    enigma.encrypt_file(public_key, filepath)
    enigma.serialize_keys(private_key, public_key)


if __name__ == '__main__':
    main()