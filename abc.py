def mask_credit_card(card_number, mask_char):
    start_pos = 6
    end_pos = 12
    max_length_pos = end_pos - start_pos
    sub_masking = list(card_number[start_pos:end_pos])
    for i in range(max_length_pos):
        sub_masking.append(mask_char)
    sub_masking.extend(card_number[end_pos:])
    return ''.join(sub_masking)

# Example Usage:
card_number = "1234567890123456"
mask_char = '*'
masked_card = mask_credit_card(card_number, mask_char)
print("Masked Card Number:", masked_card)
