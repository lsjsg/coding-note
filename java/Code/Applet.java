import java.awt.Graphics;
import javax.swing.JApplet;
public class Myapplet extends JApplet{
    public void paint(Graphics g){
        super.paint(g);
        g.drawString("This is a Java Applet!",25,25)
    }
}