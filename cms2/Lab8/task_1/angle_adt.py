"""Lab8.1_angle_adt.py"""
class AngleADT:
    """
    Abstract Data Type for encoding
    messages as camera rotation angles
    """
    def __init__(self):
        """Constructor the AngleADT"""
        self.angles = [0.0]  # Starting position of the camera

    def encode_message(self, message):
        """
        Encode the given message as an array of camera rotation angles.
        Args:
            message (str): The message to encode.
        Returns:
            list: The array of camera rotation angles.
        """
        encoded_angles = []
        prev_angle = 0.0

        for char in message:
            hex_digits = hex(ord(char))[2:]# ascii_value =
            # Convert ASCII value to 2-digit hexadecimal string
            # hex_digits = format(ascii_value, '02X')

            for hex_digit in hex_digits:
                # print(hex_digit)
                # Each hexadecimaldigit corresponds to a rotation angle
                angle = int(hex_digit, 16) * 22.5
                diff = angle - prev_angle

                if diff == 0.0:
                    # Handle unchanged angle (two consecutive identical digits)
                    encoded_angles.append(360.0)
                else:
                    encoded_angles.append(diff)

                prev_angle = angle

        self.angles = encoded_angles  # Update angles list with new encoded angles
        return self.angles
encoder = AngleADT()
message = "hello"
encoded_angles = encoder.encode_message(message)
print(encoded_angles)
# # [135.0, 45.0, -45.0, -22.5, 22.5, 135.0, -135.0, 135.0, -135.0, 202.5]

# message = "1 січня"
# encoded_angles = encoder.encode_message(message)
# print(encoded_angles)
#[67.5,-45.0,22.5,-45.0,90.0,360.0,-67.5,67.5,22.5,22.5,
# -45.0,360.0,67.5,-67.5,-22.5,225.0,-202.5,360.0,247.5]
