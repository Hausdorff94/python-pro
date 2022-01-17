# Hello 3 -> HelloHelloHello
# Name 2 -> NameName
# Platform 4 -> PlatformPlatformPlatformPlatform

def make_repeater_of(n):
    def repeater(s):
        assert type(s) == str, "Expected a string, only strings are supported."
        return s * n
    return repeater

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hello"))

if __name__ == "__main__":
    run()
