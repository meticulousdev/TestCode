from tqdm import tqdm
from time import sleep


if __name__ == "__main__":
    test_list = [i for i in range(100)]
    for i in tqdm(test_list):
        print(end="\033[K")
        sleep(0.1)
