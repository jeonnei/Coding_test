// 출처:https://www.acmicpc.net/problem/3003

#include<stdio.h>

int main() {
    int a[6] = { 1,1,2,2,2,8 };//체스
    int b = 0;
    for (int i = 0;i < 6;i++) {// 사용자 입력받은후 뺀값 저장
        scanf_s("%d", &b);
        a[i] = a[i] - b;
    }
    for (int i = 0;i < 6;i++) {//결과 출력
        printf("%d ", a[i]);
    }
}