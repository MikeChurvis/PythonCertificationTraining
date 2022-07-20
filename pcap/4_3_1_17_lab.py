from utils import get_filename_no_ext

if __name__ == "__main__":

    def main():
        filename_base = get_filename_no_ext(__file__)

        with open(f"{filename_base}.txt", "w") as sample_data_file:
            sample_data_file.write(
                "\n".join(
                    [
                        "John Smith 5",
                        "Anna Boleyn 4.5",
                        "John Smith 2",
                        "Anna Boleyn 11",
                        "Andrew Cox 1.5",
                    ]
                )
            )

    main()
