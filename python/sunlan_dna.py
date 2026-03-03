def nuc_freq(dna):
    a_count = 0
    c_count = 0
    t_count = 0
    g_count = 0

    for i in dna:
        if i == 'A':
            a_count += 1
        elif i == 'C':
            c_count += 1
        elif i == 'G':
            g_count += 1
        elif i == 'T':
            t_count += 1

    nucleo_freq = {'A': a_count, 'C': c_count, 'G': g_count, 'T': t_count}
    for key, value in nucleo_freq.items():
        print(f"{key}{value}", end=" ")