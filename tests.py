from API_Call import get_country_metadata

if __name__ == "__main__":
    print("Running tests for API_Call:")

    table = get_country_metadata()
    print(table)
