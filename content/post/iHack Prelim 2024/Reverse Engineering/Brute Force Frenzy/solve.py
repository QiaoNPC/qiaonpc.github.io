def find_license_key(predefined_values, target_sum):
    license_key = []
    for i in range(8):
        found = False
        for c in range(32, 127):  # Printable ASCII characters
            iVar1 = ((c * (i + 1) + 13) % 97)
            if iVar1 == predefined_values[i]:
                license_key.append(chr(c))
                found = True
                break
        if not found:
            return None  # If no valid character is found

    if len(license_key) == 8:
        computed_sum = sum(((ord(license_key[i]) * (i + 1) + 13) % 97) for i in range(8))
        return ''.join(license_key)
    return None

# Example usage:
predefined_values = [91, 62, 66, 19, 59, 51, 72, 41]
target_sum = 200  # Replace with the actual target sum value
license_key = find_license_key(predefined_values, target_sum)
print(f"The license key is: {license_key}")
