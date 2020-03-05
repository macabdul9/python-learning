"""
 @author    : macab (macab@debian)
 @file      : emoji
 @created   : Wednesday Mar 20, 2019 23:05:24 IST
"""

import emoji


if __name__ == "__main__":

    # grinning face
    print("\U0001f600")

    # grinning squinting face
    print("\U0001F606")

    # rolling on the floor laughing
    print("\U0001F923")

    print(emoji.emojize(":grinning_face_with_big_eyes:"))
    print(emoji.demojize('😍'))