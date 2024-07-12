class Bin2DenException(Exception):
    pass


def bin2den(binstring):
    # Validate binary string
    if not all(bit in '01' for bit in binstring):
        raise Bin2DenException("Non-binary string")

    # Convert binary string to decimal
    decimal_value = int(binstring, 2)

    return decimal_value
