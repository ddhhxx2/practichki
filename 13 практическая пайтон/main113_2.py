def read_baggage_data(file_name):
    baggage_data = []
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 2:
                count = int(parts[0])
                weight = float(parts[1])
                baggage_data.append((count, weight))
    return baggage_data

def calculate_average_weight(baggage_data):
    total_items = sum(count for count, weight in baggage_data)
    total_weight = sum(weight for count, weight in baggage_data)
    return total_weight / total_items if total_items > 0 else 0

def analyze_baggage(baggage_data, t):
    average_weight = calculate_average_weight(baggage_data)
    similar_baggage_count = 0
    more_than_two_count = 0
    above_average_count = 0
    one_item_light_passenger_exists = False

    for count, weight in baggage_data:
        # a) Check if average weight is within the range
        if abs((weight / count) - average_weight) <= t:
            similar_baggage_count += 1
        
        # b) Count passengers with more than two items
        if count > 2:
            more_than_two_count += 1
        
        # b) Count passengers with above average items
        if count > average_weight:
            above_average_count += 1
        
        # c) Check if there's a passenger with one item less than t kg
        if count == 1 and weight < t:
            one_item_light_passenger_exists = True

    return similar_baggage_count, more_than_two_count, above_average_count, one_item_light_passenger_exists

def main():
    file_name = 'Bagazh.txt'
    t = float(input("Введите значение t (в кг): "))
    
    baggage_data = read_baggage_data(file_name)
    
    similar_baggage_count, more_than_two_count, above_average_count, one_item_light_passenger_exists = analyze_baggage(baggage_data, t)
    
    print(f"Количество пассажиров с багажом, средняя масса одной вещи которого отличается не более чем на {t} кг от общей средней массы: {similar_baggage_count}")
    print(f"Количество пассажиров с более чем двумя вещами: {more_than_two_count}")
    print(f"Количество пассажиров с количеством вещей выше среднего: {above_average_count}")
    print(f"Существует ли пассажир с одной вещью массой менее {t} кг: {'Да' if one_item_light_passenger_exists else 'Нет'}")
    if __name__=="__main__":
        main()