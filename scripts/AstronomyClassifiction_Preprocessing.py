# Dependencies
import cv2
import os

# Input directory
input_directories = r'project_root/data/raw/'

def preprocessing():
    global input_directories
    for directory in os.walk(input_directories):
        if directory[0] != input_directories:

        # Set input and output directories
            input_directory = directory[0]
            output_directory = input_directory.replace("raw", "preprocessed")
            label = "_" + input_directory.split("/")[-1].replace("_images","")

            if not os.path.exists(output_directory):
                os.makedirs(output_directory)

            # Set target size
            target_size = (224, 224)

            # Iterate over input directory
            for filename in os.listdir(input_directory):
                # Load image
                image = cv2.imread(os.path.join(input_directory, filename))
                
                # Resize image
                image = cv2.resize(image, target_size)
                
                # Save image
                output_filename = os.path.splitext(filename)[0] + label +'.jpg'
                cv2.imwrite(os.path.join(output_directory, output_filename), image)


if __name__ == "__main__":
    preprocessing()
