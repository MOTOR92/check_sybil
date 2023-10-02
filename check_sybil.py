# Функция для проверки адреса
def check_address(address):
    with open("list_sybil_address.txt", "r") as file:
        addresses = file.read().splitlines()
        if address in addresses:
            return f"{address} - найден в списке"
        else:
            return f"{address} - не найден в списке"

# Запрос адресов у пользователя
user_addresses = []

print("Введите адреса кошельков MetaMask (для завершения ввода введите пустую строку):")

while True:
    address = input()
    if not address:
        break
    user_addresses.append(address.strip())

# Вызов функции для проверки адресов
results = {}

for address in user_addresses:
    result = check_address(address)
    results[address] = result

# Вывод результатов
for address, result in results.items():
    if "не найден" in result:
        print("\033[92m" + result)  # Зеленый цвет для "не найден"
    else:
        print("\033[91m" + result)  # Красный цвет для "найден"
