import cv2
from keras.models import load_model
import numpy as np
import time

def get_input(delay, verbose = False):
    """
    Camera is active for delay seconds, a countdown of rock, paper, scissors begins from the last 3 seconds of delay.
    """
    start_time = time.time()
    count_down_index = 0 #Used for the countdown, increases by one after each of rock, paper and scissors
    model = load_model('keras_model.h5', compile = False)
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    while time.time() - start_time <= delay:
        current_time = time.time()

        if current_time - start_time >= delay - 3 and count_down_index == 0:
            count_down_index += 1   
            print("Rock!")

        if current_time - start_time >= delay - 2 and count_down_index == 1:
            print("Paper!")
            count_down_index += 1

        if current_time - start_time >= delay - 1 and count_down_index == 2:
            print("Scissors!")
            count_down_index += 1 

        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        if verbose == True:
            print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    return prediction[0]


