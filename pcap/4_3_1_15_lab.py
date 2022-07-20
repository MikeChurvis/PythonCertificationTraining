def read_file(filename: str) -> str:
    with open(filename, "r") as file:
        return file.read()


def get_latin_character_manifest(content: str) -> dict:
    manifest = {}

    for character in content:
        if not character.isalpha():
            continue

        character = character.lower()

        if character not in manifest:
            manifest[character] = 0

        manifest[character] += 1

    return manifest


def print_latin_character_manifest(manifest: dict) -> None:
    print(generate_histogram_from_manifest(manifest))


def generate_histogram_from_manifest(manifest: dict) -> str:
    manifest_items = sorted(manifest.items(), key=lambda item: item[1], reverse=True)
    return "\n".join(f"{character} -> {count}" for character, count in manifest_items)


def write_histogram_to_file(manifest: dict, filename: str) -> None:
    histogram = generate_histogram_from_manifest(manifest)
    with open(f"{filename}.hist", 'w') as file:
        file.write(histogram)


if __name__ == "__main__":

    def main(filename=None):
        content = read_file(filename or input("Enter filename: "))
        manifest = get_latin_character_manifest(content)
        write_histogram_to_file(manifest, filename)

    main("pcap_lab_4_3_1_16.txt")
