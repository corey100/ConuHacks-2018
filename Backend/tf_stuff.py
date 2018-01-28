from subprocess import call

def retrain_model():
    call(["python3", "/Users/jasonle/Projects/CONUHacks/Final_Idea/tensorflow/tensorflow/examples/image_retraining/retrain.py", "--image_dir", "images"])
