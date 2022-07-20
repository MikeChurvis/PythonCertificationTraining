class LuxuryWatch:
    watches_created = 0

    def __init__(self):
        self.__class__.watches_created += 1
        self.engraving = None

    @classmethod
    def get_watches_created(cls):
        return cls.watches_created

    @classmethod
    def create_with_engraving(cls, text):
        cls.validate_engraving(text)
        new_watch = cls()
        new_watch.engraving = text
        return new_watch

    @staticmethod
    def validate_engraving(text):
        constraints = [
            ("Length must be no more than 40 characters.", len(text) <= 40),
            ("Must contain alphanumeric characters only.", text.isalnum()),
        ]

        failed_constraints = list(label for label, constraint_satisfied in constraints if not constraint_satisfied)

        if failed_constraints:
            raise ValueError("Engraving text fails the following constraints:\n\t" + "\n\t".join(failed_constraints))


if __name__ == '__main__':
    def main():
        LuxuryWatch()

        LuxuryWatch.create_with_engraving('Foo')

        try:
            LuxuryWatch.create_with_engraving('foo@baz.com')
        except ValueError as e:
            print(e)

        print(LuxuryWatch.get_watches_created())


    main()
