import random

def is_que_full():
    global size, queue, front, rear
    if front == (rear + 1) % size:
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
    rear = (rear + 1) % size
    queue[rear] = data


def dequeue():
    global size, queue, front, rear
    if is_que_empty():
        print("큐가 비었습니다.")
        return None
    front = (front + 1) % size
    data = queue[front]
    queue[front] = None
    return data


def peek():
    global size, queue, front, rear
    if is_que_empty():
        print("큐가 비었습니다.")
        return None
    return queue[(front + 1) % size]


def cal_time():
    global front, rear, size, queue
    time = 0
    for i in range(front+1, rear+1):
        time += queue[i][1]
    return time


size = 5
queue = [None for i in range(size)]
front = rear = 0
calls = [('사용', 9), ('환불', 4), ('기타', 1)]

if __name__ == "__main__":
    for i in range(size-1):
        enqueue(random.choice(calls))
        print(f'현재 대기 콜 : {queue}')
        print(f'예상 대기 시간 {cal_time()}')


