from typing import Tuple
import sys

def boot_index(data:list[str])-> Tuple[int]:
    lower = 0
    upper = len(data) - 1
    return lower, upper

def calculate_middle_index(lower:int, upper:int) -> int:      
    return (lower + upper) // 2

def get_index(md_index:str,search_element:str) -> bool:
    if md_index == search_element:
        return True
    return False

def greater_or_less(data:list[str],md_index:int,lower_index:int,upper_index:int,search_element:str)->Tuple[int]:
    if data[md_index] > search_element:
        upper_index = md_index  - 1  
    else:
        lower_index = md_index + 1
    return lower_index,upper_index

def main(data:list[str]) -> None:
    search_element = input("\n ingresa el nombre que desas buscar \n").lower()
    data = sorted([name.lower() for name in data])
    lower_index, upper_index = boot_index(data)
    while upper_index - lower_index >= 0:
        md_index = calculate_middle_index(lower_index,upper_index)
        finded = get_index(data[md_index],search_element)
        if finded :
            print(f"EL indice para {data[md_index]} es {md_index}")
            sys.exit()
        lower_index,upper_index = greater_or_less(data,md_index,lower_index,upper_index,search_element)
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