from PyPDF2 import PdfFileMerger
import os
import datetime

os.chdir('./New')

cover = 'cover.pdf'
newyear = 'newyear.pdf'
savings = 'savings.pdf'
todo = 'todo.pdf'
grocery = 'grocery.pdf'
workout = 'workout.pdf'
weekly1 = 'weekly1.pdf'
weekly2 = 'weekly2.pdf'


merger = PdfFileMerger()

# add cover page
merger.append(cover)

# add newyear page
merger.append(newyear)

# add newyear page
merger.append(savings)

for i in range(0, 52):
    merger.append(todo)
    merger.append(grocery)
    merger.append(workout)
    merger.append(weekly2)

merger.write("result.pdf")
merger.close()