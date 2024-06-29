import random
import datetime

LOG_FNAME = ".log"
t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')


def main():
    key_word = "おなか吹田市"
    now = datetime.datetime.now(JST)
    time_str = now.strftime('%Y %m %d %H %M %S')
    shuffuled_key_word = ''.join(random.sample(key_word, len(key_word)))

    outline = f"{time_str}\t{shuffuled_key_word}\n"
    with open(LOG_FNAME, 'a') as f:
        f.write(outline)
    print(outline, end="")


if __name__ == "__main__":
    main()
