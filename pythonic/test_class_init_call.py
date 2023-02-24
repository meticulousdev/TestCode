# test __init__ __call__
class Computer:
    def __init__(self, name: str, cpu_name: str, gpu_name: str):
        print("__init__")
        self.name = name
        self.cpu_name = cpu_name
        self.gpu_name = gpu_name

    def __call__(self, name: str, cpu_name: str, gpu_name: str) -> None:
        print("__call__")
        self.name = name
        self.cpu_name = cpu_name
        self.gpu_name = gpu_name

    def get_computer_info(self):
        print(f"name    : {self.name}")
        print(f"cpu name: {self.cpu_name}")
        print(f"gpu name: {self.gpu_name}\n")


if __name__ == "__main__":
    my_computer: Computer = Computer('AMD Laptop', 'AMD Rygen 5', 'Radeon')
    my_computer.get_computer_info()

    my_computer('Intel Laptop', 'Intel i5', 'RTX 3060')
    my_computer.get_computer_info()
