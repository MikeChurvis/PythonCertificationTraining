class Scanner:
    def scan(self):
        print("{} method from {} class".format('scan', 'Scanner'))


class Printer:
    def print(self):
        print("{} method from {} class".format('print', 'Printer'))


class Fax:
    def print(self):
        print("{} method from {} class".format('print', 'Fax'))

    def send(self):
        print("{} method from {} class".format('send', 'Fax'))


class MFD_SPF(Scanner, Printer, Fax):
    pass


class MFD_SFP(Scanner, Fax, Printer):
    pass


if __name__ == '__main__':
    def main():
        scanner_printer_fax = MFD_SPF()
        scanner_fax_printer = MFD_SFP()

        for device in (scanner_printer_fax, scanner_fax_printer):
            print(type(device).__bases__)
            device.scan()
            device.print()
            device.send()


    main()
