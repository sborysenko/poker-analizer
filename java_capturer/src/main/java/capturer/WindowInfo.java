package capturer;

import com.sun.jna.platform.win32.WinDef.HWND;

public class WindowInfo {
    public final HWND hWnd;
    public final String title;

    public WindowInfo(HWND hWnd, String title) {
        this.hWnd = hWnd;
        this.title = title;
    }

    @Override
    public String toString() {
        return title; // This is what will be displayed in the JComboBox
    }

    // Optional: equals and hashCode for better collection handling if needed
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        WindowInfo that = (WindowInfo) o;
        return hWnd.equals(that.hWnd);
    }

    @Override
    public int hashCode() {
        return hWnd.hashCode();
    }
}