from typing import Tuple

def boot_index(data:list[str])-> Tuple[int]:
    lower = 0
    upper = len(data) - 1
    return lower, upper

def calculate_middle_index(lower:int, upper:int) -> int:
    sum_index = lower + upper
    if sum_index == 1:
        return lower
    return sum_index // 2

def get_index(md_index:str,search_element:str) -> Tuple[bool]:
    if md_index == search_element:
        return True

def greater_or_less(md_index:int,lower_index:int,upper_index:int)->Tuple[int]:
    if md_index > upper_index:
        lower_index = upper_index
        return 

def main(data:list[str]) -> None:
    search_element = input("ingresa el nombre que desas buscar").lower()
    data = sorted([name.lower() for name in data])
    lower_index, upper_index = boot_index(data)
    md_index = calculate_middle_index(lower_index,upper_index)
    while md_index > 0:
        md_index = calculate_middle_index(lower_index,upper_index)
        finded = get_index(data[md_index],search_element)
        if finded :
            print(f"EL indice para {data[md_index]} es {md_index}")
            break
        lower_index,upper_index = greater_or_less(md_index,lower_index,upper_index)
    print("No se encontraron datos :(")





if __name__ == "__main__":
    names = [
    "John",
    "Emily",
    "Michael",
    "Sarah",
    "David",
    "Emma",
    "Daniel",
    "Olivia",
    "Matthew",
    "Sophia",
    "Andrew",
    "Ava",
    "James",
    "Isabella",
    "William",
    "Mia",
    "Joseph",
    "Charlotte",
    "Benjamin",
    "Amelia",
    "Christopher",
    "Ella",
    "Joshua",
    "Grace",
    "Alexander"
]
    main(names)