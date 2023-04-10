#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int numbers[], size_t numbers_len) {
    int sum = 45;

    for (int i = 0; i < numbers_len; i++)
    {
        sum = sum - numbers[i];
    }
    return sum;
}