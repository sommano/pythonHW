def sort_contacts(dictionary):
    contact_info = sorted(dictionary.items())

    for (key,value) in contact_info:
        return[(key,) + value for key, value in sorted(dictionary.items())]