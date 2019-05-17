while True:
    answer = int(input('Найти факториал для: '))

    def factorial_finder(answer):
        result = 1
        next_count = 2
        limit = answer
        while limit > 1:
            result *= next_count
            next_count += 1
            limit -= 1
        return result

    var = factorial_finder(answer)
    print(var, end='\n\n')
    
