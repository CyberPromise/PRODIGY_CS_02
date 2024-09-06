# prompt: Develop a simple image encryption tool using pixel manipulation. You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images.

from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
  """
  Encrypts an image using a simple pixel manipulation technique.

  Args:
    image_path: Path to the image file.
    key: Encryption key (an integer).

  Returns:
    None. Saves the encrypted image to a new file.
  """
  try:
    img = Image.open(image_path)
    img_array = np.array(img)

    # Apply a simple XOR operation with the key to each pixel value
    encrypted_array = img_array ^ key

    # Create a new image from the encrypted array
    encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8))

    # Save the encrypted image
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully!")

  except FileNotFoundError:
    print("Image file not found.")
  except Exception as e:
    print(f"An error occurred: {e}")


def decrypt_image(image_path, key):
  """
  Decrypts an image encrypted using the encrypt_image function.

  Args:
    image_path: Path to the encrypted image file.
    key: Encryption key (an integer).

  Returns:
    None. Saves the decrypted image to a new file.
  """
  try:
    img = Image.open(image_path)
    img_array = np.array(img)

    # Apply the XOR operation again to decrypt
    decrypted_array = img_array ^ key

    # Create a new image from the decrypted array
    decrypted_img = Image.fromarray(decrypted_array.astype(np.uint8))

    # Save the decrypted image
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully!")

  except FileNotFoundError:
    print("Image file not found.")
  except Exception as e:
    print(f"An error occurred: {e}")
