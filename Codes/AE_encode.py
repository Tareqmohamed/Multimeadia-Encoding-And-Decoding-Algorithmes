class SimpleArithmeticEncoder:
    def __init__(self):
        self.low = 0.0
        self.high = 1.0

    def encode(self, probability_low, probability_high):
        # تحديث النطاق بناءً على الاحتماليات
        range_size = self.high - self.low
        self.high = self.low + range_size * probability_high
        self.low = self.low + range_size * probability_low

    def get_encoded_value(self):
        return (self.low + self.high) / 2


# مثال على الاستخدام:
def AE(message, symbol_probabilities):
    encoder = SimpleArithmeticEncoder()

    for symbol in message:
        probability_low = sum(
            symbol_probabilities[s] for s in symbol_probabilities.keys() if s < symbol
        )
        probability_high = probability_low + symbol_probabilities[symbol]
        encoder.encode(probability_low, probability_high)

    encoded_value = encoder.get_encoded_value()
    print(symbol_probabilities)
    return encoded_value


############################################################################################################


class SimpleArithmeticDecoder:
    def __init__(self, encoded_value):
        self.low = 0.0
        self.high = 1.0
        self.encoded_value = encoded_value

    def decode(self, symbol_probabilities):
        decoded_message = ""

        while True:
            for symbol, (low_range, high_range) in symbol_probabilities.items():
                range_size = self.high - self.low
                probability_high = self.low + range_size * high_range
                if self.low <= self.encoded_value < probability_high:
                    decoded_message += symbol
                    self.high = probability_high
                    self.low = self.low + range_size * low_range
                    break

            if not (0 <= self.encoded_value < 1) or (self.high - self.low < 1e-2):
                break

        return decoded_message


def convert_to_range_probabilities(probabilities):
    sorted_probabilities = sorted(
        probabilities.items(), key=lambda x: x[1], reverse=True
    )

    cumulative_low = 0.0
    range_probabilities = {}

    for symbol, probability in sorted_probabilities:
        range_start = cumulative_low
        range_end = cumulative_low + probability
        range_probabilities[symbol] = (range_start, range_end)
        cumulative_low = range_end
    return range_probabilities


def AE_DECode(encoded, prob):
    converted_probabilities = convert_to_range_probabilities(prob)

    decoder = SimpleArithmeticDecoder(encoded)
    decoded_message = decoder.decode(converted_probabilities)
    return decoded_message
