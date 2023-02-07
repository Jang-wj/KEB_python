def is_que_full():
    global size, queue, front, rear
    if rear == size - 1:
        return True
    else:
        return False


def is_que_empty():
    global size, queue, front, rear
    if front == rear:
        return True
    else:
        return False


def enqueue(data):
    global size, queue, front, rear
    if is_que_full():
        print("큐가 꽉 찼습니다.")
        return
    rear += 1
    queue[rear] = data


def dequeue():
    global size, queue, front, rear
    if is_que_empty():
        print("큐가 비었습니다.")
        return None
    front += 1
    data = queue[front]
    queue[front] = None

    for i in range(front + 1, rear + 1):  # 모든 사람을 한칸씩 앞으로 당긴다.
        queue[i - 1] = queue[i]
        queue[i] = None
    front = -1
    rear -= 1

    return data


def peek():
    global size, queue, front, rear
    if is_que_empty():
        print("큐가 비었습니다.")
        return None
    return queue[front + 1]


size = 5
queue = [None for i in range(size)]
front = rear = -1
mans = ['정국', '뷔', '지민', '진', '슈가']

if __name__ == "__main__":
    for i in mans:
        enqueue(i)
    print("대기 줄 상태 : ", queue)

    for i in range(size):
        print(dequeue(), '님 식당에 들어감')
        print("대기 줄 상태 : ", queue)

    print("식당 영업 종료!")
