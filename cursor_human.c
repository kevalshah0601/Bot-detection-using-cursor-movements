#include <X11/Xlib.h>
#include <unistd.h>
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>

int main() {
    Display* display = XOpenDisplay(NULL);
    time_t startTime;
    time_t currentTime;

    int* xarr;
    int* yarr;
    int delt = 10000;
    int t = 3;
    int n = (t*1000000) / delt;
    int idx = 0;
    int count = 0;
    int cycles = 1;

    xarr = (int*)malloc(n * sizeof(int));
    yarr = (int*)malloc(n * sizeof(int));

    int x_cord;
    int y_cord;
    int x_coordinate;
    int y_coordinate;
    char space = ' ';
    char new_line = '\n';

    x_cord = open("x_test.txt", O_CREAT | O_WRONLY | O_TRUNC, 0666);
    y_cord = open("y_test.txt", O_CREAT | O_WRONLY | O_TRUNC, 0666);

    for(int i = 3; i >=1; i--){
        printf("Starting in %d.....\n", i);
        usleep(1000000);
    }

    startTime = time(NULL);
    if (display) {
        while (1) {
            currentTime = time(NULL);

            if(count == cycles) break;
            
            if (idx >= n) {

                for (int i = 0; i < idx; i++) {
                    x_coordinate = xarr[i];
                    y_coordinate = yarr[i];

                    char x_buffer[20];
                    char y_buffer[20];

                    sprintf(x_buffer, "%d", x_coordinate);
                    sprintf(y_buffer, "%d", y_coordinate);

                    write(x_cord, x_buffer, strlen(x_buffer));
                    write(x_cord, &space, sizeof(space));

                    write(y_cord, y_buffer, strlen(y_buffer));
                    write(y_cord, &space, sizeof(space));
                }

                write(x_cord, &new_line, sizeof(new_line));
                write(y_cord, &new_line, sizeof(new_line));

                idx = 0;
                currentTime = time(NULL);
                startTime = currentTime;
                printf("Done\n");
                count++;
            }

            Window root, child;
            int rootX, rootY, winX, winY;
            unsigned int mask;
            XQueryPointer(display, DefaultRootWindow(display), &root, &child, &rootX, &rootY, &winX, &winY, &mask);

            printf("Cursor Position: x=%d, y=%d, Timestamp: %ld\n", winX, winY, currentTime);

            xarr[idx] = winX;
            yarr[idx] = winY;
            idx++;

            usleep(delt);
        }

        XCloseDisplay(display);
    }

    usleep(1000000);

    return 0;
}