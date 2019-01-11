import os
import sys
from datetime import datetime


class GenerateStructure:
    def __init__(self, number_of_lectures, number_of_labs, number_of_homework, number_of_advance_sections, folders,
                 default_directory, default_directory_lectures, default_directory_lecture_playground,
                 default_directory_labs, default_directory_labs_playground, default_directory_homework,
                 default_directory_homework_playground, default_directory_advance_sections):

        self.number_of_lectures = number_of_lectures
        self.number_of_labs = number_of_labs
        self.number_of_homework = number_of_homework
        self.number_of_advance_sections = number_of_advance_sections
        self.folders = folders
        self.default_directory = default_directory
        self.default_directory_lectures = default_directory_lectures
        self.default_directory_lecture_playground = default_directory_lecture_playground
        self.default_directory_labs = default_directory_labs
        self.default_directory_labs_playground = default_directory_labs_playground
        self.default_directory_homework = default_directory_homework
        self.default_directory_homework_playground = default_directory_homework_playground
        self.default_directory_advance_sections = default_directory_advance_sections

    @staticmethod
    def create_directory(directory, fold):
        os.makedirs(directory + fold)
        open(directory + fold + '/.placeholder', 'w').close()

    @staticmethod
    def create_index(directory, title, slug, i):
        with open(directory + "index.md", 'a')as index:
            index.write("Title: " + title + str(i) + '\n' +
                        "Date: " + datetime.today().strftime('%Y-%m-%d') + '\n' +
                        "Slug: " + slug + str(i) + '\n' +
                        "Author: " + '\n' +
                        '\n\n\n' + "# " + title + str(i) + '\n')

    # Create Lectures folders
    def create_lectures(self, directory, number_of_lectures, folders):
        for i in range(0, number_of_lectures):

            if not os.path.exists(directory):
                os.makedirs(directory)

            if not os.path.exists(directory + "lecture" + str(i)):
                os.makedirs(directory + "lecture" + str(i))

                directory_lectures = directory + "lecture" + str(i) + '/'

                for fold in folders:
                    self.create_directory(directory_lectures, fold)

                self.create_index(directory_lectures, "Lecture ", "lecture", i)

            else:
                print("The directory : '", directory + "lecture" + str(i), "' already exist.")

    # Create Lectures playground folders
    def create_lecture_playground(self, directory, number_of_lectures, folders):
        for i in range(0, number_of_lectures):

            if not os.path.exists(directory):
                os.makedirs(directory)

            if not os.path.exists(directory + "lecture" + str(i)):
                os.makedirs(directory + "lecture" + str(i))

                directory_lectures = directory + "lecture" + str(i) + '/'

                for fold in folders:
                    self.create_directory(directory_lectures, fold)

            else:
                print("The directory : '", directory + "lecture" + str(i), "' already exist.")

    # Create Labs folders
    def create_labs(self, directory, number_of_labs, folders):
        for i in range(0, number_of_labs):

            if not os.path.exists(directory):
                os.makedirs(directory)

            if not os.path.exists(directory + "lab" + str(i)):
                os.makedirs(directory + "lab" + str(i))

                directory_lab = directory + "lab" + str(i) + '/'

                for fold in folders:
                    self.create_directory(directory_lab, fold)

                self.create_index(directory_lab, "Lab ", "lab", i)

            else:
                print("The directory : '", directory + "lab" + str(i), "' already exist.")

    # Create Homework folders
    def create_homework(self, directory, number_of_labs, folders):
        for i in range(0, number_of_labs):

            if not os.path.exists(directory):
                os.makedirs(directory)

            if not os.path.exists(directory + "how" + str(i)):
                os.makedirs(directory + "how" + str(i))

                directory_homework = directory + "how" + str(i) + '/'

                for fold in folders:
                    self.create_directory(directory_homework, fold)

            else:
                print("The directory : '", directory + "homework" + str(i), "' already exist.")

    # Create Advance Sections folders
    def create_a_section(self, directory, advance_sections, folders):
        for i in range(0, advance_sections):

            if not os.path.exists(directory):
                os.makedirs(directory)

            if not os.path.exists(directory + "a-sec" + str(i)):
                os.makedirs(directory + "a-sec" + str(i))

                directory_a_section = directory + "a-sec" + str(i) + '/'

                for fold in folders:
                    self.create_directory(directory_a_section, fold)

                self.create_index(directory_a_section, "Advance Sections ", "a-section", i)

            else:
                print("The directory : '", directory + "Advance Sections" + str(i), "' already exist.")


if __name__ == "__main__":
    number_of_lectures = 10
    number_of_labs = 7
    number_of_homework = 7
    number_of_advance_sections = 7
    folders = ["data", "fig", "notes", "presentation"]

    default_directory = dir_path = os.path.dirname(os.path.realpath(__file__)) + '/'

    default_directory_lectures = default_directory + "lectures/"
    default_directory_lecture_playground = default_directory + "lecture_playground/"

    default_directory_labs = default_directory + "labs/"
    default_directory_labs_playground = default_directory + "lab_playground/"

    default_directory_homework = default_directory + "homework/"
    default_directory_homework_playground = default_directory + "homework_playground/"

    default_directory_advance_sections = default_directory + "a-section/"

    try:
        print("The default values are : \n")
        print("Number of lectures: ", number_of_lectures, '\n')
        print("Number of labs: ", number_of_labs, '\n')
        print("Default directory: ", default_directory, '\n')

        change = input("Do you want to change it ? Please press 'y' if you want or 'n' if you do not change it:")

        while change not in ('y', 'n'):
            change = input("Do you want to change it ? Please press 'y' if you want or 'n' if you do not change it:")

        if change == 'y':
            default_directory = input("Please enter the default directory: ")
            print("Default directory: ", default_directory, '\n')

            default_directory_lectures = default_directory + "lectures/"
            default_directory_lecture_playground = default_directory + "lecture_playground/"

            default_directory_labs = default_directory + "labs/"
            default_directory_labs_playground = default_directory + "lab_playground/"

            default_directory_homework = default_directory + "homework/"
            default_directory_homework_playground = default_directory + "homework_playground/"

            default_directory_advance_sections = default_directory + "a-section/"

            number_of_lectures = int(input("Please enter the number of lectures: "))
            print("Number of lectures: ", number_of_lectures, '\n')

            number_of_labs = int(input("Please enter the number of labs: "))
            print("Number of labs: ", number_of_labs, '\n')

            # number_of_homework = int(input("Please enter the number of homework: "))
            # print("Number of homework: ", number_of_homework, '\n')

            number_of_advance_sections = int(input("Please enter the number of advance sections: "))
            print("Number of advance sections: ", number_of_advance_sections, '\n')

        ge = GenerateStructure(number_of_lectures, number_of_labs, number_of_homework, number_of_advance_sections,
                               folders, default_directory, default_directory_lectures,
                               default_directory_lecture_playground, default_directory_labs,
                               default_directory_labs_playground, default_directory_homework,
                               default_directory_homework_playground, default_directory_advance_sections)

        ge.create_lectures(default_directory_lectures, number_of_lectures, folders)  # Create Lectures folders
        ge.create_lecture_playground(default_directory_lecture_playground,
                                     number_of_lectures, folders)  # Create Lectures playground folders

        ge.create_labs(default_directory_labs, number_of_labs, folders)  # Create Labs folders
        ge.create_labs(default_directory_labs_playground, number_of_labs, folders)  # Create Labs playground folders

        # ge.create_homework(default_directory_homework, number_of_homework, folders)  # Create Homework folders
        # ge.create_homework(default_directory_homework_playground,
        #                    number_of_homework, folders)  # Create Homework playground folders

        ge.create_a_section(default_directory_advance_sections, number_of_advance_sections,
                            folders)  # Create advance sections  folders


    except:
        print(sys.exc_info()[0])
