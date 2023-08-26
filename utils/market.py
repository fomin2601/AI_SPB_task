def tam_sam_som(total_population=30, tam_limits=[1], sam_limits=[1], som_limits=[1]):
    tam_result = total_population
    for lim in tam_limits:
        tam_result *= tam_result * lim

    sam_result = tam_result
    for lim in sam_limits:
        sam_result *= sam_limits

    som_result = sam_result
    for lim in som_limits:
        som_result *= lim

    return tam_result, sam_result, som_result

