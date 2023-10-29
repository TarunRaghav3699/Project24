import cv2
import numpy as np

def create_meter_reading(image):
  """Creates a meter reading from an image of a meter.

  Args:
    image: A numpy array representing the image of the meter.

  Returns:
    A float representing the meter reading.
  """

  # Convert the image to grayscale.
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Detect the needle of the meter.
  edges = cv2.Canny(gray, 50, 150)

  # Find the center of the meter.
  center = np.mean(np.where(edges == 255), axis=1)

  # Calculate the angle of the needle.
  angle = np.arctan2(center[1] - image.shape[0] / 2, center[0] - image.shape[1] / 2)

  # Convert the angle to a meter reading.
  max_meter_reading = 100
  min_meter_reading = 0
  meter_reading = angle * (max_meter_reading - min_meter_reading) / 360

  return meter_reading

# Read the image of the meter.
image = cv2.imread("meter_reading.jpg")

# Create a meter reading.
meter_reading = create_meter_reading(image)

# Print the meter reading.
print(meter_reading)
