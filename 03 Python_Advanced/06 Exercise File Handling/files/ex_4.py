import os
def extract_files(dir):
    return [el for el in dir if "." in el]

def get_report_for_foles_extensions(files):
    report = {}
    for file in files:
        file_name, extention = file.split(".")
        if extention not in report:
            report[extention] = []
        report[extention].append(file_name)
    return report

dir_content = os.listdir()

files = extract_files(dir_content)
report_info = get_report_for_foles_extensions(files)

for extension, file_name in sorted(report_info.items(), key=lambda x: x[0]):
    print(f".{extension}")
    print(*[f"- - - {name}.{extension}" for name in file_name], sep="\n")




