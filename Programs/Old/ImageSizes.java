/*
* @author: Dimension Detector Team
* Reads in all images and extracts total_frame_width and total_frame_height and prints these to textfiles
*/

import java.awt.image.BufferedImage;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import javax.imageio.ImageIO;
public class ImageSizes {

    public static void main(String[] args) throws IOException {

        String parentLocation = "C:\\Users\\SHEETHAL\\Documents\\GitHub\\Annotator\\VGGAnnotator\\Images\\";

        File folder = new File(parentLocation);
        File[] listOfFiles = folder.listFiles();
        for (int i = 0; i < listOfFiles.length; i++) {
            System.out.println("starting the loop");

            if (listOfFiles[i].isFile()) {
                String name = listOfFiles[i].toString();


                BufferedImage bimg = ImageIO.read(new File(name));
                int width          = bimg.getWidth();
                int height         = bimg.getHeight();

                System.out.println(listOfFiles[i].getName() + " " + width + " width pixels" + " " + height + " height pixels");



                String filename = listOfFiles[i].getName();
                filename = filename.replace(".jpg", ".txt");
                filename = filename.replace(".Jpg", ".txt");
                filename = filename.replace(".JPG", ".txt");
                filename = filename.replace(".png", ".txt");
                filename = filename.replace(".Png", ".txt");
                filename = filename.replace(".PNG", ".txt");
                filename = filename.replace(".jpeg", ".txt");
                filename = filename.replace(".Jpeg", ".txt");
                filename = filename.replace(".JPEG", ".txt");
                filename = filename.replace(".gif", ".txt");
                filename = filename.replace(".Gif", ".txt");
                filename = filename.replace(".GIF", ".txt");

                File textfile = new File("C:\\Users\\SHEETHAL\\Documents\\GitHub\\Annotator\\VGGAnnotator\\ImageSizes\\" + filename);

                BufferedWriter writer = new BufferedWriter(new FileWriter(textfile));
                writer.write(width + " " + height);

                writer.close();
            }

        }
    }
}
