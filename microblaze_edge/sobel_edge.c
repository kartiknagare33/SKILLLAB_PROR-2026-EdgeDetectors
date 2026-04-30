#include <stdio.h>
#include <stdint.h>
#include "image.h"   // 🔥 THIS LINE IS CRITICAL

uint8_t output[HEIGHT][WIDTH];

void sobel_edge()
{
    int gx, gy, mag;

    for(int y = 1; y < HEIGHT - 1; y++)
    {
        for(int x = 1; x < WIDTH - 1; x++)
        {
            gx = -input[y-1][x-1] - 2*input[y][x-1] - input[y+1][x-1]
                 + input[y-1][x+1] + 2*input[y][x+1] + input[y+1][x+1];

            gy = -input[y-1][x-1] - 2*input[y-1][x] - input[y-1][x+1]
                 + input[y+1][x-1] + 2*input[y+1][x] + input[y+1][x+1];

            if(gx < 0) gx = -gx;
            if(gy < 0) gy = -gy;

            mag = gx + gy;
            if(mag > 255) mag = 255;

            output[y][x] = (uint8_t)mag;
        }
    }
}

/*
    Output image in PGM format (ASCII)
    You will capture this from UART and save as edges.pgm
*/
void print_pgm()
{
    // PGM header
    printf("P2\n");
    printf("%d %d\n", WIDTH, HEIGHT);
    printf("255\n");

    // Pixel data
    for(int y = 0; y < HEIGHT; y++)
    {
        for(int x = 0; x < WIDTH; x++)
        {
            printf("%d ", output[y][x]);
        }
        printf("\n");
    }
}

int main()
{
    printf("Starting Sobel Edge Detection...\n");

    sobel_edge();

    printf("Done. Sending image...\n");

    print_pgm();

    printf("END\n");

    while(1);

    return 0;
}