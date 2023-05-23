#include <windows.h>

int main() {
    while (true) {
        if (GetAsyncKeyState(VK_LBUTTON) & 0x8000) {
            POINT cursorPos;
            GetCursorPos(&cursorPos);
            
            if (cursorPos.y >= 10) {
                cursorPos.y += 10;
                SetCursorPos(cursorPos.x, cursorPos.y);
            }
        }
    }
    
    return 0;
}
