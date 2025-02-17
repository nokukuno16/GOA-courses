def bin_rota(seating_plan):
    rota = []
    
    for i, row in enumerate(seating_plan):
        if i % 2 == 0:
            rota.extend(row)
        else:
            rota.extend(row[::-1]) 
    
    return rota

