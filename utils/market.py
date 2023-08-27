def tam_sam_som(total_population=30, tam_limits=[1], sam_limits=[0.05], som_limits=[0.05]):
    tam_result = total_population
    for lim in tam_limits:
        tam_result *= tam_result * lim

    sam_result = tam_result
    for lim in sam_limits:
        sam_result *= lim

    som_result = sam_result
    for lim in som_limits:
        som_result *= lim

    return round(tam_result, 2), round(sam_result, 2), round(som_result, 2)

