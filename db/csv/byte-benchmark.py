# benchmarking purposes, do not grade

if __name__ == "__main__":
    import os, time

    avg_table_sizes = {}

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    for filename in os.listdir("."):
        if not filename.endswith(".csv"):
            continue 
        with open(filename) as f:
            for line in f:
                if not line: # skip empty lines 
                    continue 

                if filename not in avg_table_sizes:
                    avg_table_sizes[filename] = [len(line)]

                avg_table_sizes[filename].append(len(line))

    total_chars = sum([sum(x) for x in avg_table_sizes.values()])
    total_lines = sum([len(x) for x in avg_table_sizes.values()])
    total_avg = round(total_chars/total_lines, 2)

    overall_table_sizes = {}

    for table, lens in avg_table_sizes.items():
        avg_table_sizes[table] = round(sum(lens)/len(lens), 2) # average
        overall_table_sizes[table] = f'{sum(lens)} of {len(lens)}'

    with open("benchmark.log", "w+") as f:
        for table in avg_table_sizes: # get table names
            f.write(f'{table}: {overall_table_sizes[table]} - '
                    f'{avg_table_sizes[table]}\n')
            
        f.write(f'total: {total_chars} of {total_lines} - {total_avg}')

    print("complete! check out benchmark.log")