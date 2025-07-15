package capturer;

import javax.swing.SwingUtilities;

public class Main {
    public static void main(String[] args) {
        // Ensure GUI updates happen on the Event Dispatch Thread
        SwingUtilities.invokeLater(() -> new ScreenshotGUI());
    }
}