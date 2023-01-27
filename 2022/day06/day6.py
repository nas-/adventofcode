from collections import deque


def find_start_of_packet(data: str, capacity: int) -> int:
    buffer = deque(maxlen=capacity)
    for i, caracter in enumerate(data):
        buffer.append(caracter)
        if len(buffer) == capacity:
            if len(set(buffer)) == capacity:
                return i + 1
    return -1


if __name__ == '__main__':
    with open("input.txt") as fin:
        inputs = fin.readline().strip()
    print(f"First part result {find_start_of_packet(inputs, 4)}")
    print(f"Second part result {find_start_of_packet(inputs, 14)}")
