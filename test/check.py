from EorzeaEnv.EorzeaTime import EorzeaTime


class K:
    def thetime():
        while 1:
            t = str(EorzeaTime.now())
            print("\r"+t, end="")


if __name__ == "__main__":
    K.thetime()
