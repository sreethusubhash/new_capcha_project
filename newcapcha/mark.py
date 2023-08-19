def marks():
    subjects=['physics','chemistry','English']
    marks=[]
    for i in range(len(subjects)):
        mark=input(f'Enter the mark of {subjects[i]}: ')
        marks.append(mark)
    var=dict(zip(subjects,marks))
    return var