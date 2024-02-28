
def select_pivot(data:list[str]) -> str:
    return data[0]

def re_order_list(data:list[str]) -> list[str]:        
    if len(data) <= 1:
        return data
    pivot = select_pivot(data)
    lower_list, greather_list = [e  for e in data if e < pivot ], [e for e in data if e > pivot]  
    return re_order_list(lower_list) + [pivot] + re_order_list(greather_list)


def main(data:list[str]) -> None:    
    print(re_order_list(data))



if __name__ == "__main__":
    data = ["John",
    "Emily",
    "Michael",
    "Sarah",
    "David"]
    main(data)