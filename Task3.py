import re

def normalize_phone(phone_number: str) -> str:
    # Залишаємо тільки цифри та плюс
    cleaned = re.sub(r"[^\d+]", "", phone_number)

    # If the nuber starts with '+'
    if cleaned.startswith("+"):
        # If it is +380..., then everything is okay
        if cleaned.startswith("+380"):
            return cleaned
        # If it is +38..., but without 0 — then it is okay too
        if cleaned.startswith("+38"):
            return cleaned
        # If it is a different international code, than return it as is.
        return cleaned

    # If the number starts with '380' → add only '+'
    if cleaned.startswith("380"):
        return "+" + cleaned

    # If the number starts with '0' or just numbers, add +38
    
    return "+38" + cleaned

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
