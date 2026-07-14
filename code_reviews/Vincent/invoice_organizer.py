import os


INVOICES_FOLDER = os.path.join("invoices")


def sort_to_file(checked_file_list):
    for file, format_check in checked_file_list:
        file_src = os.path.join(INVOICES_FOLDER, file)

        if format_check: # sorts files into corresponding folders
            month = file.split("_")[2].split(".")[0]
            file_dst = os.path.join(INVOICES_FOLDER, month, file)
        elif not format_check:
            file_dst = os.path.join(INVOICES_FOLDER, "needs_review", file)

        if not check_path_exists(file_dst):
            os.rename(file_src, file_dst)


def check_path_exists(path):
    return os.path.exists(path)


def create_review_folder():
    review_folder = os.path.join(INVOICES_FOLDER, "needs_review")
    if not check_path_exists(review_folder):
        os.mkdir(review_folder)


def create_folders(folder_names):
    create_review_folder()

    for folder in folder_names:
        folder_path = os.path.join(INVOICES_FOLDER, folder)
        if not check_path_exists(folder_path):
            os.mkdir(folder_path)


def extract_month(checked_file_list):
    month_set = set() # prevent doubles

    for file, format_check in checked_file_list:
        if format_check:
            month = file.split("_")[2].split(".")[0] # Hallelujah
            month_set.add(month)

    return month_set


def check_file_name_format(file):
    if len(file.split("_")) == 3 and file.split("_")[2].endswith(".pdf"):
        return True
    return False # returns False so PyCharm does not flag inconsistent returns


def link_file_with_format_check(file_list):
    checked_file_list = []

    for file in file_list:
        format_check = check_file_name_format(file)
        file_format = (file, format_check)
        checked_file_list.append(file_format)

    return checked_file_list


def get_checked_file_list(path):
    file_list = []

    for entry in os.listdir(path):
        entry_path = os.path.join(path, entry)
        if os.path.isfile(entry_path): # prevents the program to sort every folder into "needs_review"
            file_list.append(entry)

    return link_file_with_format_check(file_list)


def main():
    checked_file_list = get_checked_file_list(INVOICES_FOLDER)
    month_set = extract_month(checked_file_list)
    create_folders(month_set)
    sort_to_file(checked_file_list)
    print("Goodbye - Guten Einkauf!")


if __name__ == "__main__":
    main()