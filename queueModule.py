#!/usr/bin/env python
# coding: utf-8

# In[38]:


class Queue:
    def __init__(self, size=5):
        self.queue = [] # 큐 역할을 할 빈 리스트
        self.size = size # 큐의 크기
        self.rear = 0 # 큐의 뒤쪽 포인터 => 큐의 데이터가 입력될 때마다 1씩 증가한다.
        self.front = 0 # 큐의 앞쪽 포인터 => 큐의 데이터가 제거될 때마다 1씩 증가한다.
        
    # add => 입력
    def add(self, data):
        if data not in self.queue: # 중복 검사
            if self.rear < self.size: # overflow 검사
                # 큐에 데이터를 저장하고 rear를 1증가 시킨다.
                self.queue.append(data)
                self.rear += 1
                print('큐에 {}을(를) 저장합니다. rear = {}, front = {}'.format(data, self.rear, self.front))
            else:
                # overflow가 발생되면 큐가 가득찼다는 메시지를 출력한다.
                print('overflow 발생... 큐가 가득차서 {}를(을) 저장할 수 없습니다.'.format(data))
            # ===== if   
        else:
            print('{}는(은) 중복된 데이터 입니다.'.format(data))
        # ===== if
        self.view()
    # ===== add()
        
    # view => 데이터 보기
    def view(self):
        print('큐에 저장된 데이터 => ', end='')
        # underflow 인가 검사한다. => 큐는 underflow 조건이 2가지가 있다.
        # 데이터가 1건도 입력되지 않았을 경우 rear는 0이므로 underflow가 발생한다.
        # 데이터가 모두 제거된 경우 rear와 front가 같아져서 underflow가 발생된다.
        if self.rear <= 0 or self.rear == self.front:
            print('없음')
        else:
            for i in range(self.front, self.rear):
                print(self.queue[i], end=' ')
            print()
        # ==== if
    # ===== view()
    
    # remove => 출력
    def remove(self):
        if self.rear <= 0 or self.rear == self.front: # underflow 인가 검사한다.
            print('큐에 저장된 데이터가 없습니다.')
        else:
            data = self.queue[self.front] # 큐에 저장된 제거할 데이터를 얻어온다.
            self.queue[self.front] = '제거됨' # 얻어온 데이터를 큐에서 제거한다.
            self.front += 1 # 큐에서 데이터를 제거했으므로 front를 1증가시킨다.
            print('큐에서 {}을(를) 제거합니다. rear = {}, front = {}'.format(data, self.rear, self.front))
            self.view()
        # ===== if
    # ===== remove()


# In[39]:


if __name__ == '__main__':
    queue = Queue()
    print('='*70)
    queue.view()
    queue.remove()
    print('='*70)
    queue.add(111)
    queue.add(111)
    queue.add(333)
    queue.add(999)
    queue.add(555)
    queue.add(777)
    queue.add(888)
    print('='*70)
    queue.view()
    print('='*70)
    queue.remove()
    queue.remove()
    queue.remove()
    queue.remove()
    queue.remove()
    print('='*70)
    queue.remove()
    print('='*70)
    queue.view()
    print('='*70)

