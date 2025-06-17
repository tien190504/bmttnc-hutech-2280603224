class RailfenceCipher:
    def __init__(self):
        pass
    def railfence_encrypt(self, plaintext, num_rails):
        rails = [[] for i in range(num_rails)]
        rail_index = 0
        direction = 1
        for char in plaintext:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        return ''.join(''.join(rail) for rail in rails)

    def railfence_decrypt(self, ciphertext, num_rails):
        rail_lenght = [0] * num_rails
        rail_index = 0
        direction = 1
        for _ in range(len(ciphertext)):
            rail_lenght[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        rails =[]
        start = 0
        for rail_len in rail_lenght:
            rails.append(ciphertext[start:start+rail_len])
            start += rail_len

        plain_text = ""
        rail_index = 0
        direction = 1
        for _ in range(len(ciphertext)):
            plain_text += rails[rail_index][0]
            rails[rail_index] = rails[rail_index][1:]
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        return plain_text