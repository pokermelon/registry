import yamale


def validate(schema_path: str, data_path: str):
    schema = yamale.make_schema(schema_path)
    data = yamale.make_data(data_path)
    yamale.validate(schema, data)


def main():
    validate("./schema/festival.yaml", "./data/festivals/appt-manila-2025.yaml")
    validate("./schema/series.yaml", "./data/series/appt.yaml")
    validate("./schema/venue.yaml", "./data/venues/ph-okada-manila.yaml")


if __name__ == "__main__":
    main()
