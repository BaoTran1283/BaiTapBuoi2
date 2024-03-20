#include <stdio.h>
#include <math.h>

// Hàm kiểm tra số chính phương
int isPerfectSquare(int number) {
    int squareRoot = sqrt(number);
    return (squareRoot * squareRoot == number);
}


void countPerfectSquares(int n) {
    int count = 0;
    printf("Cac so chinh phuong nho hon %d:\n", n);

    for (int i = 1; i < n; i++) {
        if (isPerfectSquare(i)) {
            printf("%d ", i);
            count++;
        }
    }

    printf("\nTong cong co %d so chinh phuong\n", count);
}

int main() {
    int n;

    printf("Nhap vao mot so nguyen duong: ");
    scanf("%d", &n);

    countPerfectSquares(n);

    return 0;
}
