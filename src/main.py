# Este script é um terminal simples que solicita uma data no formato ddmmaaaa e valida se a data é válida.

def is_valid_date(date_str):
    # Verifica se a data tem exatamente 8 caracteres
    if len(date_str) != 8:
        return False
    
    # Verifica se os caracteres são números
    if not date_str.isdigit():
        return False
    
    # Extrai os componentes da data
    day = int(date_str[0:2])
    month = int(date_str[2:4])
    year = int(date_str[4:8])
    
    # Verifica se o mês está entre 1 e 12
    if month < 1 or month > 12:
        return False
    
    # Verifica se o dia está dentro dos limites do mês
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    else:
        # Verifica se é ano bissexto
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False
    
    return True

def main():
    print("Bem-vindo ao terminal simples!")
    print("Por favor, digite uma data no formato ddmmaaaa:")
    
    while True:
        date_str = input("Data: ")
        
        if is_valid_date(date_str):
            print("Data válida!")
            break
        else:
            print("Data inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()