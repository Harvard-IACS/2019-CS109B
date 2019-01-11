import json
import re
from os import listdir
from os.path import isfile, join

import pandas as pd


# Script to extract grade to cvs from a path.
# Components must be put in this way.
#
# Inside *markdown*
# To refer to a question : #?
# To refer to a comment : #>
# To refer to a grade : #-
#
# THe scrip will read all the jupyter nothebook in a path and will to generate a new path *equal to the
# same/result/* with the new jupyter notebook with out the grade for the students.

def div_color(note, color_div, color_note):
    return "<div class='alert alert-block alert-" + color_div + \
           "'><b>Question :</b><span style = 'color:" + color_note + \
           "'>" + note + "</span></div>"


class GradeComments:
    def __init__(self, input_file_name, pos_name_user):
        self.input_filename = input_file_name
        self.pos_name_user = pos_name_user

    @staticmethod
    def update_jupyter_notebook(self, jupyter_notebook_new, name_file):
        with open(self.input_filename + 'results/' + name_file, 'w') as outfile:
            json.dump(jupyter_notebook_new, outfile)

    @staticmethod
    def add_cell_author(jupiter_notebook, author, role, address, email):
        jupiter_notebook['cells'].append(

            {'cell_type': 'markdown', 'metadata': {},
             'source': ['<script>\n', '  $(document).ready(function(){\n', "    $('div.prompt').hide();\n",
                        "    $('div.back-to-top').hide();\n", "    $('nav#menubar').hide();\n",
                        "    $('.breadcrumb').hide();\n", "    $('.hidden-print').hide();\n", '  });\n', '</script>\n',
                        '\n', '<footer id="attribution" style="float:right; color:#999; background:#fff;">\n',
                        'Checked by' + author + ", " + role + ", " + address + ", " + email + '\n', '</footer>']}
        )
        return

    @staticmethod
    def div_color(note, type_comment=None, color='primary', color_note='black'):
        # Type : Question, Comments or Grade
        # color : [primary, secondary, success, danger, warning, info, light and dark]
        # https://getbootstrap.com/docs/4.0/components/alerts/
        # color_note : [red, blue, ..., ]

        return "<div class='alert alert-block alert-" + color + \
               "'><b>" + type_comment + " :</b>" \
                                        "<span style = 'color:" + color_note + "'>" + note + "</span></div>"

    def get_grade_and_comments(self, remove=True):
        global context
        dfgrade = pd.DataFrame(columns=['Name', 'Question', 'Grade', 'Comments'])

        for name_file in [f for f in listdir(self.input_filename) if isfile(join(self.input_filename, f))]:
            if '.ipynb' in name_file:
                name_student = name_file.split('_')[-self.pos_name_user]
                print('User : ', name_student)
                temp_jupyter_notebook = json.load(open(self.input_filename + name_file, 'r'))
                context = {}

                for i in temp_jupyter_notebook.get('cells'):
                    if i['cell_type'] == 'markdown':
                        # print(i['source'])
                        for idx, item in enumerate(i['source']):
                            # print(item)
                            context['Name'] = name_student

                            if item.startswith('#? '):
                                print('Question : ', re.findall(r"(?:#? )(.*)", item))
                                i['source'][idx] = self.div_color(item.split('#? ')[-1], "Question", "success", "black")
                                context['Question'] = item.split('#? ')[-1]

                            if item.startswith('#> '):
                                print('Comments : ', re.findall(r"(?:#> )(.*)", item))
                                i['source'][idx] = self.div_color(item.split('#> ')[-1], "Comments", "info", "black")
                                context['Comments'] = item.split('#> ')[-1]

                            if item.startswith('#- '):
                                grade = int(item.split('#- ')[-1]) / 5
                                if grade < 0.6:
                                    if remove:
                                        print('Grade : ', re.findall(r"(?:#- )(.*)", item))
                                        context['Grade'] = grade
                                        i['source'].remove(item)
                                    else:
                                        i['source'][idx] = self.div_color(item.split('#- ')[-1], "Grade", "danger",
                                                                          "black")
                                        context['Grade'] = grade
                                elif 0.61 <= grade < 0.9:
                                    if remove:
                                        print('Grade : ', re.findall(r"(?:#- )(.*)", item))
                                        context['Grade'] = grade
                                        i['source'].remove(item)
                                    else:
                                        i['source'][idx] = self.div_color(item.split('#- ')[-1], "Grade", "warning",
                                                                          "black")
                                        context['Grade'] = grade

                                elif 0.91 < grade <= 1:
                                    if remove:
                                        print('Grade : ', re.findall(r"(?:#- )(.*)", item))
                                        context['Grade'] = grade
                                        i['source'].remove(item)
                                    else:
                                        i['source'][idx] = self.div_color(item.split('#- ')[-1], "Grade", "success",
                                                                          "black")
                                        context['Grade'] = grade

                    # if i['cell_type'] == 'markdown':
                    dfgrade = dfgrade.append(context, ignore_index=True)

                self.add_cell_author(temp_jupyter_notebook, "Javier Machin",
                                     "Student Assistant", "Harvard", "havy211@gmail.com")
                self.update_jupyter_notebook(self, temp_jupyter_notebook, name_file)

        return dfgrade


if __name__ == "__main__":
    input_filename = '/Users/havy/PycharmProjects/2019-CS109B-private/content/scripts_playground/test_extract_grades_to_csv/'
    pos_name_user = 3
    ext = GradeComments(input_filename, pos_name_user)
    df_grade = ext.get_grade_and_comments(remove=False)
    df_grade.to_csv(input_filename + 'Homework_.csv')

    print('Pavlos the extraction of notes are already Done')
