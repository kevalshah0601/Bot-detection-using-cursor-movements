#include <X11/Xlib.h>
#include <X11/Xutil.h>
#include <X11/extensions/XTest.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>

void changeDisplayColor(Display *display) {
    int screen_num = DefaultScreen(display);
    Window root = DefaultRootWindow(display);

    XSetWindowAttributes swa;
    swa.background_pixel = WhitePixel(display, screen_num);
    Window win = XCreateWindow(display, root, 0, 0, DisplayWidth(display, screen_num), DisplayHeight(display, screen_num), 0, CopyFromParent, InputOutput, CopyFromParent, CWBackPixel, &swa);

    XMapWindow(display, win);
    XFlush(display);
}

void moveCursor(int x, int y) {
    Display *display = XOpenDisplay(NULL);
    if (display == NULL) return;

    Window dest_w = DefaultRootWindow(display);
    XWarpPointer(display, None, dest_w, 0, 0, 0, 0, x, y);
    XFlush(display);
    XCloseDisplay(display);
}

int main() {
    Display *display = XOpenDisplay(NULL);
    if (display == NULL) return 1;

    changeDisplayColor(display);

    int size = 4096;
    int x_cord[300];
    int y_cord[300];
    char x_buffer[size];
    char y_buffer[size];

    int x_file = open("x_test.txt", O_RDONLY);
    int y_file = open("y_test.txt", O_RDONLY);

    int x_bytes = read(x_file, x_buffer, size);
    int y_bytes = read(y_file, y_buffer, size);

    char* num = strtok(x_buffer, " ");
    int idx = 0;

    while(num != NULL){
        x_cord[idx] = atoi(num);
        num = strtok(NULL, " ");
        idx++;
    }

    num = strtok(y_buffer, " ");
    idx = 0;

    while(num != NULL){
        y_cord[idx] = atoi(num);
        num = strtok(NULL, " ");
        idx++;
    }

    for (int i = 0; i < 300; ++i) {
        moveCursor(x_cord[i], y_cord[i]);
        usleep(10000);
    }

    usleep(1000000);

    XCloseDisplay(display);

    return 0;
}
