import  os


def dir_files (dir):
    return [el for el in dir if '.' in el]


def extension_info(files):
    result = {}
    for file in files:
        file_name, extension = file.split('.')
        if extension not  in result:
            result[extension] = []
        result[extension].append(file_name)
    return  result


my_dir = os.listdir()
files = dir_files(my_dir)
report = extension_info(files)

with open(os.path.expanduser("~/Desktop/report.txt"), "w") as report_file:
    for extnsn, file_names in sorted(report.items(), key=lambda x: x[0]):
        # print(f'.{extnsn}')
        # print(*[f"--- {name}.{extnsn}" for name in file_names], sep="\n")
        report_file.write(f'.{extnsn}')
        report_file.write('\n')
        for name in file_names:
            report_file.write(f"--- {name}.{extnsn}")
            report_file.write('\n')

