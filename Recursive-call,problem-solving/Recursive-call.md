# 재귀호출
## 수학적 귀납법   
✔️ 명제 P(n)을 다음과 같이 증명하는 방법   
1. N = 1일 때 성립함을 보임
2. P(K)가 성립한다고 가정할 때, P(K + 1)이 성립함을 보임
3. 따라서 모든 자연수 n에 대하여 P(n)이 성립함
  - N이 1일 때 성립했으므로, 2일 때도 성립. 2일 때 성립했으므로 3일 때도 성립. ...

## 퀵정렬(Quick Sort)   
✔️ 재귀호출을 이용한 대표적인 정렬   
```py
def quickSort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    a = []
    b = []
    for i in range(1, len(array)):
        if array[i] <= pivot:
            a.append(array[i])
        else:
            b.append(array[i])

    left = quickSort(a)
    right = quickSort(b)
    
    return left + [pivot] + right 

def main():
    line = [int(x) for x in input("정렬할 수를 입력하세요 (예시:10 2 3 4 5 6 9 7 8 1): ").split()]

    print('정렬 결과:', *quickSort(line))

if __name__ == "__main__":
    main()
```
