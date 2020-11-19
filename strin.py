if __name__ == '__main__':
    s = input()


    def _isupper(sr):
        l = len(sr)
        for i in range(l):
            if sr[i].isupper():
                return True
            else:
                continue
        return False


    def _islower(sr):
        l = len(sr)
        for i in range(l):
            if sr[i].islower():
                return True
            else:
                continue
        return False


    def _isdigit(sr):
        l = len(sr)
        for i in range(l):
            if sr[i].isdigit():
                return True
            else:
                continue
        return False


    def _isalpha(sr):
        l = len(sr)
        for i in range(l):
            if sr[i].isalpha():
                return True
            else:
                continue
        return False


    print(s.isalnum())
    print(_isalpha(s))
    print(_isdigit(s))
    print(_islower(s))
    print(_isupper(s))
