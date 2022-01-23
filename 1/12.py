class App():
    def __init__(self) -> None:
        print(self.main(26))

    def main(self, n):
        if n == 1:
            result = 1

        elif n % 2:
            result = 2 * self.main(n-2)
        elif not n % 2 and n > 1:
            result = n + self.main(n-1)

        return result

if __name__ == "__main__":
    app = App()