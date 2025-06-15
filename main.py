import yamale


def main():
    schema = yamale.make_schema("./schema/tournament.yaml")
    data = yamale.make_data("./data/tournaments/appt-manila-2025.yaml")
    print(yamale.validate(schema, data))


if __name__ == "__main__":
    main()
