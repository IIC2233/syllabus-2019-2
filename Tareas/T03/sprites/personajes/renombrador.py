import os


dirc = {
    'Female adventurer': 'character_femaleAdventurer_',
    'Female person': 'character_femalePerson_',
    'Male adventurer': 'character_maleAdventurer_',
    'Male person': 'character_malePerson_',
    'Robot': 'character_robot_',
    'Zombie': 'character_zombie_'
}


def main():
    for directory, text in dirc.items():
        for filename in os.listdir(directory):
            src = os.path.join(directory, filename)
            dst = src.replace(text, '')

            print(src, '\t', dst)
            os.rename(src, dst)


if __name__ == '__main__':
    main()
