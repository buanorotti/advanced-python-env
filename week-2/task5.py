allowed_letters = set("ABCEHKMOPTXY")  # допустимые буквы

num_plates = int(input())  # количество номеров для проверки

for _ in range(num_plates):
    car_plate = input().strip()  

    is_valid = (
        len(car_plate) == 6 and
        car_plate[0] in allowed_letters and
        car_plate[1].isdigit() and
        car_plate[2].isdigit() and
        car_plate[3].isdigit() and
        car_plate[4] in allowed_letters and
        car_plate[5] in allowed_letters
    )

    print("Yes" if is_valid else "No")
