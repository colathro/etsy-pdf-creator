from PyPDF2 import PdfFileMerger
import os
import datetime

# 365
# 2
# 156

os.chdir('./Vintage Yellow Schedule Book 2')

cover = 'cover.pdf'
day = 'day.pdf'
newyear = 'newyear.pdf'
grocery = 'grocery.pdf'
workout = 'workout.pdf'
weekly = 'weekly.pdf'

merger = PdfFileMerger()

# add cover page
merger.append(cover)

# add newyear page
merger.append(newyear)

tracking_date = datetime.date(2022, 1, 1)

for i in range(0, 52):
    merger.append(weekly)
    merger.append(workout)
    merger.append(grocery)

    for i in range(0,7):
        tracking_date += datetime.timedelta(days=1)
        print(tracking_date)
        merger.append(day)

merger.write("result.pdf")
merger.close()