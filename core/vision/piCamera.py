import os
import time
import libcamera
from picamera2 import Picamera2

class Camera:
    def __init__(self):
        """Initialize the Raspberry Pi camera using libcamera."""
        self.picam2 = Picamera2()
        config = self.picam2.create_still_configuration(main={'size': (640, 480)})
        self.picam2.configure(config)
        self.picam2.start()
        
        time.sleep(2)

    def take_photo(self, path):
        """Capture and save a photo to the given path."""
        if os.path.exists(path):
            os.remove(path) 
        
        self.picam2.capture_file(path)
        print(f"Image saved successfully: {path}")

    def close(self):
        """Release the camera resources."""
        self.picam2.close()
        print("Camera released.")
